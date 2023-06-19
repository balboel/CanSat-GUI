import time

from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import RemoteXBeeDevice

# TODO: Replace with the serial port where your first local module is connected to.
PORT_LOCAL = "COM3"
# TODO: Replace with the baud rate of your first local module.
BAUD_RATE_LOCAL = 9600
# TODO: Replace with the serial port where your second local module is connected to.
PORT_REMOTE = "COM4"
# TODO: Replace with the baud rate of your second local module.
BAUD_RATE_REMOTE = 9600


def main():

    print(" +-------------------+")
    print(" | Send Data 16 Test |")
    print(" +-------------------+\n")

    local = XBeeDevice(PORT_LOCAL, BAUD_RATE_LOCAL)
    local_remote = XBeeDevice(PORT_REMOTE, BAUD_RATE_REMOTE)

    try:
        local.open()
        local_remote.open()

        remote = RemoteXBeeDevice(local, x16bit_addr=local_remote.get_16bit_addr())
        local.send_data(remote, "Test message")

        time.sleep(1)

        message = local_remote.read_data()
        assert (message is not None)
        assert (message.remote_device.get_16bit_addr() == local.get_16bit_addr())

        print("Test finished successfully")

    finally:
        if local is not None and local.is_open():
            local.close()
        if local_remote is not None and local_remote.is_open():
            local_remote.close()


if __name__ == "__main__":
    main()