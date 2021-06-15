from datetime import datetime, date
import time
import os
from subprocess import call
from sensors.Mcp9808 import Mcp9808
from sensors.Reed_swich import Reed_switch
from sensors.Oled_display import Oled_display
from sensors.Buzzer import Buzzer
from sensors.Neopixel_ring import Neopixel_ring
import threading

from repositories.DataRepository import DataRepository
from flask import Flask, jsonify, request, redirect
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS

##### Sensors #####
prev_switch_status = 0


def temp_sensor_data():
    temp_sensor = Mcp9808()
    while True:
        # Temp sensor
        DataRepository.create_history(
            1, temp_sensor.measure_temperature(), datetime.now())
        get_temperature(1)
        time.sleep(5)

    print("Script stopped!!!")


def switch_sensor_data():
    cap_count = 0
    DataRepository.create_bottle_cap_count(datetime.now(), cap_count)
    data = DataRepository.read_bottle_cap_count_by_date()
    cap_count = data["BottleCapCount"]

    switch_sensor = Reed_switch()

    while True:
        DataRepository.create_history(
            2, switch_sensor.status(), datetime.now())
        get_switch(2)
        time.sleep(.5)
        global prev_switch_status
        if switch_sensor.status():
            prev_switch_status = 1
        else:
            if prev_switch_status:
                cap_count += 1
                DataRepository.create_bottle_cap_count(
                    datetime.now(), cap_count)

            prev_switch_status = 0


def oled_display():
    person_data = DataRepository.read_person_by_id(1)
    oled = Oled_display()
    oled.execute_items()
    while True:
        oled.show_text("HydroBottle 9001")
        oled.show_ip_address()
        oled.show_water_temp()
        oled.show_user(str(person_data["Firstname"]))
        oled.execute_items()


def toggle_alarm():
    buzzer = Buzzer()
    neo_ring = Neopixel_ring()
    buzzer.alarm_on()
    neo_ring.rainbow_cycle()
    time.sleep(3)
    buzzer.alarm_off()
    neo_ring.color()
    # DataRepository.create_history(5, buzzer.status(), datetime.now())

    # Code voor Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret101!'
socketio = SocketIO(app, cors_allowed_origins="*", logger=False,
                    engineio_logger=False, ping_timeout=1)

CORS(app)

# Handles the default namespace


@socketio.on_error()
def error_handler(e):
    print(e)

# API ENDPOINTS


endpoint = "/api/v1"


@app.route("/")
def hallo():
    return "Server is running, er zijn momenteel geen API endpoints beschikbaar."


@app.route(endpoint + "/history/<sensor_id>", methods=["GET"])
def get_history_by_sensor(sensor_id):
    if request.method == "GET":
        s = DataRepository.read_history_by_id(sensor_id)
        return jsonify(s), 200


@socketio.on("connect")
def initial_connection():
    print("A new client connect")
    data = DataRepository.read_history()
    if data["SensorValue"]:
        previous_data = data["SensorValue"]
    else:
        previous_data = 0
    # # Send to the client!
    socketio.emit("b2f_connected", {
                  "SensorValue": previous_data}, broadcast=True)


@socketio.on("f2b_get_temperature")
def get_temperature(sensor_id):
    # Haal sensor data op
    data = DataRepository.read_history_by_id(1)
    print("Water temperature: " + str(data["SensorValue"]))
    socketio.emit("b2f_show_temperature", {
                  "SensorValue": data["SensorValue"]}, broadcast=True)


@socketio.on("f2b_get_switch")
def get_switch(sensor_id):
    # Haal sensor data op
    data = DataRepository.read_bottle_cap_count_by_date()
    print("Bottle cap count: " + str(data["BottleCapCount"]))
    socketio.emit("b2f_show_bottlecap", {
                  "BottleCapCount": data["BottleCapCount"]}, broadcast=True)


@socketio.on("f2b_get_oled_display")
def turn_on_oled(data):
    # Haal sensor data op
    person_data = DataRepository.read_person_by_id(1)
    sensor_data = DataRepository.read_sensor_by_id(1)
    print("oled values:" +
          str(person_data["Name"]), str(sensor_data["SensorValue"]))
    oled_display()


