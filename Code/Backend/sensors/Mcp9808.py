from RPi import GPIO
from smbus import SMBus

i2c = SMBus()
i2c.open(1)


class Mcp9808:

    def __init__(self, address=0x18):
        self.address = address
        GPIO.setmode(GPIO.BCM)

    def measure_temperature(self):
        # MCP9808 address, 0x18
        data = i2c.read_byte(self.address)
        # Temp MSB, TEMP LSB
        data = i2c.read_i2c_block_data(self.address, 0x05)
        # Convert the data to 13-bits
        temp_data = round(((data[0] & 0x1F) < 8) + data[1] * 0.10, 2)
        # Convert temp_data to temperature
        temp_data = ((data[0] & 0x1F) << 8) + data[1]
        # Output data to console
        temp = temp_data & 0x0FFF
        temp /= 16.0
        if temp_data & 0x1000:
            temp_data -= 256
        # Output data to console
        return round(temp)
