import datetime
import requests
from config import config


def get_weather(location="kerala"):
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={config.WEATHER_API_KEY}'
    response = requests.get(base_url)
    data = response.json()
    
    if response.status_code == 200:
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        return f"The current weather in {location.capitalize()} is {weather_desc} with a temperature of {temp}°C and humidity at {humidity}%."
    else:
        return f"Sorry, I couldn't fetch the weather for {location.capitalize()}. Please check the location name and try again."


def date_time_info():
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time



