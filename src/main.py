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
import sys

#Add the project directory to the path and import custom classes
sys.path.append("CatBerry")
from packages import *



if __name__ == "__main__":
    print("CatBerry running")