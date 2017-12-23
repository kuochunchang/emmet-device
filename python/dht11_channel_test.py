from channel import Channel
import time
import random

class DH11Channel(Channel):
    def _checking_loop(self):
        self.value = 0
        last_value = None
        while True:
            self.value =  str(random.randint(20,30)) + "," + str(random.randint(50,90))
            if(last_value != self.value):
                self._publish_status() 
                last_value = self.value
    
            time.sleep(self._check_interval)
