# OpenAquaponics
An open-source aquaponics project, developed for the Computer Science Interdisciplinary Capstone at Montana State University during the Spring 2025 semester. This project was built for a Raspberry Pi Model 3B+ using Python and the Django framework, with Adobe Dreamweaver utilized for HTML5 web design. Additional tools utilized include the Python Requests library and Motion (for video capture). 

## Our Implementation:
![The OpenAquaponics prototype on display](/demoImage.jpg)

## System Diagram:
![System diagram](/Capstone%20-%20Prototype%20System%20Diagram.png)

## Features:
- Easily built with [off-the-shelf parts](/Parts%20List.md) (and a whole lot of electrical tape)
- Scalable design with the ability to incorporate more sensors in the future.
- Easy-to-use web interface for system monitoring of grow bed outflow and aquarium temperature, pH, and total dissolved solids (TDS).
- Ability to export system data as CSV for data analysis
- Automatic water pump control via water-level sensor in grow bed.

## Get Started:
1. Download the source code onto your Raspberry Pi.
2. [Configure the smart plugs for your network](https://tasmota.github.io/docs/).
3. Install [Motion](https://github.com/Motion-Project/motion) and [Django](https://www.djangoproject.com/).
4. Follow the sensor configuration guides linked [here](/sensorConfiguration.md).
5. [Adjust the IPs used in the scripts for the smart plugs and Motion](/networkConfiguration.md). They will not be the same as ours, and are hardcoded in since they rely on HTTP requests for control.
6. Run the startup script located at `/oa/helperScripts/start.sh`.
7. Connect to the web interface in your browser at `http://[pi's local IP]:8000/oa`

## Future Ideas:
Given that the development took place over the course of only one semester, there are some ideas the team did not get to implement. These include:
- Ability to interface with the system remotely over the internet (port-forwarding)
- More environmental sensors, as there are currently none for monitoring the conditions of the grow bed.
- Ability to notify user of issues via web push notifications
- Secondary camera feed for aquarium
- Mobile app for iOS and/or Android
- System control for autofeeder (the one in use and on the parts list is a battery-operated unit with its own time-delay circuitry that did not look easy to modify for this project)
- Bespoke PCB for ADC and power distribution
- Better grow lamp. The one we used required extensive modifications to bypass the built-in time delay circuitry.
