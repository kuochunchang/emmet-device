from device_model import DeviceHeartbeat
import time
import threading

class Heartbeat(threading.Thread):
    def __init__(self, device_id, device_mqtt_publish):
        threading.Thread.__init__(self)
        self._device_id = device_id
        self._device_mqtt_publish = device_mqtt_publish
        self._heartbeat = DeviceHeartbeat(self._device_id)
   
    def run(self):
        while True:
            heartbeat_msg = self._heartbeat.new().json()
            self._device_mqtt_publish("/devices/heartbeat", heartbeat_msg)
            print("Heartbeat published: " + heartbeat_msg)
            time.sleep(2)
            

