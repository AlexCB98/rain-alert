import requests

API_KEY = 'Example_key'

# https://www.latlong.net/
LAT = 48.669102
LONG = 12.690720

parameters = {
    'lat': LAT,
    'lon': LONG,
    'appid': API_KEY,
}

response = requests.get(
    url='https://api.openweathermap.org/data/2.5/weather',
    params=parameters,
)
response.raise_for_status()

data = response.json()

location = data['name']

