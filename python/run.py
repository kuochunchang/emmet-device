import time
import paho.mqtt.client as mqtt
import json

INPUT_GOIO = [10]
OUTPUT_GOIO = [20]
# MQTT_SERVER_ADDRESS = "iot.emmet-project.com"
MQTT_SERVER_ADDRESS = "localhost"
MQTT_SERVER_PORT = 1883
device_id = "device-0001"

current_data = {}

control_topic = "/devices/" + device_id + "/control"
update_topic = "/devices/" + device_id + "/update"
status_topic = "/devices/" + device_id + "/status"


def sendStatus():
    print("--")


def send_heartbeat():
    client.publish("/devices/heartbeat", json.dumps(
        {'deviceId': device_id, 'sequence': sequence, 'timestamp': int(time.time())}))


def on_connect(client, userdata, flags, result_code):
    print("Connected with result code " + str(result_code))
    client.subscribe(control_topic)
    client.subscribe(update_topic)


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    if msg.topic == control_topic:
        sendStatus()


def get_dht11():
    print("DHT11")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER_ADDRESS, MQTT_SERVER_PORT, 60)


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
    client.publish("/devices/heartbeat", json.dumps(
        {'deviceId': device_id, 'sequence': sequence, 'timestamp': int(time.time())}))

    print("Publish heartbeat...")
    time.sleep(1)
    # for key, value in current_data.items():
    #     print("%s: %s" % (key, value))
    #     get_dht11()
    client.loop()
