import cv2
import numpy as np
import time

class Camera(object):
    def __init__(self):
        print("Constructor for Camera class")

        #Get camera data
        self.cameraData = cv2.VideoCapture(0)
        self.frame_width = int(self.cameraData.get(3))
        self.frame_height = int(self.cameraData.get(4))
        self.fps = self.cameraData.get(cv2.CAP_PROP_FPS)

        print("Frequency:", self.fps, "FPS:", int((1/self.fps)*1000))

        fourcc = cv2.VideoWriter_fourcc(*'MP4V')

        self.outputVideo = cv2.VideoWriter('/home/pi/Documents/Python/CatPie/Outputs/video.mp4', fourcc, self.fps, (self.frame_width, self.frame_height))
        self.start_time = time.time()


    def RecordVideo(self):
        print("Record Video request")

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
        


    def __exit__(self):
        cv2.destroyAllWindows()
        self.cameraData.release()
        self.outputVideo.release()





if __name__ == "__main__":
    print("Camera app test module")

    camera = Camera()
    camera.RecordVideo()