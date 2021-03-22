# simple example for mqtt subscriber

import paho.mqtt.client as mqtt
import sys 

memory = {}

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # msg.payload format: (name,temperature)
    info = msg.payload.decode().split(",")
    print("received: " , info)
    if info[0] not in memory:
        memory[info[0]] = float(info[1])
    else:
        del memory[info[0]]
    
    # if house is empty set to 15, otherwise find average
    if len(memory) == 0:
        avg = 15
    else:
        avg = sum(memory.values()) / len(memory)
    print("people in the room: " , list(memory))
    print("average temperature: " , avg)

    

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