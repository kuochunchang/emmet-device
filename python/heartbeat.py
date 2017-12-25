from device_model import DeviceHeartbeat
import time

class Heartbeat(object):
    def __init__(self, device_id, device_mqtt_publish):
        self._device_id = device_id
        self._device_mqtt_publish = device_mqtt_publish
        self._heartbeat = DeviceHeartbeat(self._device_id)
   
    def start(self):
        while True:
            heartbeat_msg = self._heartbeat.new().json()
            self._device_mqtt_publish("/devices/heartbeat", heartbeat_msg)
            print("Heartbeat published: " + heartbeat_msg)
            time.sleep(2)

