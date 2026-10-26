# RetinaAI — QCDP-BiFormer

## 1. Project Overview

RetinaAI is a Flask-based retinal image analysis research prototype designed to generate a joint patient-level prediction from left-eye and right-eye fundus images.

The application integrates the QCDP-BiFormer inference pipeline with a retrieval-augmented generation (RAG) system and a locally hosted large language model (LLM). It provides a web interface for image upload, prediction visualization, medical information reports, and follow-up questions.

The project is intended for research and educational purposes. Its output is not a confirmed medical diagnosis and must not replace professional medical evaluation.

## 2. Main Features

- Upload left-eye and right-eye fundus images for one patient.
- Generate a joint patient-level retinal disease prediction.
- Display prediction confidence, model probabilities, and relevant model outputs.
- Generate a medical information report using retrieved reference material and an LLM.
- Ask follow-up questions about the prediction.
- Provide a web interface through Flask, HTML, CSS, and JavaScript.
- Run the application in a Docker container.

## 3. Technologies Used

### Backend
- Python 3.11
- Flask
- PyTorch and TorchVision
- NumPy, SciPy, and pandas
- Pillow and OpenCV

### AI and Machine Learning
- QCDP-BiFormer inference pipeline
- FAISS for vector similarity search
- Sentence Transformers and a local embedding model
- Hugging Face Transformers
- XGBoost, where required by the model artifacts

### Retrieval-Augmented Generation and LLM
- RAG-based retrieval from a prepared reference knowledge base
- Ollama for local language-model inference
- Llama 3.2 3B, configured as `llama3.2:3b`

### Frontend
- HTML5
- CSS3
- JavaScript

### Deployment
- Docker
- Docker networking for communication between Flask and Ollama

## 4. Project Structure

```text
Prototype/
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── models/
│   ├── qcdp_biformer.py
│   ├── model checkpoints and supporting artifacts
│   └── module10_surrogates/
│
├── rag/
│   ├── rag.py
│   ├── odir5k_faiss.index
│   ├── odir5k_chunks.json
│   └── bge_model/
│
├── llm/
│   └── llm.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── script.js
    └── style.css
```

The model and RAG directories must contain all artifacts referenced by the application. The structure above summarizes the principal files; additional required files should be retained.

## 5. System Workflow

1. The user uploads left-eye and right-eye fundus images.
2. The Flask backend receives both images.
3. The QCDP-BiFormer inference pipeline processes the images and produces a joint patient-level prediction.
4. The application retrieves relevant medical information from the prepared knowledge base using FAISS and the embedding model.
5. Ollama generates a medical information report using the retrieved context.
6. The frontend displays the prediction and report.
7. The user can submit follow-up questions, which are answered using the configured RAG and LLM pipeline.

## 6. Prerequisites

- Python 3.11 for local development.
- Docker installed on the host machine.
- The complete source code and required model checkpoints.
- The FAISS index, reference chunks, and local embedding model.
- An Ollama service reachable from the Flask container.
- The configured language model, `llama3.2:3b`, available to Ollama.

## 7. Docker Configuration

The Dockerfile uses Python 3.11, installs the required system libraries and CPU-only PyTorch packages, installs the Python dependencies, copies the application files, and starts the Flask application on port 5000.

The application connects to Ollama using the endpoint configured in `llm/llm.py`. The Ollama service must be running and reachable through the configured Docker network.

## 8. Build and Run

Open PowerShell and navigate to the project directory:

```powershell
cd D:\RetinaAI\RetinaAI\Prototype
```

Start the existing Ollama container:

```powershell
docker start ollama
```

Build the RetinaAI Docker image:

```powershell
docker build -t retinaai:latest .
```

Run the application:

```powershell
docker run --rm --network retinaai-network -p 5000:5000 retinaai:latest
```

Open the following address in a browser:

http://127.0.0.1:5000

These commands assume that the `retinaai-network` Docker network exists and that the Ollama container is attached to it and reachable by the hostname `ollama`.

If the Ollama container is already running, Docker may report that it is already running when `docker start ollama` is executed. In that case, the service does not need to be started again.

## 9. API Endpoints

- `GET /` — Serves the web interface.
- `POST /predict` — Accepts both eye images and returns the prediction output and medical information report.
- `POST /ask` — Accepts a follow-up question and prediction context and returns an answer from the configured medical information pipeline.

## 10. Required Artifacts

The following resources must be available at the paths expected by the source code:

- Model checkpoints and supporting inference files.
- Disease prototypes and threshold configuration.
- Quality metric files and any required surrogate model files.
- FAISS vector index.
- Reference text chunks in JSON format.
- Local embedding model files.
- Ollama service and the configured language model.

The application may fail to start or perform inference if required files are missing.

## 11. Testing Checklist

- Confirm the Docker image builds successfully.
- Confirm the Flask application starts and is accessible.
- Confirm the model checkpoints and RAG files load.
- Upload both fundus images and verify the patient-level prediction.
- Verify that the medical information report is generated.
- Submit a follow-up question and verify that the answer is returned.
- Check the terminal logs for missing artifacts, dependency errors, or Ollama connection failures.

## 12. Limitations and Disclaimer

RetinaAI is a research prototype. Model confidence is not equivalent to clinical certainty, and the prediction should not be interpreted as a confirmed diagnosis.

Generated medical information depends on the available reference material and language-model output. The system must not replace examination, diagnosis, or treatment decisions made by a qualified healthcare professional.
