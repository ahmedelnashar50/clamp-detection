from ultralytics import YOLO
from roboflow import Roboflow
import os

def start_training():
    rf = Roboflow(api_key="dWeIsPmdrV9rCQGHcGIJ")
    project = rf.workspace("ai-is-all-you-need-ucjd0").project("clamp-detection-q3avj")
    version = project.version(3)
    dataset = version.download("yolov11")
   
    model = YOLO("yolo11m.pt") 

  
    model.train(
        data=os.path.join(dataset.location, "data.yaml"),
        epochs=100,
        imgsz=640,
        plots=True 
    )

if __name__ == "__main__":
    start_training()