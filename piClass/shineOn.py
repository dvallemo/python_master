import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, 0) # resets I2C pull up 

flash = int(input("How many times would you like the LED to blink? "))
pin = int(input("Which pin? "))

def blink(flash, pin):
    
    for i in range(flash):
        if pin == 13:
            time.sleep(.2)
            GPIO.output(13, 0)
            time.sleep(.2)
            GPIO.output(13, 1)
            time.sleep(.2)
            GPIO.output(13, 0)
        elif pin == 3:
            time.sleep(0.2)
            GPIO.output(3, 0)
            time.sleep(.2)
            GPIO.output(3, 1)
            time.sleep(.2)
            GPIO.output(3, 0)
        print(i+1)

blink(flash, pin)


    

