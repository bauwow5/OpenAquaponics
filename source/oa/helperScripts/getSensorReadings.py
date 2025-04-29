import spidev
import sys
import RPi.GPIO as GPIO
import Adafruit_DHT
import requests
import json

spi = spidev.SpiDev()
spi.open(0, 0)  # Ensure SPI0 is used
spi.max_speed_hz = 1000000

class HelperScripts:
    
    def __init__(self):
        print("init")
        

    def getSensorReading(self):
        sensor_array =[]
        sensor_array.append(self.isDraining()) 
        sensor_array.append(self.thermo()) 
        sensor_array.append(self.getTDS())
        sensor_array.append(self.getPH())
        print(sensor_array)
        return sensor_array

    def lightStatus(self):
        request =requests.get('http://10.0.1.2/cm?cmnd=Power')
        jsonRequest =request.json()
        status = jsonRequest.get('POWER')
        return status

    def isDraining(self):
        try:
            request =requests.get('http://10.0.1.3/cm?cmnd=Power')
            jsonRequest =request.json()
            status = jsonRequest.get('POWER')
            if status =="ON":
                return "Filling"
            else:
                return "Draining"
        except:
            return 0
            
    def waterLevel(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        waterLine = (GPIO.input(17) ==GPIO.HIGH)
        return waterLine
        
    def thermo(self):
        try:
            temperature = open("/sys/bus/w1/devices/28-0000103f8d52/temperature","r")
            temp = temperature.read().replace("\n","")
            temperature.close()
            temperature = int(temp)/1000 #conversion to Celcius
            return temperature
        except:
            return 0
            
    def getPH(self):
        try:
            Value = self.readadc(0)
            voltage = (Value * 5.0) / 1023  # Corrected for 5V MCP3008
            phvalue = 7 - (voltage - 1.85) * 3.5  # Adjusted neutral voltage
            phvalue = self.truncate(phvalue,2)
            return phvalue
        except:
            return 0
            
    def readadc(self,adcnum):
        if adcnum < 0 or adcnum > 7:
            return -1
        r = spi.xfer2([1, (8 + adcnum) << 4, 0])
        adcout = ((r[1] & 3) << 8) + r[2]
        return adcout
        # Read pH sensor on Channel 0

    def getTDS(self):
        # Read TDS sensor on Channel 1
        try:
            tds_adc = self.readadc(1)
            tds_voltage = (tds_adc * 5.0) / 1023  # Convert ADC to voltage
            # Convert voltage to TDS (from DFRobot's formula)
            tds_value = (133.42 * tds_voltage**3 - 255.86 * tds_voltage**2 + 857.39 * tds_voltage) * 0.5
            tds_value =self.truncate(tds_value,2) # Truncates the value
            return tds_value
        except:
            return 0
            
    # Helper method to truncate floating point numbers
    def truncate(self,f, n):
        s = '%.12f' % f
        i, p, d = s.partition('.')
        return '.'.join([i, (d+'0'*n)[:n]])
        
