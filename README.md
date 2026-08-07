# RetinaAI: AI-Based Clinical Decision Support System

## Project Overview

RetinaAI is an AI-powered Clinical Decision Support System (CDSS) designed to assist in the early screening of retinal eye diseases from fundus images.

The system integrates:

- Computer Vision (EfficientNet-B4)
- Explainable AI (Grad-CAM)
- Retrieval-Augmented Generation (RAG)
- Large Language Model (LLM)
- Flask Web Application
- Microsoft SQL Server

This project is intended for research and educational purposes and **does not replace professional medical diagnosis**.

---

## Features

- Upload retinal fundus image
- AI-based disease prediction
- Confidence score visualization
- Grad-CAM heatmap
- AI-generated explanation
- RAG-based medical knowledge retrieval
- Clinical recommendations
- Prediction history
- Modern responsive dashboard

---

## Technologies

### Backend

- Python
- Flask
- PyTorch
- OpenCV

### Frontend

- HTML5
- CSS3
- JavaScript

### AI

- EfficientNet-B4
- Grad-CAM
- Retrieval-Augmented Generation (RAG)
- Large Language Model (LLM)

### Database

- Microsoft SQL Server

---

## Project Structure

```
RetinaAI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── uploads/
├── models/
├── database/
└── rag/
```

---

## Workflow

1. Upload retinal image
2. Image preprocessing
3. Disease prediction using EfficientNet-B4
4. Grad-CAM visualization
5. Retrieve medical knowledge using RAG
6. Generate explanation using LLM
7. Display recommendations
8. Store prediction history

---

## Current Progress

- [x] GitHub Repository Created
- [x] Flask Project Setup
- [x] Initial Dashboard UI
- [ ] Image Upload Backend
- [ ] EfficientNet-B4 Integration
- [ ] Grad-CAM Integration
- [ ] RAG Integration
- [ ] LLM Integration
- [ ] SQL Server Integration
- [ ] Deployment

---

## Contributors

- **Iqra Batool**
- **Aqsa Majeed**

---

## Disclaimer

This application is a research prototype intended for educational and early screening purposes only. It should not be used as a substitute for professional medical diagnosis or treatment.
