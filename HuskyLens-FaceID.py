import RPi.GPIO as GPIO
import math
import serial
import sys
from time import sleep
import time
import threading
ctrlpin = 5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ctrlpin, GPIO.OUT)
gs90_pwm = GPIO.PWM(ctrlpin, 50)
gs90_pwm.start(0)
gs90_pwm.ChangeDutyCycle(12.5)
sleep(0.1)
gs90_pwm.stop()
ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=2)
ID = 30
Number = 8
face_number = 0
x = 0
yes_no = 0
print("serial test start ...")
data_position = 0
Current_face = 0
over = 1
code = 0
i = 7.5

def motor_close():
    gs90_pwm = GPIO.PWM(ctrlpin, 50)
    gs90_pwm.start(0)
    gs90_pwm.ChangeDutyCycle(12)
    sleep(0.5)
    gs90_pwm.stop()

def motor_open():
    gs90_pwm = GPIO.PWM(ctrlpin, 50)
    gs90_pwm.start(0)
    gs90_pwm.ChangeDutyCycle(7.5)
    sleep(0.5)
    gs90_pwm.stop()


while True:
    data_all = []
    i = 0
    while ser.inWaiting() > 0:
        str_n = ser.read()
        str_y = str(str_n.hex())
        if data_position == 0 and str_y != '55':
            continue
        ser.write(str_n)
        data_all.append(str_y)
        data_position += 1
        i += 1
        if data_position == 6:
            try:
                x = int(str_y[0]) * 10 + int(str_y[1])
            except:
                print("data error1")
            if x > 0:
                yes_no = x
                print("This time %d individuals were face" % yes_no)
            else:
                yes_no = 0
                print("No face was recognized.")
        if (data_position == 16 and yes_no == 0) or (data_position == 31 + (yes_no - 1) * 16 and yes_no != 0):
            break
    if yes_no > 0:
        for i in range(0, 16 + yes_no * 16 - 1, 1):
            if i == Number - 1:
                try:
                    x = int(data_all[i][0]) * 10 + int(data_all[i][1])
                except:
                    print("data error2")
                face_number = x
                print("Currently %d face data has been saved." % x)
            if i == ID + Current_face * 16 - 1:
                try:
                    x = int(data_all[i][0]) * 10 + int(data_all[i][1])
                except:
                    print("data error3")
                    print("Identify the face with ID %d" % x)
                if x == 1:
                    motor_open()
                    timer = threading.Timer(5.0, motor_close)
                    timer.start()

    sleep(0.1)
    data_position = 0
    Current_face = 0
    yes_no = 0
    ser.write([0x55, 0xaa, 0x11, 0x00, 0x24, 0x34])


        
