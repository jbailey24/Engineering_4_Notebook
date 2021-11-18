import RPi.GPIO as GPIO
from time import sleep
from gpiozero import LED  #library which lets me define LEDs by using LED command (see lines 6 and 7)
GPIO.setmode(GPIO.BCM)    #sets BCM as numbering scheme

led = LED(21) 	#defines where my LEDs are
led2 = LED(26)

while True:

	led.on() 	#turns red led on and green led off
	led2.off()
	print("Red on, Green off")
	sleep(1)	#waits for one second
	led.off()	#turns green led on and red led off
	led2.on()
	print("Green on, Red off")
	sleep(1)	#waits for one second
