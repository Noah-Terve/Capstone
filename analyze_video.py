import numpy as np
import cv2
import os
from ultralytics import YOLO
from PIL import Image
from datetime import datetime as dt

def analyze_video(save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        start = dt.now()
    input_video_path = input("Enter path to video to process: ")
    
    start = dt.now()
    fileName_prefix = save_dir + start.strftime("%Y_%m_%d-%I_%M_%S_%p")
    result_filename = fileName_prefix +'.mp4'
    
    cap = cv2.VideoCapture(input_video_path)
    size = (int(cap.get(3)) ,int(cap.get(4))) 
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(result_filename, fourcc, 30.0, size)
    model = YOLO('model.pt')

    
    while True: 
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            result = model(frame)
            for r in result:
                im_array = r.plot()
                im = Image.fromarray(im_array[..., ::-1])
                out.write(np.uint8(im))
        else:
            break
    

def main():
    save_dir='./output/'
    analyze_video(save_dir)

if __name__ == "__main__":
    main()