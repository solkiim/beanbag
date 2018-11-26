import smbus
from gyro import Accel
import time

if __name__ == "__main__":
    bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
    address = 0x68       # via i2cdetect
    ac = Accel(bus, address)

    try:
        while True:
            x, y = ac.get_value()
            print("x: %f, y: %f" % (x, y))
            time.sleep(1)
    except KeyboardInterrupt as ex:
        print("Done.")
