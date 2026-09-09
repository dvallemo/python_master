import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
time.sleep(0.2)
GPIO.output(3, 0)
GPIO.output(3, 1)
time.sleep(0.2)
GPIO.output(3, 0)


