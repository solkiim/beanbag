# beanbag
cs1951c fall 2018 beanbag final project

## Connecting the Accelerometer

![pi diagram](https://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2a.jpg)

We connected:
- `VCC` to pin 4 (5V). 
- `GND` to pin 6 (Ground)
- `SCL` to pin 5 (GPIO 3)
- `SDA` to pin 3 (GPIO 2)

## After Booting the Pi

Run `sudo raspi-config`. Go to Interfacing Options. Enable
* SSH
* I2C (Protocol needed for the accelerometer)
