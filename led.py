import RPi.GPIO as GPIO
import time
from device import PWMDevice

RED_PIN   = 7
GREEN_PIN = 11
BLUE_PIN  = 13
SERVO_PIN = 37

class LED:

    def __init__(self, rpin, gpin, bpin, freq=60):
        self._rpwm = PWMDevice("R", rpin, freq=freq)
        self._gpwm = PWMDevice("G", gpin, freq=freq)
        self._bpwm = PWMDevice("B", bpin, freq=freq)
        self._current_color = None

    def init(self):
        self._rpwm.init()
        self._gpwm.init()
        self._bpwm.init()

    def set_color(self, r, g, b):
        """r, g, b values range from 0.0 to 100.0"""
        self._rpwm.set(r)
        self._gpwm.set(g)
        self._bpwm.set(b)
        self._current_color = (r, g, b)

    @classmethod
    def gradient(cls, color1, color2, n=10):
        """Returns an array of tuples which are the linear gradients
        to change from color1 to color2. The gradient will take n steps."""
        colors = [color1]
        for t in range(1, n):
            colors.append(tuple(
                color1[i] + float(t)/(n-1)*(color2[i] - color1[i])
                for i in range(3)
            ))
        return colors
        

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    
    led = LED(RED_PIN, GREEN_PIN, BLUE_PIN)
    led.init()
    try:
        color1 = (0, 0, 100)
        color2 = (50, 100, 0)
        for r, g, b in LED.gradient(color1, color2, 10):
            led.set_color(r, g, b)
            time.sleep(0.05)
    finally:
        GPIO.cleanup()
