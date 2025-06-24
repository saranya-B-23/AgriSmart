import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")  # Loaded from .env

def get_weather_data(city):
    """
    Fetch real-time weather data (temperature, humidity, rainfall) for a given city.
    Returns a dictionary with keys: temperature, humidity, rainfall
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code != 200:
            raise ValueError(data.get("message", "Failed to fetch weather data."))

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        # Get rainfall in the last 1 hour
        rainfall = data.get("rain", {}).get("1h", 0.0)

        if rainfall == 0.0:
            print(f" Note: No rain in '{city}' currently. Rainfall set to 0 mm for prediction.")

        return {
            "temperature": temperature,
            "humidity": humidity,
            "rainfall": rainfall
        }

    except Exception as e:
        print(f" Error fetching weather data: {e}")
        return {
            "temperature": None,
            "humidity": None,
            "rainfall": None
        }
