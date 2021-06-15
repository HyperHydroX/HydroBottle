import time
from Mcp9808 import Mcp9808
from smbus import SMBus

i2c = SMBus()
i2c.open(1)
temp_sensor = Mcp9808()


def mcp9808():
    # MCP9808 address, 0x18
    data = i2c.read_byte(0x18)
    time.sleep(0.5)
    # Temp MSB, TEMP LSB
    data = i2c.read_i2c_block_data(0x18, 0x05)
    # Convert the data to 13-bits
    # temp_data = (data[0] << 8) + data[1]
    temp_data = ((data[0] & 0x1F) << 8) + data[1]
    # Output data to console
    temp = temp_data & 0x0FFF
    temp /= 16.0
    if temp_data & 0x1000:
        temp_data -= 256
    print(f"Temperature in Celsius is: C{temp}°")
    return temp


try:
    print("Script started !!!")

    while True:
        mcp9808()
        print(temp_sensor.measure_temperature())
        time.sleep(0.5)


except KeyboardInterrupt as e:
    pass

finally:
    print("Script stopped!!!")
