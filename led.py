import RPi.GPIO as GPIO
import time

RED_PIN   = 7
GREEN_PIN = 11
BLUE_PIN  = 13

class LED:

    def __init__(self, rpin, gpin, bpin, freq=60):
        self._rpin = rpin
        self._gpin = gpin
        self._bpin = bpin
        self._rpwm = None
        self._gpwm = None
        self._bpwm = None
        self._freq = freq

    def __del__(self):
        print("I am called!")
        if self._rpwm is not None:
            self._rpwm.stop()
        if self._gpwm is not None:
            self._gpwm.stop()
        if self._bpwm is not None:
            self._bpwm.stop()

    def init(self):
        GPIO.setup(self._rpin, GPIO.OUT)
        GPIO.setup(self._gpin, GPIO.OUT)
        GPIO.setup(self._bpin, GPIO.OUT)
        self._rpwm = GPIO.PWM(self._rpin, self._freq)
        self._gpwm = GPIO.PWM(self._gpin, self._freq)
        self._bpwm = GPIO.PWM(self._bpin, self._freq)

        print("Starting RGB PWM pins...")
        self._rpwm.start(0)
        self._gpwm.start(0)
        self._bpwm.start(0)


    def set_color(self, r, g, b):
        """r, g, b values range from 0.0 to 100.0"""
        self._rpwm.ChangeDutyCycle(r)
        self._gpwm.ChangeDutyCycle(g)
        self._bpwm.ChangeDutyCycle(b)
        

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    
    led = LED(RED_PIN, GREEN_PIN, BLUE_PIN)
    led.init()
    try:
        while True:
            print("Color 1")
            led.set_color(50, 100, 100)
            time.sleep(1)
            print("Color 2")
            led.set_color(100, 50, 20)
            time.sleep(1)
    finally:
        GPIO.cleanup()
