import requests

#https://openweathermap.org/
API_KEY = 'YOUR_API_KEY'

# https://www.latlong.net/
LAT = 48.669102
LONG = 12.690720

parameters = {
    'lat': LAT,
    'lon': LONG,
    'appid': API_KEY,
    'cnt': 4,
}

response = requests.get(
    url='https://api.openweathermap.org/data/2.5/forecast',
    params=parameters,
)
response.raise_for_status()
data = response.json()

weather_data = data['list']

will_rain = False

for forecast in weather_data:
    weather_id = forecast['weather'][0]['id']

    if weather_id < 700:
        will_rain = True

if will_rain:
    print('Bring an Umbrella')