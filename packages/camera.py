import os
import cv2
import numpy as np
import time
import threading

class Camera(threading.Thread):
    def __init__(self, event_dist, event_upload,  proj_dir):
        print("Constructor for Camera class")
        self.event_dist = event_dist
        self.event_upload = event_upload

        #Get camera data
        self.cameraData = cv2.VideoCapture(0)
        self.frame_width = int(self.cameraData.get(3))
        self.frame_height = int(self.cameraData.get(4))
        self.fps = self.cameraData.get(cv2.CAP_PROP_FPS)
        self.output_dir = os.path.join(proj_dir, 'outputs')

        print("Frequency:", self.fps, "FPS:", int((1/self.fps)*1000))

        fourcc = cv2.VideoWriter_fourcc(*'XVID')

        record_path = os.path.join(self.output_dir, 'video.avi')
        print(record_path)

        self.outputVideo = cv2.VideoWriter(record_path, fourcc, self.fps, (self.frame_width, self.frame_height))
        self.start_time = time.time()


    def RecordVideo(self):
        print("Record Video request")

        self.event_dist.wait()


        if not self.cameraData.isOpened():
            print("Error opening video stream")
            return

        while(True):
            current_time = time.time()
            if((current_time - self.start_time) > 10):
                break
            ret, frame = self.cameraData.read()
            self.outputVideo.write(frame)
            cv2.imshow("Capture", frame)
            cv2.waitKey(int((1/self.fps)*1000))

        self.event_dist.clear()
        


    def __exit__(self):
        cv2.destroyAllWindows()
        self.cameraData.release()
        self.outputVideo.release()





if __name__ == "__main__":
    print("Camera app test module")

    camera = Camera('/home/pi/Documents/Python/CatBerry')
    camera.RecordVideo()