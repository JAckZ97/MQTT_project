# simple example for mqtt subscriber
import paho.mqtt.client as mqtt
import sys 
memory = {}     # Dictionary of people name and preferred temperature
present = []    # Dictionary of people name and their presenting status

# TODO: catch specitial case such input "jack1"

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_message_app(client, userdata, msg):
    # msg.payload format: (name,temperature)
    info = msg.payload.decode().split(",")
    print("received: " , info[0] + " prefer " + info[1] + " degrees. ")
    memory[info[0]] = float(info[1])


def on_message_door(client, userdata, msg):
    # msg.payload format: (name,present_status)
    info = msg.payload.decode().split(",")
    print("received: " , info[0] + " with status of " + info[1])

    # Check present list
    # People enter the room
    if info[1] == "0":
        present.append(info[0])
    # People leave the room
    elif info[1] == "1":
        present.remove(info[0])
    else:
        pass

    totalTemp = 0.0
    for x in present:
        if x in memory:
            totalTemp += memory[x]
        else:
            pass

    # If house is empty set to 15, otherwise find average
    if len(present) == 0:
        avg = 15
    else:
        avg = totalTemp / len(present)

    print("people in the room: " , present)
    print("average temperature: " , avg)


client = mqtt.Client()

client.message_callback_add("mqtt/app", on_message_app)
client.message_callback_add("mqtt/door", on_message_door)
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.subscribe("mqtt/#", 0)

client.loop_forever()
client.disconnect()