import time
import paho.mqtt.client as mqtt
import json


INPUT_GOIO = [10]
OUTPUT_GOIO = [20]
mqtt_server_address = "iot.emmet-project.com"
mqtt_server_port = 1883
device_id = "device-0001"

current_data = {}

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/devices/device-0001/control")
    client.subscribe("/devices/device-0001/update")


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))



def get_dht11():
    print("DHT11")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_server_address, mqtt_server_port, 60)
time.sleep(3)
# client.loop_forever()

# initial current data
# for i in INPUT_GOIO:
#     current_data[i] = 100
#     print(i, ": ", current_data[i])

# for o in OUTPUT_GOIO:
#     current_data[o] = 200
#     print(o, ": ", current_data[o])

sequence = 0
while True:
    
    sequence += 1    
    client.publish("/devices/heartbeat", json.dumps({'deviceId': device_id, 'sequence': sequence}))
    
    print("Publish heartbeat...")
    time.sleep(1)
    # for key, value in current_data.items():
    #     print("%s: %s" % (key, value))
    #     get_dht11()
    client.loop()