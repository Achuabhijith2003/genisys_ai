import time
import datetime
import requests



def get_weather(location):
    api_key = 'f737c4f8db421551ff71a7445e714c67'  # Replace with your actual API key
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}'
    response = requests.get(base_url)
    return response.json()

if True:
    current_time = time.strftime('%H:%M:%S')
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    location = 'New York'  # Replace with your desired location
    weather_data = get_weather(location)
    
    print(f'Time: {current_time}')
    print(f'Date: {current_date}')
    print(f'Weather in {location}: {weather_data}')
    
    time.sleep(60)  # Wait for 60 seconds before getting the data again
