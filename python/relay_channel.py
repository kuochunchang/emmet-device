from channel import Channel
import time
import RPi.GPIO as GPIO

class RelayChannel(Channel):

    _last_value = None
    def update(self, value):
        self.value = value
        if self.value:
            GPIO.output(22,GPIO.HIGH)
        else:
            GPIO.output(22,GPIO.LOW)
            
        print("--------------Relay update to: %s--------------" %(self.value))

    def _checking_loop(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(13,GPIO.OUT)
       
        while True:
            if self.value != self._last_value:
                self._publish_status() 
                self._last_value = self.value
            time.sleep(self._check_interval)