import requests
import pandas as pd

API_key = "17bdfac100aa243eb3047cfdeaa08877"
URL = f"https://api.openweathermap.org/data/3.0/onecall?lat=10.58&lon=77.25&appid={API_key}"

response = requests.get(URL)
raw_data = response.json()


current_weather = raw_data['current']
weather_description = current_weather['weather'][0]['description']

transformed_data = {
    "timestamp": pd.to_datetime(current_weather['dt'], unit='s'),
    "location": raw_data['timezone'],
    "temp_celsius": current_weather['temp'] - 273.15,
    "humidity": current_weather['humidity'],
    "weather_description": weather_description,
    "wind_speed_m_s": current_weather['wind_speed']
}

df = pd.DataFrame([transformed_data])
print(df)