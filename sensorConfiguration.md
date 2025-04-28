# Sensor Configuration:
See the following guides below for connecting the sensors to the Pi, as well as our notes.
- (DFRobot pH Meter and TDS Sensor)[https://forums.raspberrypi.com/viewtopic.php?t=252146]: Use 5V for MCP3008 power, not 3.3V. Connect the pH sensor data to input 1 of the MCP3008, TDS to input 2.
- (DFRobot Water Level Sensor)[https://forums.raspberrypi.com/viewtopic.php?t=186786]: Find where your bell siphon starts draining, and set the sensor at that level. For us, it was just below the indent on the bin we used. We used pin 11 on the Pi for its input.
- (DS18B20 Temp Sensor)[https://forums.raspberrypi.com/viewtopic.php?t=343876]: Don't accidentally connect the main voltage line to 5V. Bad things happen. Soldering may be required.
You may run out of voltage and ground pins on your Pi. We recommend using a breadboard to distribute 5V, 3.3V, and GND, to avoid running out of GPIO space.
