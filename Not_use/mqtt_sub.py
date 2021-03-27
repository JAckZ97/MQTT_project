# simple example for mqtt subscriber

import paho.mqtt.client as mqtt
import sys 

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()

# Bind call back function
client.on_message = on_message

if client.connect("localhost", 1883, 60) != 0:
    print("Not able to connect to MQTT broker.")
    sys.exit(-1)
else: 
    print("Connecting to the broker: localhost")

client.subscribe("test/status")

client.loop_forever()

client.disconnect()