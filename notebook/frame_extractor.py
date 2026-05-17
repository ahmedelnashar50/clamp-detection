import cv2
import os

def extract_distinct_frames(video_path, output_dir, total_frames=30):
   
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video. Check the file path.")
        return

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
 
    interval = max(1, frame_count // total_frames)
    
    saved_count = 0
    for i in range(total_frames):
        frame_id = i * interval
        if frame_id >= frame_count:
            break
            
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
        success, frame = cap.read()
        
        if success:
 
            frame_name = f"clamp_frame_{saved_count:03d}.jpg"
            file_path = os.path.join(output_dir, frame_name)
            cv2.imwrite(file_path, frame)
            saved_count += 1
            
    cap.release()
    print(f"Done! Successfully extracted {saved_count} frames to: {output_dir}")

if __name__ == "__main__":
    VIDEO_SOURCE = "Task.mp4" 
    OUTPUT_FOLDER = "raw_frames"
    
    extract_distinct_frames(VIDEO_SOURCE, OUTPUT_FOLDER)