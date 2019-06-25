class Algorithms():
    def decimal_degrees_to_time_degrees(self, decimal_degrees):
        assert decimal_degrees >=0 and decimal_degrees <= 360, "decimal degrees is out of scope"
        time_degrees = {"hours": 0, "minutes": 0, "seconds": 0}
        time_degrees["hours"] = int(decimal_degrees)
        time_degrees["minutes"] = int((decimal_degrees - time_degrees["hours"])*60)
        time_degrees["seconds"] = round((decimal_degrees - time_degrees["hours"] - time_degrees["minutes"] / 60) * 3600)
        return time_degrees

    def time_degrees_to_decimal_degrees(self, time):
        assert time["hours"] >= 0 and time["hours"] <= 360, "Time degrees 'hours' is out of scope"
        assert time["minutes"] >= 0 and time["minutes"] < 60 , "Time degrees 'minutes' is out of scope"
        assert time["seconds"] >= 0 and time["seconds"] < 60, "Time degrees 'seconds' is out of scope"
        if time["hours"] == 360:
            time["minutes"] = 0
            time["seconds"] = 0
        return(time["hours"] + time["minutes"]/60 + time["seconds"] / 3600)
