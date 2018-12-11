#!/usr/bin/python

from LIS3DH import LIS3DH
from time import sleep


if __name__ == '__main__':
    sensor = LIS3DH(debug=True)
    sensor.setRange(LIS3DH.RANGE_2G)

    # second accelerometer
    # s2 = LIS3DH(address=0x19, debug=True)

    print("Starting stream")
    while True:

        x = sensor.getX()
        y = sensor.getY()
        z = sensor.getZ()

        # raw values
        print("\rX: %.6f\tY: %.6f\tZ: %.6f" % (x, y, z))
        sleep(0.1)

    # click sensor if polling & not using interrupt
    #        click = sensor.getClick()
    #        if (click & 0x30) :
    #            print "Click detected (0x%2X)" % (click)
    #            if (click & 0x10): print " single click"
#            if (click & 0x20): print " double click"
