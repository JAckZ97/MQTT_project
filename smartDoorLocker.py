# simple example for mqtt publisher
import paho.mqtt.client as mqtt
import sys 
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection Ok!")
        print("Input message format: name,0 or name,1 ")
        print("Example: John,0 represent John entered room ")
        print("Example: John,1 represent John left room ")
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
    
    # Message format : jack,0
    # jack,0 : jack entered
    # jack,1 : jack left
    client.publish("mqtt/door", input('Who is entered/left: '), 0)

    # Stop loop and disconnect
    client.loop_stop()

client.disconnect()