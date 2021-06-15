# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

import time

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from sensors.Mcp9808 import Mcp9808
import socket


class Oled_display:
    def __init__(self):

        # Create the I2C interface.
        self.i2c = busio.I2C(SCL, SDA)

        # Create the SSD1306 OLED class.
        # The first two parameters are the pixel width and pixel height.  Change these
        # to the right size for your display!
        self.disp = adafruit_ssd1306.SSD1306_I2C(128, 32, self.i2c)

        # Clear display.
        self.disp.fill(0)
        self.disp.show()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new("1", (self.width, self.height))

        # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)

        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        # Draw some shapes.
        # First define some constants to allow easy resizing of shapes.
        padding = -2
        self.top = padding
        self.bottom = self.height - padding
        # Move left to right keeping track of the current x position for drawing shapes.
        self.x = 0

        # Load default font.
        self.font = ImageFont.load_default()

    # def turn_display_on(self):
    #     # Draw a black filled box to clear the image.
    #     self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

    def show_ip_address(self):
        ip_address = ''
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        self.draw.text((self.x, self.top + 16), "Ip: " +
                       ip_address, font=self.font, fill=255)

    def show_user(self, name):
        self.draw.text((self.x, self.top + 8), "Looking good " + name.capitalize() + " !",
                       font=self.font, fill=255)

    def show_text(self, text):
        self.draw.text((self.x, self.top + 0), text,
                       font=self.font, fill=255)

    def show_water_temp(self):
        temp = Mcp9808()
        self.draw.text((self.x, self.top + 24), "Temp: " +
                       str(temp.measure_temperature()) + "°C", font=self.font, fill=255)

    def show_water_volume(self):
        pass

    def execute_items(self):
        self.disp.image(self.image)
        self.disp.show()
        time.sleep(0.1)
