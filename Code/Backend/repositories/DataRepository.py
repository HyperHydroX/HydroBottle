from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    ##### Sensors #####
    @staticmethod
    def read_sensors():
        sql = "SELECT * FROM Sensors"
        return Database.get_rows(sql)

    @staticmethod
    def read_sensor_by_id(id):
        sql = "SELECT * FROM Sensors WHERE id = %s"
        params = [id]
        return Database.get_one_row(sql, params)

    ##### History #####
    @staticmethod
    def read_history():
        sql = "SELECT * FROM History"
        return Database.get_rows(sql)

    @staticmethod
    def read_history_by_id(id):
        sql = "SELECT * FROM History WHERE SensorID = %s ORDER BY date DESC"
        params = [id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def create_history(id, sensor_value, date, sensor_status=1):
        sql = "INSERT INTO History (SensorID, SensorValue, Date, SensorStatus) VALUES (%s, %s, %s, %s)"
        params = [id, sensor_value, date, sensor_status]
        return Database.execute_sql(sql, params)

    @staticmethod
    def update_history_by_id(id, sensor_value, date, sensor_status=1):
        sql = "UPDATE History h SET h.SensorValue = %s, h.Date = %s, h.SensorStatus = %s WHERE SensorID = %s"
        params = [id, sensor_value, date, sensor_status]
        return Database.execute_sql(sql, params)

    ##### Bottles #####

    @staticmethod
    def read_bottles():
        sql = "SELECT * FROM bottles"
        return Database.get_rows(sql)

    @staticmethod
    def read_bottle_by_id(id):
        sql = "SELECT * FROM Bottles WHERE BottleID = %s"
        params = [id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def update_bottle(id, bottle_cap_opened):
        sql = "UDPATE Bottle b SET b.BottleCapOpened = %s WHERE BottleID = %s"
        params = [id, bottle_cap_opened]
        return Database.execute_sql(sql, params)

    ##### bottleCapCount #####
    def read_bottle_cap_count():
        sql = "SELECT * FROM BottleCapCount"
        return Database.get_rows(sql)

    def read_bottle_cap_count_by_date():
        sql = "SELECT MAX(BottleCapCount) AS BottleCapCount FROM BottleCapCount WHERE DATE(Date) = CURDATE() ORDER BY date DESC"
        return Database.get_one_row(sql)

    @staticmethod
    def create_bottle_cap_count(date, bottle_cap_count):
        sql = "INSERT INTO BottleCapCount (date, BottleCapCount) VALUES (%s, %s)"
        params = [date, bottle_cap_count]
        return Database.execute_sql(sql, params)

    ##### Waterconsumption #####

    @staticmethod
    def read_waterconsumption():
        sql = "SELECT * FROM WaterConsumption"
        return Database.get_rows(sql)

    @staticmethod
    def read_waterconsumption_by_date():
        sql = "SELECT * FROM WaterConsumption WHERE DATE(Date) = CURDATE()"
        return Database.get_rows(sql)

    @staticmethod
    def create_waterconsumption(date, bottle_id, waterloss, watertemperature):
        sql = "INSERT INTO WaterConsumption (date, BottleID, WaterLoss, WaterTemperature) VALUES (%s, %s, %s, %s)"
        params = [date, bottle_id, waterloss, watertemperature]
        return Database.execute_sql(sql, params)

    @staticmethod
    def update_waterconsumption(id, water_loss, water_temperature):
        sql = "UPDATE WaterConsuption w SET w.WaterLoss = %s, w.Watertemperature = %s WHERE WaterConsumptionID = %s"
        params = [id, water_loss, water_temperature]
        return Database.execute_sql(sql, params)

    ##### Persons #####
    @staticmethod
    def read_persons():
        sql = "SELECT * FROM Persons"
        return Database.get_rows(sql)

    @staticmethod
    def read_person_by_id(id):
        sql = "SELECT * FROM Persons WHERE PersonID = %s"
        params = [id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def create_person(name, firstname, age, length, weight, waterconsumption_perday):
        sql = "INSERT INTO Persons (Name, Firstname, Age, Length, Weight, WaterConsumptionPerDay) VALUES (%s, %s, %s, %s, %s, %s)"
        params = [name, firstname, age, length,
                  weight, waterconsumption_perday]
        return Database.execute_sql(sql, params)

    @staticmethod
    def update_waterconsumption_goal(goal, id):
        sql = "UPDATE Persons p SET p.WaterConsumptionPerDay = %s WHERE PersonID = %s"
        params = [goal, id]
        return Database.execute_sql(sql, params)

    @staticmethod
    def delete_person(id):
        sql = "DELETE FROM Persons WHERE PersonID = %s"
        params = [id]
        return Database.execute_sql(sql, params)
