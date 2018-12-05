import RPi.GPIO as GPIO

class RaspiDevice:

    def __init__(self, name):
        self._name = name

    
class I2CDevice(RaspiDevice):

    def __init__(self, bus, address):
        RaspiDevice.__init__(self, "I2C")
        self._bus = bus
        self._address = address

    def read_byte(self, reg):
        return self._bus.read_byte_data(self._address, reg)
 
    def read_word(self, reg):
        h = self._bus.read_byte_data(self._address, reg)
        l = self._bus.read_byte_data(self._address, reg+1)
        value = (h << 8) + l
        return value
 
    def read_word_2c(self, reg):
        val = self.read_word(reg)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val


class PWMDevice(RaspiDevice):

    def __init__(self, name, pin, freq=60):
        self._name = name
        self._pin = pin
        self._freq = freq
        self._pwm = None

    def __del__(self):
        if self._pwm is not None:
            self._pwm.stop()

    def init(self):
        GPIO.setup(self._pin, GPIO.OUT)
        self._pwm = GPIO.PWM(self._pin, self._freq)
        
        print("Starting %s PWM pins..." % self._name)
        self._pwm.start(0)

    def set(self, val):
        self._pwm.ChangeDutyCycle(val)

    @property
    def pin(self):
        return self._pin
    
