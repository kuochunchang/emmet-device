from channel import Channel
from dht11 import dht11
import time
import RPi.GPIO as GPIO

class DH11Channel(Channel):

    def _checking_loop(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()
        instance = dht11.DHT11(pin=26)
     
        last_value = None
        while True:
            result = instance.read()
            if result.is_valid():
                self.value = str(result.temperature) + "," + str(result.humidity)
                if(last_value != self.value):
                  self._publish_status() 
                  last_value = self.value
    
            time.sleep(self._check_interval)
