from device_model import *
from channel import Channel
import paho.mqtt.client as mqtt
import config
import time
from dht11_channel import DH11Channel


class Device(object):

    _LOOP_INTERVAL = 5

    def __init__(self, device_id):
        self._device_id = device_id
        self._channels = []
        self._heartbeat_topic = "/devices/heartbeat"
        self._control_topic = "/devices/" + self._device_id + "/control"
        self._update_topic = "/devices/" + self._device_id + "/update"
        self._status_topic = "/devices/" + self._device_id + "/status"
        self._heartbeat = DeviceHeartbeat(self._device_id)

        self._mqtt_client = mqtt.Client()
        self._mqtt_client.on_connect = self._on_mqtt_connect
        self._mqtt_client.on_message = self._on_mqtt_message
        self._mqtt_client.connect(config.MQTT_HOST, config.MQTT_PORT, 60)

    def add_channel(self, channel: Channel):
        self._channels.append(channel)
        channel.set_callback(self.on_channel_status_change)
        channel.start()

    def run(self):
        while True:
            self._publish_heartbeat()
            print("Current status: ", self._current_status().json(), len(self._channels))
            time.sleep(self._LOOP_INTERVAL)
            self._mqtt_client.loop()

    def _on_mqtt_connect(self, client, userdata, flags, result_code):
        print("MQTT server connected with result code " + str(result_code))
        self._mqtt_client.subscribe(self._control_topic)
        self._mqtt_client.subscribe(self._update_topic)

    def _on_mqtt_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        if msg.topic == self._control_topic:
            self._publish_current_status()

    def _mqtt_publish(self, topic, msg):
        self._mqtt_client.publish(topic, msg)
        print("Published message to topic: %s: %s" % (topic, msg))

    def _current_status(self):
        status = DeviceStatus(self._device_id)
        for chl in self._channels:
            status.add_channel(ChannelStatus(chl.name, chl.value))
        return status

    def _publish_current_status(self):
        print("---", type(self._current_status().json))
        self._mqtt_publish(self._status_topic, self._current_status().json())

    def _publish_heartbeat(self):
        heartbeat_msg = self._heartbeat.new().json()
        self._mqtt_publish(self._heartbeat_topic, heartbeat_msg)
        print("Heartbeat published: " + heartbeat_msg)

    def on_channel_status_change(self, msg):
        status = DeviceStatus(self._device_id)
        status.add_channel(ChannelStatus(msg.name, msg.value))
        self._mqtt_publish(self._status_topic, status.json())


