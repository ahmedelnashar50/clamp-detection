from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import shutil
import os
from .core.model_loader import ClampDetector

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "static/uploads")
OUTPUT_DIR = os.path.join(BASE_DIR, "static/outputs")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")


detector = ClampDetector(os.path.join(BASE_DIR, "../models/best.pt"))

@app.post("/analyze")
async def analyze_video(file: UploadFile = File(...)):
    try:

        input_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(input_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)


        detector.predict(input_path, OUTPUT_DIR)
        

        video_url = f"http://127.0.0.1:8000/static/outputs/predict/{file.filename}"
        
        return {"status": "success", "video_url": video_url}
    except Exception as e:
        return {"status": "error", "message": str(e)}