from RPi import GPIO
import sys
import time

pin = 17


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Set BtnPin's mode is input, and pull up to high level(3.3V)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=detect, bouncetime=200)


def detect(chn):
    print(GPIO.input(pin))  # Printing detected magnetic substance


def status(pin):
    channel = GPIO.wait_for_edge(channel, GPIO_RISING, timeout=5000)
    if channel is None:
        print('Timeout occurred')
    else:
        print('Edge detected on channel', channel)


try:
    print("Script started !!!")
    setup()

    while True:
        input = GPIO.input(17)
        print(input)
        time.sleep(1)


except KeyboardInterrupt as e:
    pass

finally:
    GPIO.cleanup()
    print("Script stopped!!!")
