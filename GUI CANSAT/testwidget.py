from digi.xbee.devices import XBeeDevice
xbee = XBeeDevice("COM6", 9600)
xbee.open()

# Read data.
xbee_message = xbee.read_data()
print(xbee_message)