@socketio.on('f2b_toggle_alarm')
def find_bottle(data):
    # Ophalen van de data
    buzzer_id = data['buzzer_id']
    new_status = data['new_status']
    print(
        f"Buzzer met id sensor id:{buzzer_id} wordt geswitcht naar sensor_status: {new_status}")

    # Stel de status in op de DB
    print(buzzer_id, 1, datetime.now(), new_status)
    res = DataRepository.create_history(
        buzzer_id, 1, datetime.now(), new_status)

    data = DataRepository.read_history_by_id(buzzer_id)
    toggle_alarm()


@socketio.on("f2b_get_waterconsumption_goal")
def get_waterconsumption_goal(data):
    # Haal sensor data op
    person_id = data["person_id"]
    data = DataRepository.read_person_by_id(person_id)
    print("Daily waterconsumption goal: " +
          str(data["WaterConsumptionPerDay"]))
    socketio.emit("b2f_show_waterconsumption", {
                  "WaterConsumptionPerDay": data["WaterConsumptionPerDay"]}, broadcast=True)


@socketio.on("f2b_send_change_waterconsumption")
def change_waterconsumption_goal(data):
    # Haal sensor data op
    person_id = data["person_id"]
    waterconsumption_goal = data["water_consumption_goal"]
    print(person_id, waterconsumption_goal)
    data = DataRepository.update_waterconsumption_goal(
        waterconsumption_goal, person_id)
    print("Changed daily waterconsumption goal: " +
          str(waterconsumption_goal))


@socketio.on("f2b_add_water")
def add_water(data):
    # Haal sensor data op
    bottle_data = DataRepository.read_bottle_by_id(1)
    bottle_id = bottle_data["BottleID"]

    sensor_data = DataRepository.read_history_by_id(1)
    water_temp = sensor_data["SensorValue"]

    water_amount = data["water_consumption"]
    data = DataRepository.create_waterconsumption(
        datetime.now(), bottle_id, water_amount, water_temp)
    print("Added water to waterconsumption: " +
          str(water_amount))


@socketio.on("f2b_get_water_percentage")
def get_water_percentage(data):
    # Haal sensor data op
    person_id = data["person_id"]
    waterconsumption_data = DataRepository.read_waterconsumption_by_date()
    person_data = DataRepository.read_person_by_id(person_id)
    list_waterloss = []
    for data in waterconsumption_data:
        list_waterloss.append(data["WaterLoss"])

    socketio.emit("b2f_show_water_percentage", {
        "WaterConsumptionPerDay": person_data["WaterConsumptionPerDay"], "WaterLoss": list_waterloss}, broadcast=True)
    print("Send waterconsumption_goal & waterconsumptions to front: " +
          str(person_data["WaterConsumptionPerDay"]), str(
              list_waterloss))


@socketio.on("f2b_get_daily_water_history")
def get_water_history(water_id):
    # Haal sensor data op
    waterconsumption_data = DataRepository.read_waterconsumption_by_date()
    list_waterloss = []
    list_drank_datetime = []
    for data in waterconsumption_data:
        print(data)
        list_waterloss.append(data["WaterLoss"])
        list_drank_datetime.append(str(data["Date"]))

    socketio.emit("b2f_show_daily_waterconsumption_history", {
                  "WaterLoss": list_waterloss, "Date": list_drank_datetime}, broadcast=True)
    print("Send history of waterconsumptions to front: " +
          str(person_data["WaterConsumptionPerDay"]), str(
              list_waterloss))


@socketio.on("f2b_turn_off_hydrobottle")
def shutdown_system():
    # Shutsdown the Raspberry pi
    call("echo LordPervert007lol?| sudo -S shutdown -h now", shell=True)


temp_thread = threading.Thread(target=temp_sensor_data)
temp_thread.start()

switch_thread = threading.Thread(target=switch_sensor_data)
switch_thread.start()

oled_thread = threading.Thread(target=oled_display)
oled_thread.start()

# ANDERE FUNCTIES
if __name__ == "__main__":
    socketio.run(app, debug=False, host="0.0.0.0")
