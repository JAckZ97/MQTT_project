# MQTT_project
## COEN446 project

### Paho-mqtt client
Role: publisher & subscriber  
Source: https://pypi.org/project/paho-mqtt/#id3

### Mosquitto broker
Role: broker  
Source: https://github.com/eclipse/mosquitto  
Windows download: https://mosquitto.org/download/

## Instruction for running on Linux
1. Clone the repo
2. Make sure you have python3 and pip3 installed
3. pip install requirement library
```
pip install paho-mqtt
pip install pyyaml
```
4. install Mosquitto MQTT Broker by following the instrution: 
```
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa	
sudo apt-get update
sudo apt-get install mosquitto
```
And start the broker by following instruction:
```
sudo /etc/init.d/mosquitto start
sudo /etc/init.d/mosquitto status   # Check broker status
sudo /etc/init.d/mosquitto stop     # Stop broker
```
More detail refer to: https://howtoprogram.xyz/2016/10/15/install-mosquitto-mqtt-broker-ubuntu-16-04-lts-xenial-xerus/  

(Option for Window user)  
- Download Mosquitto broker by: https://mosquitto.org/files/binary/win64/mosquitto-2.0.10-install-windows-x64.exe
- Installed in one fold and go to the folder
- Start mosquitto broker by "mosquitto -v"

5. Change config file for mosquitto by
```
sudo nano /etc/mosquitto/mosquitto.conf
```
Make the change into following format: 
```
persistence true
persistence_location /var/lib/mosquitto/
log_dest file /var/log/mosquitto/mosquitto.log
log_dest stdout
log_dest topic
# log_type all  # debug mode
log_type error
log_type warning
log_type notice
log_type information
include_dir /etc/mosquitto/conf.d
```
6. Open the log file in default location at (Linux):
```
/var/log/mosquitto/mosquitto.log
```
Open it by:
```
sudo gedit /var/log/mosquitto/mosquitto.log
```
7. Start the programs in following order:
```
python3 thermostat.py
python3 managementApp.py
python3 smartDoorLocker.py
```