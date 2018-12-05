import smbus
from device import I2CDevice
from gyro import Accel
import RPi.GPIO as GPIO
from led import LED
import time
import pygame

if __name__ == "__main__":
	RED_PIN   = 7
	GREEN_PIN = 11
	BLUE_PIN  = 13

	GPIO.setmode(GPIO.BOARD)
	bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
	address = 0x68	   # via i2cdetect
	gy = Accel(bus, address)
	pygame.mixer.init()
	led = LED(RED_PIN, GREEN_PIN, BLUE_PIN)
	led.init()

	try:
		while True:
			x, y, z = gy.get_gyro()
			ax, ay, az = gy.get_accel()
			print("x: %f, y: %f, z: %f | ax: %f, ay: %f, az: %f" % (x, y, z, ax, ay, az))
			time.sleep(1)
			
			# TODO: replace if statement with equivalent of "if sat on"
			if True:
				# play audio
				pygame.mixer.music.load("r2d2.wav")
				pygame.mixer.music.play()
				while pygame.mixer.music.get_busy() == True:
					continue
				
				color1 = (0, 0, 100)
				color2 = (0, 100, 0)
				for r, g, b in LED.gradient(color1, color2, 20):
					led.set_color(r, g, b)
					time.sleep(0.05)
	except KeyboardInterrupt as ex:
		print("Done.")
	finally:
		GPIO.cleanup()
