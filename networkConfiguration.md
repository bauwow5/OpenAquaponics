# Configuring the Network Devices:
1. Determine the IP addresses of the smart plugs in use.
2. In `oa/helperScripts/plug.py`, modify the IP addresses to match the ones for your smart plugs.
3. In `oa/helperScripts/getSensorReadings.py`, modify the IP addresses on lines 31 and 38 to match the grow light and water pump plugs, respectively.
4. In `oa/templates/oa/index.html`, modify the IP address on line 37 to match the IP address from the Motion camera server being run.
