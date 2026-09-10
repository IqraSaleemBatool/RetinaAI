import ollama
from rag.rag import retrieve_chunks, build_context
import json
import re

MODEL_NAME = "llama3.2:3b"

def _to_text(value):
    """Convert any value to plain text string"""
    if value is None:
        return "Medical information is currently unavailable."
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, dict):
        parts = []
        for key, val in value.items():
            label = str(key).replace("_", " ").title()
            if isinstance(val, list):
                val = "\n".join(f"  - {item}" for item in val)
            elif isinstance(val, dict):
                subparts = []
                for subkey, subval in val.items():
                    subparts.append(f"  **{subkey}**: {subval}")
                val = "\n".join(subparts)
            parts.append(f"### {label}\n{val}")
        return "\n\n".join(parts)
    if isinstance(value, list):
        return "\n".join(f"- {item}" for item in value)
    return str(value)


def generate_initial_report(left_prediction, right_prediction):
    print(f"[LLM] Generating report for: Left={left_prediction}, Right={right_prediction}")
    
    # Get RAG context - ONLY for the predicted diseases
    left_query = f"{left_prediction} definition symptoms risk factors"
    right_query = f"{right_prediction} definition symptoms risk factors"
    
    left_results = retrieve_chunks(left_query, k=3)
    right_results = retrieve_chunks(right_query, k=3)
    
    left_context = build_context(left_results)
    right_context = build_context(right_results)

    # PROMPT THAT FORCES CORRECT DISEASE MAPPING
    prompt = f"""
You are a medical information assistant for a retinal disease research prototype.

PREDICTED CONDITIONS:

LEFT EYE:
{left_prediction}

RIGHT EYE:
{right_prediction}

RETRIEVED MEDICAL INFORMATION:

LEFT EYE:
{left_context}

RIGHT EYE:
{right_context}

Instructions:

1. Explain the predicted condition(s) for the LEFT eye using the LEFT retrieved information.
2. Explain the predicted condition(s) for the RIGHT eye using the RIGHT retrieved information.
3. If multiple conditions are predicted, explain each predicted condition.
4. If "Others" is predicted, explain that it represents other retinal findings not covered by the named disease classes.
5. If "Normal" is predicted, explain what normal retinal findings mean.
6. Do not introduce unrelated diseases.
7. Do not invent medical information.
8. Do not say that the AI prediction is a confirmed diagnosis.

For each eye provide:

### Overview
What the predicted condition is.

### Symptoms and Signs
Important symptoms or retinal signs.

### Risk Factors
Important risk factors.

### Detection
How the condition is generally detected.

### Management
General management or monitoring information.

Return ONLY valid JSON:

{{
  "left": "complete medical explanation for the LEFT eye",
  "right": "complete medical explanation for the RIGHT eye"
}}
"""


    try:
        print("[LLM] Calling model...")
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            options={
                "temperature": 0.1,  # Very low for consistency
                "num_ctx": 1024,
                "num_predict": 500
            }
        )

        response_text = response["message"]["content"]
        print(f"[LLM] Response: {response_text[:150]}...")
        
        # Clean response
        response_text = re.sub(r'```json\s*', '', response_text)
        response_text = re.sub(r'```\s*', '', response_text)
        
        # Extract JSON
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            json_str = json_match.group()
        else:
            json_str = response_text
        
        try:
            report = json.loads(json_str)
            
            left_text = _to_text(report.get("left", ""))
            right_text = _to_text(report.get("right", ""))
            
            # If left_text is empty or too short, provide fallback
            if not left_text or len(left_text) < 20:
                left_text = f"### {left_prediction}\n\nInformation about {left_prediction} is being processed. Please consult a healthcare professional."
            
            if not right_text or len(right_text) < 20:
                right_text = f"### {right_prediction}\n\nInformation about {right_prediction} is being processed. Please consult a healthcare professional."
            
            return {
                "left": left_text,
                "right": right_text
            }
            
        except json.JSONDecodeError as e:
            print(f"JSON parse error: {e}")
            # Return text-based fallback with correct disease names
            return {
                "left": f"### {left_prediction}\n\n{response_text[:200]}\n\nPlease consult a healthcare professional.",
                "right": f"### {right_prediction}\n\nAdditional information available."
            }

    except Exception as e:
        print(f"[LLM] Error: {e}")
        return {
            "left": f"### {left_prediction}\n\nMedical information currently unavailable. Please consult a healthcare professional.",
            "right": f"### {right_prediction}\n\nMedical information currently unavailable. Please consult a healthcare professional."
        }


def answer_followup_question(
    left_prediction,
    right_prediction,
    user_question
):
    print(f"[LLM] Follow-up: '{user_question}'")
    
    try:
        # Get RAG context for the question
        query = f"{left_prediction} {user_question}"
        results = retrieve_chunks(query, k=3)
        context = build_context(results)
        
        prompt = f"""
You are a medical information assistant.

PREDICTED CONDITIONS:
LEFT EYE: {left_prediction}
RIGHT EYE: {right_prediction}

USER QUESTION: {user_question}

RETRIEVED INFORMATION:
{context}

CRITICAL:
1. ONLY answer about {left_prediction} and {right_prediction}
2. DO NOT mention other diseases
3. If "Normal" is predicted, explain what normal retinal findings are
4. If "Others" is predicted, explain it means other conditions

Provide a clear, detailed answer with:
### Overview
### Symptoms
### Risk Factors  
### Management
"""

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            options={
                "temperature": 0.2,
                "num_ctx": 1024,
                "num_predict": 450
            }
        )
        
        answer = response["message"]["content"]
        answer = re.sub(r'```\w*\s*', '', answer)
        answer = re.sub(r'```\s*', '', answer)
        
        return answer.strip() or f"Information about {left_prediction} is being processed."

    except Exception as e:
        print(f"[LLM] Follow-up error: {e}")
        return f"Unable to answer about {left_prediction}. Please try again."
