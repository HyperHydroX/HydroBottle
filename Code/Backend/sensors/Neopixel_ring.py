import time
import board
import neopixel

ORDER = neopixel.RGB


class Neopixel_ring:
    def __init__(self, pin=board.D10, num_pixels=24, brightness=0.2):
        self.pin = pin
        self.num_pixels = num_pixels
        self.brightness = brightness
        # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
        # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
        self.pixels = neopixel.NeoPixel(
            self.pin, self.num_pixels, brightness=self.brightness, auto_write=False, pixel_order=ORDER
        )

    def wheel(self, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

    def rainbow_cycle(self, delay=0.001):
        for j in range(255):
            for i in range(self.num_pixels):
                pixel_index = (i * 256 // self.num_pixels) + j
                self.pixels[i] = self.wheel(pixel_index & 255)
            self.pixels.show()
            time.sleep(delay)

    def color(self, r=0, g=0, b=0):
        self.pixels.fill((r, g, b))
        self.pixels.show()
