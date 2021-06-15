import RPi.GPIO as GPIO


class Reed_switch:

    def __init__(self, pin=17):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def status(self):
        return GPIO.input(self.pin)
