import time
import json
import threading


class Channel(threading.Thread):
    def __init__(self, name, on_status_change, check_interval):
        threading.Thread.__init__(self)
        self._on_status_change = on_status_change
        self._check_interval = check_interval
        self.name = name
        self.value = 1

    def _publish_status(self):
        print("--")
        self._on_status_change(self._json())

    def _json(self):
        state = self.__dict__.copy()
        del state['_on_status_change']
        del state['_check_interval']
        # return json.dumps(state)
        return json.dumps("<---->")

    def run(self):
        self._checking_loop()


    def _checking_loop(self):
        while True:
            next_value = self.value + 1
            if(next_value != self.value):
               self._publish_status() 

            time.sleep(self._check_interval)
