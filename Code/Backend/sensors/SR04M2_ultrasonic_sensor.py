from RPi import GPIO
import time
import math

echo = 27
trigger = 22


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(echo, GPIO.IN)
    GPIO.setup(trigger, GPIO.OUT)
    time.sleep(0.00001)
    GPIO.output(trigger, GPIO.LOW)


def measure_distance_in_cm():
    time.sleep(0.1)
    GPIO.output(trigger, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger, GPIO.LOW)

    while GPIO.input(echo) == 0:
        pulse_start_time = time.time()
    while GPIO.input(echo) == 1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = (pulse_duration * 17150)
    print("Measured Distance = %.1f cm" % distance)
    return distance


def calculate_water(data):
    # 4.30cm = 0cl, 4.15cm = 750 (0.15cm speling)
    # 0.15 / 750 = 0.0002 ==> 0.0002 = 0% & 0.15 = 100%
    # 0.0002 = 1cl
    # V = πr2h .
    # volume_bottle = round((math.pi*(4**2)) * 17)
    # print(f"volume of the bottle is: {volume_bottle} cm3")
    return round(data * 166)


try:
    print("Script started !!!")
    setup()

    while True:
        measure = 0
        for i in range(0, 5):
            measure = measure_distance_in_cm()

        time.sleep(5)
        average_measure = measure / 5
        print(f"Water in bottle: {round(average_measure, 2)} cm")
        print(
            f"test calculate water: {calculate_water(average_measure)} cl in bottle")
        # take five reading
        # water_level = 0

        # for in range(0, 5):
        #     read_value = measure_distance_in_cm()
        #     # unstable reading
        #     if read_value > 16 or read_value < 3:
        #         # return to calling function because reading is unstable
        #         return
        #     # valid value
        #     elif read_value <= 16 and read_value >= 3:
        #         water_level = water_level + read_value

        #     time.sleep(10)


except KeyboardInterrupt as e:
    pass

finally:
    GPIO.cleanup()
    print("Script stopped!!!")
