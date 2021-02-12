import RPi.GPIO as GPIO
import time

# GPIO.BOARD:=物理ピン番号、GPIO.BCM:=役割ピン番号
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

while True:
    # HIGHは点灯
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(4, GPIO.HIGH)

    time.sleep(0.5)

    # LOWは消灯
    GPIO.output(2, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)

    time.sleep(0.5)