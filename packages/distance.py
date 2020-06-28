import RPi.GPIO as GPIO
import time

class Distance(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.TRIG = 23
        self.ECHO = 24
        self.EVENT = 25

        GPIO.setup(self.EVENT, GPIO.OUT)
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

    def Triggered(self):
        #Event on occurance of a trigger
        GPIO.output(self.EVENT, GPIO.HIGH)
        time.sleep(5)
        

    def Get_Distance(self):
        #Set an initial trigger variable off
        trigger_var = 0

        GPIO.output(self.EVENT, GPIO.LOW)
        GPIO.output(self.TRIG, False)
        print("Waiting for sensor to settle")
        time.sleep(2)

        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

        while GPIO.input(self.ECHO)==0:
            pulse_start = time.time()

        while GPIO.input(self.ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        
        if distance < 20:
            self.Triggered()
            trigger_var = 1
        print("Distance:", distance, "cm")
        return trigger_var

    def __exit__(self):
        GPIO.cleanup()
    



if __name__ == "__main__":
    print("Distance tect app")
    #main()
    trigger = 0

    meas_dist = Distance()
    while(True):
        trigger = meas_dist.Get_Distance()

    