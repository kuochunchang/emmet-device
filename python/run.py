from device import Device 
from dht11_channel import DH11Channel

DATA_CHECK_INTERVAL = 2

THE_DEVICE = Device("device-0001")
THE_DEVICE.add_channel(DH11Channel("DHT11", DATA_CHECK_INTERVAL))

THE_DEVICE.run()
