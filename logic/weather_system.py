import random
from datetime import datetime, timedelta


class WeatherSystem:
    WEATHER_TYPES = ["Sonne", "Bewölkt", "Regen", "Sturm", "Heiß", "Kalt"]

    def __init__(self):
        self.today = datetime.today().date()
        self.forecast = self.generate_weekly_forecast(self.today)

    def generate_weekly_forecast(self, start_date):
        forecast = []
        for i in range(7):
            day = start_date + timedelta(days=i)
            weather = random.choice(self.WEATHER_TYPES)
            forecast.append({"date": day, "weather": weather})
        return forecast

    def advance_day(self):
        self.today += timedelta(days=1)
        self.forecast.pop(0)
        next_day = self.today + timedelta(days=6)
        new_weather = random.choice(self.WEATHER_TYPES)
        self.forecast.append({"date": next_day, "weather": new_weather})

    def get_forecast(self):
        return self.forecast.copy()

    def get_today_weather(self):
        return self.forecast[0]["weather"]
