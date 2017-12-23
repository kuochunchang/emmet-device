from channel import Channel
# from dht11 import dht11
import time


class DH11Channel(Channel):
    def _checking_loop(self):
        last_value = None
        while True:
            self.value = self.value + 10
            if(last_value != self.value):
                self._publish_status() 
                last_value = self.value
    
            time.sleep(self._check_interval)
