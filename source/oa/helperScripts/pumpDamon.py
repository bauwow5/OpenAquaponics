import requests
import time
from getSensorReadings import HelperScripts
from plug import  waterPump, growLamp
def main():
    helper = HelperScripts() 
    while True:

        if(helper.waterLevel()):
            time.sleep(15)
            waterPump()
            time.sleep(180)
            waterPump()    
main()

