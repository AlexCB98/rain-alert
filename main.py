import requests
import smtplib

#https://openweathermap.org/
API_KEY = 'YOUR_API_KEY'

# https://www.latlong.net/
LAT = 48.669102
LONG = 12.690720

MY_EMAIL = 'Example@gmail.com'
MY_PASSWORD = 'Your_password'

parameters = {
    'lat': LAT,
    'lon': LONG,
    'appid': API_KEY,
    'cnt': 4,
}

response = requests.get(
    url='https://api.openweathermap.org/data/2.5/forecast',
    params=parameters,
    timeout=10,
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
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='lexyus22@gmail.com',
            msg=(f"Subject: OpenWeather's API\n\n"
                 'Bring an Umbrella')
        )
