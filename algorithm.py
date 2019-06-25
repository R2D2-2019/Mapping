class Algorithms():
    def time_degrees_to_decimal_degrees(self, time):
        assert time["hours"] >= 0 and time["hours"] <= 360, "Time degrees 'hours' is out of scope"
        assert time["minutes"] >= 0 and time["minutes"] < 60 , "Time degrees 'minutes' is out of scope"
        assert time["seconds"] >= 0 and time["seconds"] < 60, "Time degrees 'seconds' is out of scope"
        if time["hours"] == 360:
            time["minutes"] = 0
            time["seconds"] = 0
        return(time["hours"] + time["minutes"]/60 + time["seconds"] / 3600)
