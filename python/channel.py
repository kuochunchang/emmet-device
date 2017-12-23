import time
import json
import threading


class Channel(threading.Thread):
    def __init__(self, name , check_interval, on_status_change = None):
        threading.Thread.__init__(self)
        self._on_status_change = on_status_change
        self._check_interval = check_interval
        self.name = name
        self.value = 1

    def set_callback(self, callback):
        self._on_status_change = callback

    def _publish_status(self):
        print("--")
        self._on_status_change(self)

    def _json(self):
        state = {}
        state["name"] = self.name
        state["value"] = self.value
        # state["lastUpdateTime"] = int(time.time())

        return json.dumps(state)


    def run(self):
        self._checking_loop()
    
    """
    交給子類別實做
    """
    def _checking_loop(self):
        pass

