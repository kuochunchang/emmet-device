import time
import json

class DeviceHeartbeat(object):
    def __init__(self, device_id):
        self.deviceId = device_id
        self.timestamp = 0
        self.sequence = 0

    def new(self):
        self.sequence +=  1
        self.timestamp = int(time.time())
        return self

    def json(self):
        return json.dumps(self.__dict__)
    

class DeviceStatus(object):
    def __init__(self, device_id):
        self.deviceId = device_id
        self.channels = []

    def add_channel(self, channel):
        self.channels.append(channel)

    def json(self):
        return json.dumps(self.__dict__, cls=ComplexEncoder)


class ChannelStatus(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.lastUpdateTime = int(time.time())

    def json(self):
        return self.__dict__


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'json'):
            return obj.json()
        else:
            return json.JSONEncoder.default(self, obj)