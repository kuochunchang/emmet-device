from device_model import ChannelStatus, DeviceStatus, DeviceHeartbeat
from channel import Channel
import paho.mqtt.client as mqtt
import config
import time


class Device(object):

    _LOOP_SLEEP_SEC = 1

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

    def add_channel(self, channel):
        self._channels.append(channel)

    def run(self):
        print("Device id: %s start!" % (self._device_id))
        while True:
            self._publish_heartbeat()
            for channel in self._channels:
                channel.publish_status()
                
            time.sleep(self._LOOP_SLEEP_SEC)
            self._mqtt_client.loop()

    def _on_mqtt_connect(self, client, userdata, flags, result_code):
        print("MQTT server connected with result code " + str(result_code))
        self._mqtt_client.subscribe(self._control_topic)
        self._mqtt_client.subscribe(self._update_topic)

    def _on_mqtt_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        if msg.topic == self._control_topic:
            self._publish_current_status()

    def _publish(self, topic, msg):
        self._mqtt_client.publish(topic, msg)

    def _current_status(self):
        channel1 = ChannelStatus("A1", 12)
        channel2 = ChannelStatus("A2", 22)
        status = DeviceStatus(self._device_id)
        status.add_channel(channel1)
        status.add_channel(channel2)

        return status

    def _publish_current_status(self):
        print("---", type(self._current_status().json))
        self._publish(self._status_topic, self._current_status().json())

    def _publish_heartbeat(self):
        heartbeat_msg = self._heartbeat.new().json()
        self._publish(self._heartbeat_topic, heartbeat_msg)
        print("Heartbeat published: " + heartbeat_msg)

    def on_channel_status_change(self, msg):
        print("_on_channel_status_change:" + msg)


device = Device("device-0001")
channel = Channel("A10", device.on_channel_status_change, 1)

channel.start()
device.add_channel(channel)
device.run()
