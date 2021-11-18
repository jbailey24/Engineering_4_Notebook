import RPi.GPIO as GPIO
from time import sleep
from gpiozero import LED
GPIO.setmode(GPIO.BCM)

led = LED(21)
led2 = LED(26)

while True:

	led.on()
	led2.off()
	print("Red on, Green off")
	sleep(1)
	led.off()
	led2.on()
	print("Green on, Red off")
	sleep(1)
