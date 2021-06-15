from RPi import GPIO
import time


class Buzzer:

    def __init__(self, buzzer_pin=6):
        self.buzzer_pin = buzzer_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)

    def alarm_on(self):
        print("Alarm starts")
        GPIO.output(self.buzzer_pin, GPIO.HIGH)

    def alarm_off(self):
        print("Alarm stopt")
        GPIO.output(self.buzzer_pin, GPIO.LOW)
