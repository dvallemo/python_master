import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

flash = int(input("How many times would you like the LED to blink?"))

def blink(flash):
    for i in range(flash):
        time.sleep(.2)
        GPIO.output(11, 0)
        time.sleep(.2)
        GPIO.output(11, 1)
        time.sleep(.2)
        GPIO.output(11, 0)
        print(i + 1)
    GPIO.cleanup()

blink(flash)

#finished 


    

