# simple example for mqtt subscriber
import paho.mqtt.client as mqtt
import sys 
memory = {}     # Dictionary of people name and preferred temperature
present = []    # List of people name and their presenting status

# XXX: Condition:
#      If re-enter the same name with different temperature, it will update the memory (Edit).

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_message_app(client, userdata, msg):
    try:
        # msg.payload format: (name,temperature)
        info = msg.payload.decode().split(",")
        print("received: " , info[0] + " prefer " + info[1] + " degrees. ")
        memory[info[0]] = float(info[1])

    except Exception as e: 
        print(e)


def on_message_door(client, userdata, msg):
    try:
        # msg.payload format: (name,present_status)
        info = msg.payload.decode().split(",")
        print("received: " , info[0] + " with status of " + info[1])

        # Check present list
        if checkNameInPresent(info[0]):
            if info[1] == "1":
                present.remove(info[0])
            else:
                pass
        else:
            # People enter the room
            if info[1] == "0":
                if checkNameInApp(info[0]):
                    present.append(info[0])
                else:
                    print(info[0] + " has no temperature record.")
            # People leave the room
            elif info[1] == "1":
                print(info[0] + " is not in the room.")
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
    
    except Exception as e: 
        print(e)

# Check if we have the name in memory dictionary       
def checkNameInApp(name):
    if name in memory:
        return True
    else:
        return False

# Check if we have the name in present list       
def checkNameInPresent(name):
    if name in present:
        return True
    else:
        return False

client = mqtt.Client()

client.message_callback_add("mqtt/app", on_message_app)
client.message_callback_add("mqtt/door", on_message_door)
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.subscribe("mqtt/#", 0)

client.loop_forever()
client.disconnect()