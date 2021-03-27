# simple example for mqtt publisher
import paho.mqtt.client as mqtt
import sys 
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection Ok!")
        print("Input message format: name,temperature ")
        print("Example: John,25.3 ")
    else: 
        print("Bad connected with result code "+str(rc))

# Construtor
client = mqtt.Client()

# Bind call back function
client.on_connect = on_connect
if client.connect("localhost", 1883, 60) != 0:
    print("Not able to connect to MQTT broker.")
    sys.exit(-1)
else: 
    print("Connecting to the broker: localhost")

while True:
    # Start loop 
    client.loop_start()
    time.sleep(1)
    
    # Message format : jack,23
    client.publish("mqtt/app", input('Message : '), 0)

    # Stop loop and disconnect
    client.loop_stop()

client.disconnect()
