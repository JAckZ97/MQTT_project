import paho.mqtt.client as mqtt
from database import DatabaseController
import sys
import time
import threading

db = DatabaseController()
temp_data = " "
temp_data_old = " "

# Construtor
client = mqtt.Client()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection Ok!")
        print("Temperature range is 15.0 to 35.0 degrees ")
        print("Input message format: name,temperature ")
        print("Example: John,25.3 ")
    else: 
        print("Bad connected with result code "+str(rc))


def on_message_door(client, userdata, msg):
    try:
        # msg.payload format: (name,present_status)
        info = msg.payload.decode().split(",")

        # Check if enter command, then check database
        if info[1] == "0":
            if db.checkExistUser(info[0]):
                global temp_data
                new_temp = db.readNamedTemperature(info[0])
                temp_data = info[0] + "," + str(new_temp)
            else:
                temp_data = info[0] + ",not"
        else:
            pass

    except Exception as e: 
        print(e)


def storeInDatabase(name, temperature):
    db.addUser(name,temperature)


def publishToDB():
    while True:
        time.sleep(1)
        
        # Message format : John,25.3
        info = input('Message : ')
        infoSplit = info.split(",")

        try:
            # Assume perfered temperature is in the range of 15 to 35 degrees
            if float(infoSplit[1]) >= 15 and float(infoSplit[1]) <= 35:
                storeInDatabase(infoSplit[0], float(infoSplit[1]))
                client.publish("mqtt_db/database", info, 0)
            else:
                print("Please choose proper temperature range. ")
        
        except Exception as e: 
            print(e)


def subscribeToDoorLock():
    # Subscribe doorLocker topic
    client.subscribe("mqtt/door", 0)
    client.on_message = on_message_door


def publishToThermo():
    global temp_data_old
    while True:
        time.sleep(1)

        if temp_data_old != temp_data:
            # Publish the userName with the person entered
            client.publish("mqtt/app", temp_data, 0)
            temp_data_old = temp_data
        else:
            pass


# Bind call back function
client.on_connect = on_connect
if client.connect("localhost", 1883, 60) != 0:
    print("Not able to connect to MQTT broker.")
    sys.exit(-1)
else: 
    print("Connecting to the broker: localhost")

x = threading.Thread(target=publishToDB)
x.start()
y = threading.Thread(target=subscribeToDoorLock)
y.start()
z = threading.Thread(target=publishToThermo)
z.start()

client.loop_forever()

x.join()
y.join()
z.join()

client.disconnect()
