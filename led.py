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
        self._current_color = None

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
        color2 = (0, 100, 0)
        for r, g, b in LED.gradient(color1, color2, 20):
            led.set_color(r, g, b)
            time.sleep(0.05)
    finally:
        GPIO.cleanup()
