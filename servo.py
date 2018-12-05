import RPi.GPIO as GPIO
import time
from device import PWMDevice

SERVO_PIN = 37

class ServoSet:

    def __init__(self, pins, freq=60):
        self._servos = {p: PWMDevice("servo%d" % i, p, freq=freq)
                        for i,p in enumerate(pins)}

    def init(self):
        for p in self._servos:
            self._servos[p].init()

    def set(self, pin, val):
        self._servos[pin].set(val)


if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    
    servos = ServoSet([SERVO_PIN], freq=60)
    servos.init()
    try:
        for i in range(0, 100):
            servos.set(SERVO_PIN, i)
            time.sleep(0.1)
    finally:
        GPIO.cleanup()
