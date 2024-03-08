import numpy as np
import cv2
from flirpy.camera.boson import Boson
from datetime import datetime as dt
import csv
import os
import sys
# import matplotlib.pyplot as plt
import winsound
from win32com.client import Dispatch
import shutil


def check_memory():

    total, used, free = shutil.disk_usage("/")
    print("\nTotal memory in system: %d GiB" % (total // (2**30)))
    print("Used memory in system: %d GiB" % (used // (2**30)))
    print("Free memory in system: %d GiB \n" % (free // (2**30)))
    
    if ( (free // (2**30)) < 100 ):
        speak = Dispatch("SAPI.SpVoice").Speak
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 700  # Set Duration To 1000 ms == 1 second
    
        for i in range (5):
            winsound.Beep(frequency, duration)
        speak("Low memory")
        print("\nSystem memory is very low:  %d GiB" % (free // (2**30)))
        for i in range (3):
            winsound.Beep(frequency, duration)   
        sys.exit()
        

# TODO: this will have to change as now we don't want to save to a dir, just
# throw it to the external port which will eventually be a python container
def capture_video_boson(save_dir, show):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    device_index = Boson.find_video_device()
    count=1
    cap = cv2.VideoCapture(device_index)  
    size = (int(cap.get(3)) ,int(cap.get(4))) 
    fourcc =  cv2.VideoWriter_fourcc('I','4','2','0')
    start = dt.now()
    fileName_prefix = save_dir + start.strftime("%Y_%m_%d-%I_%M_%S_%p")
    thermal_filename = fileName_prefix +'.avi'
    csv_filename = fileName_prefix +'.csv'
    out = cv2.VideoWriter(thermal_filename,fourcc, 30.0, size)
    print("Press Ctrl-C to terminate while statement")
    
    with open (csv_filename, "a", newline="") as csvfile:
        writer =  csv.writer(csvfile)
        try:

            # while (dt.now() - start).seconds < 610: 
            while True: 

                ret, frame = cap.read()
                if ret==True:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                    out.write(np.uint8(frame))
                    writer.writerow([count, dt.now().timestamp()])
                    count+= 1
                    if show:
                        cv2.imshow('frame',frame.astype(np.uint8))
                        # plt.imshow(frame.astype(np.uint8))
                        # plt.show()
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                else:
                    break
        except KeyboardInterrupt:
            pass

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def main():
    save_dir='./output/'
    check_memory()
    capture_video_boson(save_dir , show=True)

if __name__ == "__main__":
    main()
