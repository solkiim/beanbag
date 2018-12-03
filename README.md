# beanbag
cs1951c fall 2018 beanbag final project

### After Booting the Pi

Run `sudo raspi-config`. Go to Interfacing Options. Enable
* SSH
* I2C (Protocol needed for the accelerometer)

### Checking Pin Connections
```
sudo id2cdetect -y 1
```
The default (with nothing plugged in) looks like:
```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- -- 
```
If we connect the accelerometer as described above, we should see
```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- 68 -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --
```
### Connecting the Accelerometer


We connected:
- `VCC` to pin 4 (5V). 
- `GND` to pin 6 (Ground)
- `SCL` to pin 5 (GPIO 3)
- `SDA` to pin 3 (GPIO 2)

<img src="https://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2a.jpg" width="700">

### Connecting the LED Strip

Refer to this diagram. Use NPN Transistors (TIP31A).
<img src="https://i.imgur.com/P6dIJH4.png" width="600">
