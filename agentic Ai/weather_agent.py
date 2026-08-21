import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read API key from .env
WEATHER_API = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    if not WEATHER_API:
        return "❌ API key not found. Please set WEATHER_API_KEY in .env file."

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,             # city name
        "appid": WEATHER_API,  # API key
        "units": "metric"      # Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        return f"🌤 Weather in {city}:\n" \
               f"🌡 Temperature: {temp}°C\n" \
               f"☁ Condition: {desc}\n" \
               f"💧 Humidity: {humidity}%\n" \
               f"🌬 Wind Speed: {wind} m/s"
    except requests.exceptions.RequestException as e:
        return f"❌ Request error: {e}"
    except KeyError:
        return "❌ Could not parse weather data. Check city name or API key."

if __name__ == "__main__":
    city = input("Enter city name (e.g., Nanded,IN): ")
    print(get_weather(city))
