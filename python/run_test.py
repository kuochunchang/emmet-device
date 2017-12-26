from device import Device 
from dht11_channel_test import DH11ChannelTest
from relay_channel_test import RelayChannelTest


DATA_CHECK_INTERVAL = 2

THE_DEVICE = Device("device-0001")
THE_DEVICE.add_channel(DH11ChannelTest("DHT11", DATA_CHECK_INTERVAL))
THE_DEVICE.add_channel(RelayChannelTest("RELAY", DATA_CHECK_INTERVAL))

THE_DEVICE.run()
