import logging

from digi.xbee.devices import XBeeDevice
from digi.xbee.exception import XBeeException

# TODO: Replace with the serial port where your local module is connected to.
PORT = "COM3"
# List of baudrates
BAUD_RATES = (115200, 57600, 38400, 19200, 9600)


def main():
    print("""
 +------------------------------------------------------+
 | XBee Python Library Recover serial connection Sample |
 +------------------------------------------------------+
    """)

    for baudrate in BAUD_RATES:
        print("Opening the XBee device by forcing its baudrate to %d" % baudrate)
        device = XBeeDevice(PORT, baudrate)

        try:
            device.open(force_settings=True)
            print("Device opened and set to operate at %d bauds" % baudrate)
        except XBeeException as e:
            print("ERROR: %s" % str(e))
            return
        finally:
            if device is not None and device.is_open():
                device.close()


if __name__ == '__main__':
    main()