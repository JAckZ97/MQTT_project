# MQTT_project
COEN446 project

### Paho-mqtt client
Role: publisher & subscriber  
Source: https://pypi.org/project/paho-mqtt/#id3

### Mosquitto broker
Role: broker  
Source: https://github.com/eclipse/mosquitto  
Download: https://mosquitto.org/download/

### pip intstall list
```
pip install paho-mqtt
```

### Instruction for running on Linux
1. Clone the repo
2. Make sure you have python3 and pip3 installed
3. pip install paho-mqtt
4. install Mosquitto MQTT Broker by following the instrution: https://howtoprogram.xyz/2016/10/15/install-mosquitto-mqtt-broker-ubuntu-16-04-lts-xenial-xerus/
```
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa	
sudo apt-get update
sudo apt-get install mosquitto
```
5. Change config file for mosquitto by
```
sudo nano /etc/mosquitto/mosquitto.conf
```
with formate of 
```
persistence true
persistence_location /var/lib/mosquitto/
log_dest file /var/log/mosquitto/mosquitto.log
log_dest stdout
log_dest topic
# log_type all  # debug
log_type error
log_type warning
log_type notice
log_type information
include_dir /etc/mosquitto/conf.d
```
6. Run the program
```
python3 thermostat.py
python3 managementApp.py
python3 smartDoorLocker.py
```