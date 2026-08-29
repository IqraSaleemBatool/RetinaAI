import ollama
# from google import genai
# from google.genai import types
# from llm.config import GEMINI_API_KEY
from rag.rag import retrieve_chunks, build_context
import json

MODEL_NAME = "llama3.2:1b"


def generate_initial_report(left_prediction, right_prediction):

    left_query = f"""
    {left_prediction}
    definition symptoms signs risk factors
    detection diagnosis treatment management prevention
    """

    right_query = f"""
    {right_prediction}
    definition symptoms signs risk factors
    detection diagnosis treatment management prevention
    """

    left_results = retrieve_chunks(left_query, k=2)
    right_results = retrieve_chunks(right_query, k=2)

    left_context = build_context(left_results)
    right_context = build_context(right_results)

    prompt = f"""
You are a medical information assistant.

The AI model predicted:

LEFT EYE: {left_prediction}
RIGHT EYE: {right_prediction}

LEFT EYE MEDICAL INFORMATION:
{left_context}

RIGHT EYE MEDICAL INFORMATION:
{right_context}

Generate medical information separately for each eye.

Keep LEFT and RIGHT eye information separate.

For each eye explain,when available:
- What the condition is
- Important symptoms/signs
- Risk factors
- Detection
- General management information if available

Do not invent information.
Do not claim that the prediction is a confirmed diagnosis.
Keep the answer concise.

Return ONLY valid JSON in exactly this format:

{{
    "left": "summary for the left eye",
    "right": "summary information for the right eye"
}}

"""

    try:

        response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
               "role": "user",
               "content": prompt
            }
           ],
        options={
            "temperature": 0.2,
            "num_ctx": 1024
            }
        )

        response_text = response["message"]["content"]

        try:
            report = json.loads(response_text)

            if report:
                return report
        
        except json.JSONDecodeError:
            print("Llama did not return valid JSON:")
            print(response_text)

        return {
            "left": "Medical information is currently unavailable.",
            "right": "Medical information is currently unavailable."
        }
        
    except Exception as e:

        print("Initial report error:", e)

        return {
            "left": (
                "Medical information is currently unavailable."
            ),
            "right": (
                "Medical information is currently unavailable."
            )
        }


def answer_followup_question(
    left_prediction,
    right_prediction,
    user_question
):

    left_query = f"{left_prediction}: {user_question}"

    right_query = f"{right_prediction}: {user_question}"

    left_results = retrieve_chunks(left_query, k=3)
    right_results = retrieve_chunks(right_query, k=3)

    left_context = build_context(left_results)
    right_context = build_context(right_results)

    prompt = f"""
You are a medical information assistant.

AI predictions:

LEFT EYE: {left_prediction}
RIGHT EYE: {right_prediction}

USER QUESTION:
{user_question}

LEFT EYE RETRIEVED INFORMATION:
{left_context}

RIGHT EYE RETRIEVED INFORMATION:
{right_context}

Answer the user's question using ONLY the retrieved information.

If the question concerns both eyes, clearly separate the
LEFT and RIGHT eye information.

If it concerns only one eye, focus on that condition.

Do not invent medical information.
Do not treat the AI prediction as a confirmed diagnosis.
Keep the answer concise.
"""

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                  "role": "user",
                  "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        print("Follow-up LLM error:", e)

        return (
            "The LLM service is temporarily unavailable. "
            "Please try again later."
        )