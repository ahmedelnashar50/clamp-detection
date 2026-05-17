# 🛠️ Automated Clamp Detection System (YOLO11 + FastAPI)

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![YOLO11](https://img.shields.io/badge/AI-YOLO11m-green.svg)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)
![TailwindCSS](https://img.shields.io/badge/Frontend-TailwindCSS-38B2AC.svg)

An end-to-end Computer Vision system designed to detect industrial clamps in video streams. This project integrates a fine-tuned **YOLO11m** model with a high-performance **FastAPI** backend and a modern web dashboard for real-time video processing and visualization.

## 🌟 Key Features
- **State-of-the-Art Detection:** Fine-tuned YOLO11m architecture for precise object localization.
- **Asynchronous Backend:** Built with FastAPI for rapid API response and efficient file handling.
- **Modern Web UI:** A responsive, user-friendly interface for uploading videos and viewing results side-by-side.
- **Production-Ready Architecture:** Modular code structure following professional software engineering practices.

## 🏗️ Project Structure
```text
clamp-detection-system/
├── app/                    # Backend Source Code (FastAPI)
│   ├── core/               # AI Model Loaders & Logic
│   ├── static/             # Uploads & Processed Output Storage
│   └── main.py             # API Routes & Application Entry
├── web/                    # Frontend Source Code (HTML/JS/CSS)
├── models/                 # Saved Weights (best.pt)
├── data/                   # Raw Dataset & Extraction Scripts
├── notebook/               # Colab Training Logs & Research
└── requirements.txt        # Project Dependencies

🚀 Getting Started
1. Installation
Clone the repository and install the required dependencies:

Bash
pip install -r requirements.txt
2. Running the Backend
Start the FastAPI server using Uvicorn:

Bash
python -m uvicorn app.main:app --reload
3. Launching the Dashboard
Open web/index.html in your browser (preferably using VS Code's Live Server to handle local file protocols).

📊 Model Performance
The model was trained for 100 epochs with the following metrics:

mAP50: 0.995 (99.5% accuracy at IoU 0.5)

Recall: 1.0 (Identified all clamps in validation set)

Precision: 0.997

Inference Speed: ~400ms per frame (Optimized for CPU/GPU)

## 📺 Model Demonstration

To showcase the effectiveness of the fine-tuned YOLO11m model, you can view the comparison between the raw industrial feed and the AI-processed output:

| Original Video | AI Detection Output |
| :--- | :--- |
| [🔗 Watch Original Feed](https://drive.google.com/file/d/1O_QSp5XG2JpjrW84Q56khUelQkJKtPbq/view?usp=sharing) | [🔗 Watch AI Processed Result](https://drive.google.com/file/d/177p-XZ5s_5ZF-j9tAUp3IBSb7NuJS5Hz/view?usp=sharing) |

> **Note:** The detection video shows the system identifying clamps with an average confidence score of **98%**.

🛠️ Tech Stack
AI Framework: Ultralytics YOLO11

Deep Learning: PyTorch

Backend: FastAPI, Uvicorn

Frontend: Tailwind CSS, Vanilla JavaScript

Developed by Ahmed Elnashar - AI Engineer