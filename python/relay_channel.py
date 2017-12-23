from channel import Channel
import time
import RPi.GPIO as GPIO

class RelayChannel(Channel):
    PIN = 19
    _last_value = None
    def update(self, value):
        self.value = value
        if self.value:
            print("--T--")
            GPIO.output(self.PIN,GPIO.HIGH)
        else:
            GPIO.output(self.PIN,GPIO.LOW)
            print("--F--")
            
        print("--------------Relay update to: %s--------------" %(self.value))

    def _checking_loop(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN,GPIO.OUT)
           
        while True:
            if self.value != self._last_value:
                self._publish_status() 
                self._last_value = self.value
            time.sleep(self._check_interval)
