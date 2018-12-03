import smbus
from gyro import Accel
import time
import pygame

if __name__ == "__main__":
	bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
	address = 0x68	   # via i2cdetect
	gy = Accel(bus, address)
	pygame.mixer.init()

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
	except KeyboardInterrupt as ex:
		print("Done.")
