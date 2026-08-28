
# RetinaAI Final Prototype

## Final flow

- Sidebar contains **Home** and **Dashboard** only.
- Dashboard accepts **Left Eye + Right Eye** images for one patient.
- Images appear in the right-side viewer.
- Analyze Patient Images produces the current prototype prediction.
- A hard-coded explanation is shown according to the predicted class.
- At the bottom of the dashboard:
  - **New Prediction** resets/refreshes the dashboard for a new case.
  - **Ask About This Prediction** opens a placeholder for the future RAG/LLM conversation.
- New Prediction is intentionally removed from the sidebar.

The current prediction is hard-coded as Diabetic Retinopathy (94.2%) for UI testing. Replace `predict_patient()` in `app.py` with the trained model later.

Replace the image placeholders in `templates/index.html` and `YOUR_BACKGROUND_RETINAL_IMAGE_URL` in `static/style.css`.

Run with:

python app.py

Then open http://127.0.0.1:5000


## Latest UI changes

- Home **Start Analysis** button is now **Go to Dashboard**. Clicking it only takes the user to the Dashboard; image upload starts there.
- The right-side patient image viewer now displays the **Left Eye and Right Eye vertically**, making better use of the available panel space.


## V2 minimal fixes

Only two UI changes were made to the original V2:
1. Removed the Home-page "Go to Dashboard" button.
2. Reduced the right-side retinal image viewer and kept it sticky/static.

The original V2 upload, prediction, result, New Prediction, and Ask About This Prediction logic was preserved.


## Compact right viewer update

Only the right-side viewer sizing was changed:
- Width reduced from 430px to 330px.
- Each vertical eye image area reduced to about 145px high.
- Viewer remains sticky/static.
- All V2 upload, prediction, result, New Prediction, and Ask About This Prediction logic remains unchanged.


## Square viewer update
Only the right-side viewer was adjusted for square 1:1 retinal images. The images remain vertically stacked, the viewer remains sticky/static, and the application logic was not changed.


## Final Home gallery fix
Home-page retinal disease gallery images are now displayed in square 1:1 cards. No application logic was changed.


## Final Home image-frame fix
The Home-page retinal gallery now uses true square 1:1 frames, matching the dashboard image shape. Images are contained inside the square frame so the square fundus images are not stretched or cropped.
=======
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
>>>>>>> ed8811f1d29fc9bb7c0b03e7fbc53b9f90ff75e4
