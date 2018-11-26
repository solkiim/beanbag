#!/usr/bin/python
import smbus
import math
 
# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

class RaspiDevice:

    def __init__(self, bus, address):
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

class Accel(RaspiDevice):

    def __init__(self, bus, address):
        RaspiDevice.__init__(self, bus, address)

    @staticmethod
    def dist(a,b):
        return math.sqrt((a*a)+(b*b))

    @staticmethod
    def get_y_rotation(x,y,z):
        radians = math.atan2(x, Accel.dist(y,z))
        return -math.degrees(radians)

    @staticmethod
    def get_x_rotation(x,y,z):
        radians = math.atan2(y, Accel.dist(x,z))
        return math.degrees(radians)

    @staticmethod
    def get_z_rotation(x,y,z):
        radians = math.atan2(y, Accel.dist(x,y))
        return math.degrees(radians)
    
    def get_gyro(self):
        # Aktivieren, um das Modul ansprechen zu koennen
        self._bus.write_byte_data(self._address, power_mgmt_1, 0)
        # gyroskop_xout = read_word_2c(0x43)
        # gyroskop_yout = read_word_2c(0x45)
        # gyroskop_zout = read_word_2c(0x47)

        ax, ay, az = self.get_accel()
        x_rot = Accel.get_x_rotation(ax, ay, az)
        y_rot = Accel.get_y_rotation(ax, ay, az)
        z_rot = Accel.get_z_rotation(ax, ay, az)

        return x_rot, y_rot, z_rot

    def get_accel(self):
        acceleration_xout = self.read_word_2c(0x3b)
        acceleration_yout = self.read_word_2c(0x3d)
        acceleration_zout = self.read_word_2c(0x3f)

        acceleration_xout_scaled = acceleration_xout / 16384.0
        acceleration_yout_scaled = acceleration_yout / 16384.0
        acceleration_zout_scaled = acceleration_zout / 16384.0
        return acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled


if __name__ == "__main__":
    bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
    address = 0x68       # via i2cdetect

    ac = Accel(bus, address)
    print(ac.get_value())


