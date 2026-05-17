from ultralytics import YOLO
import os

class ClampDetector:
    def __init__(self, model_path: str):
       
        self.model = YOLO(model_path)

    def predict(self, source_path: str, output_dir: str):
        
        results = self.model.predict(
            source=source_path,
            project=output_dir,
            name="predict",
            save=True,
            conf=0.4,
            exist_ok=True  
        )
        return results[0]