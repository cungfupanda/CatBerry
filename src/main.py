'''
Author: cungfupanda
Date: 20/06/2020
Project: Catberry
Revision: 1.0.0
Description: Raspberry Pi project. Distance sensor is continually reading and checking 
for an object to come within 20cm. If a trigger is received it will raise an event to switch 
on the camera and record a 10 second video, which is then uploaded to google drive. If the water 
bowl is empty a pump will be activated to top the bowl up.
'''

#Add packages here
import os
import sys

#Add the project directory to the path and import custom classes
cur_folder = os.path.basename(os.getcwd())
append_path = ""

if cur_folder == "CatBerry":
    append_path = os.getcwd()
elif cur_folder == "src" :
    append_path = os.path.abspath(os.getcwd())
else:
    print("Please set 'append_path' to the base CatBerry folder path")
sys.path.append(append_path)


import packages



if __name__ == "__main__":
    print("CatBerry running")

    dist = packages.Distance()
    while(True):
        flag = dist.Get_Distance()
        print("Flag:", flag)
        if flag:
            break

    base_path = os.getcwd()

    #Record video clip
    cam = packages.Camera(base_path)
    cam.RecordVideo()

    
    #upload
    up = packages.Upload(base_path)
    up.File_Upload()
    

    

