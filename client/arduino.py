import serial
import time

DEV = '/dev/cu.usbmodem1421'
F = 9600

ser = serial.Serial(DEV, F)
time.sleep(2)

def controll(cmd):
    print cmd
    ser.write(cmd)
