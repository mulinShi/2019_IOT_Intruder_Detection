import sys
import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
USTRIG = 17
USECHO = 22
BEEP = 23

def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(USTRIG, GPIO.OUT)
    GPIO.setup(USECHO, GPIO.IN)
    GPIO.setup(BEEP, GPIO.OUT, initial=GPIO.LOW)

# def beep():
#     GPIO.output(BEEP, GPIO.HIGH)
#     time.sleep(1)
#     GPIO.output(BEEP, GPIO.LOW)

def distance():
    # 发送高电平信号到 Trig 引脚
    GPIO.output(USTRIG, True)
 
    # 持续 10 us 
    time.sleep(0.00001)
    GPIO.output(USTRIG, False)
 
    start_time = time.time()
    stop_time = time.time()
 
    # 记录发送超声波的时刻1
    while GPIO.input(USECHO) == 0:
        start_time = time.time()
 
    # 记录接收到返回超声波的时刻2
    while GPIO.input(USECHO) == 1:
        stop_time = time.time()
 
    # 计算超声波的往返时间 = 时刻2 - 时刻1
    time_elapsed = stop_time - start_time
    # 声波的速度为 343m/s， 转化为 34300cm/s。
    distance = (time_elapsed * 34300) / 2
 
    return distance

def main():
    
    setup()

    try:
        while True:
            dist = distance()
            print("Measured Distance = {:.2f} cm".format(dist))
            if dist < 99:
                GPIO.output(BEEP, GPIO.HIGH)
            else:
                GPIO.output(BEEP, GPIO.LOW)
            time.sleep(0.5)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
    
if __name__ == '__main__':
    main()


