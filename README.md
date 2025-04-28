# OpenAquaponics
An open-source aquaponics project, developed for the Computer Science Interdisciplinary Capstone at Montana State University during the Spring 2025 semester. This project was built for a Raspberry Pi Model 3B+ using Python and the Django framework, with Adobe Dreamweaver utilized for HTML5 web design. Additional tools utilized include the Python Requests library and Motion (for video capture). 

## Features:
- Easily built with off-the-shelf parts (and a whole lot of electrical tape)
- Scalable design with the ability to incorporate more sensors in the future.
- Easy-to-use web interface for system monitoring of grow bed outflow and aquarium temperature, pH, and total dissolved solids (TDS).
- Ability to export system data as CSV for data analysis
- Automatic water pump control via water-level sensor in grow bed.

## Get Started:
1. Download the disk image and flash it to the SD card of your Raspberry Pi.
2. Follow the hardware configuration guides linked here.
3. Connect your Pi to LAN via Ethernet and configure it for your WiFi network, since the image is configured for our test network. Default credentials are `user: oa-user` and `password: password`. We recommend changing these ASAP.
4. Run the startup script `/home/oa-user/openAquaponics/oa/helperScripts/start.sh`.
5. Connect to the web interface in your browser at `http://[pi's local IP]:8000/oa`

## Future Ideas:
Given that the development took place over the course of only one semester, there are some ideas the team did not get to implement. These include:
- Ability to interface with the system remotely over the internet (port-forwarding)
- More environmental sensors, as there are currently none for monitoring the conditions of the grow bed.
- Ability to notify user of issues via web push notifications
- Secondary camera feed for aquarium
- Mobile app for iOS and Android
- System control for autofeeder (the one in use and on the parts list is a battery-operated unit with its own time-delay circuitry that did not look easy to modify for this project)
- Bespoke PCB for ADC and power distribution
- Better grow lamp. The one we used required extensive modifications to bypass the built-in time delay circuitry.
