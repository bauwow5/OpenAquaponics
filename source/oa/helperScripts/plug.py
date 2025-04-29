import requests
import time

def growLamp():
    requests.get('http://10.0.1.2/cm?cmnd=Power%20TOGGLE') # Grow Lamp
    
def waterPump():
    requests.get('http://10.0.1.3/cm?cmnd=Power%20TOGGLE') # Water Pump
    
