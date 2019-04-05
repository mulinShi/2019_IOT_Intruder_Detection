import socket
import os
import sys
import struct

import RPi.GPIO as GPIO
import time

BEEP = 23
SERVER_IP = "35.244.107.42"

def alarm():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(BEEP, GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(BEEP, GPIO.HIGH)
    time.sleep(300)
    GPIO.output(BEEP, GPIO.LOW)

def socket_client_image():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER_IP, 6666))  
        # s.connect(('127.0.0.1', 6666))  
    except socket.error as msg:
        print(msg)
        print(sys.exit(1))
    filepath = "output.jpg"   # input filepath
    fhead = struct.pack(b'128sq', bytes(os.path.basename(filepath), encoding='utf-8'), os.stat(filepath).st_size)  # package image file by 128sq format
    s.send(fhead)

    fp = open(filepath, 'rb')  
    while True:
        data = fp.read(1024) # read binary data
        if not data:
            print('{0} send over...'.format(filepath))
            break
        s.send(data)  

    signal = s.recv(32).decode()
    if signal == "1":
        print("Received signal! Start alarm!")
        alarm()
    s.close()
    
if __name__ == '__main__':
    socket_client_image()

