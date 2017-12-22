from  device_model import ChannelStatus, DeviceStatus, DeviceHeartbeat


channel1 = ChannelStatus("A1", 12)
channel2 = ChannelStatus("A2", 22)

device = DeviceStatus("device-0001")
device.add_channel(channel1)
device.add_channel(channel2)

heartbeat = DeviceHeartbeat("device-0001")

# print(device.channels.__len__())
print(channel1.json())
print(device.json())

print(heartbeat.json())
print(heartbeat.json())
