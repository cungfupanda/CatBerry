author: cungfupanda


Description:
Raspberry Pi based project to monitor the presence of an animal. 
If the ultrasonic sensor is triggered it will activate the raspberry pi camera and record a 10 second video clip. This clip will then be uploaded to google drive.
Image processing will be carried out on the capture and if it detects the water bowl is low it will activate a pump that will top up the bowl.

Code Structure:
src - contains the main executable script
packages - contains all the idivisual classes
data - any input data used in test, including configs
outputs - any output data written dynamically. Used as temp folder for video, deleted once uploaded to google drive
libs - any c/c++ libraries

Hardware:
Raspberry Pi 2 Model B
Raspberry Pi camera v1.2
HC-SR04 Ultrasonic sensor
DC water pump 5V 100L/H


