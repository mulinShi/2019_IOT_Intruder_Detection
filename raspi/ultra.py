import os
import sys
import time
import RPi.GPIO as GPIO

import client
import _thread

USTRIG = 17
USECHO = 22

def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(USTRIG, GPIO.OUT)
    GPIO.setup(USECHO, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(USTRIG, True)
 
    # set Trigger after 10us to LOW 
    time.sleep(0.00001)
    GPIO.output(USTRIG, False)
 
    start_time = time.time()
    stop_time = time.time()
 
    # save StartTime
    while GPIO.input(USECHO) == 0:
        start_time = time.time()
 
    # save arrival time
    while GPIO.input(USECHO) == 1:
        stop_time = time.time()
 
    # time difference between start and arrival
    time_elapsed = stop_time - start_time
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (time_elapsed * 34300) / 2
 
    return distance

if __name__ == '__main__':
    setup()
    try:
        while True:
            dist = distance()
            print("Measured Distance = {:.2f} cm".format(dist))
            if dist < 160:
                os.system("wget http://127.0.0.1:8080/?action=snapshot -O output.jpg")
                _thread.start_new_thread(client.socket_client_image,())
                time.sleep(3)

            time.sleep(0.5)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()


