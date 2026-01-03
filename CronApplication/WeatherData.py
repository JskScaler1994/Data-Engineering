import requests

API_key = "17bdfac100aa243eb3047cfdeaa08877"
URL = f"https://api.openweathermap.org/data/3.0/onecall?lat=10.58&lon=77.25&appid={API_key}"

response = requests.get(URL)
data = response.json()

print(data)