# Simple project to check if it is going to rain in next hours.
# This is the good approach for garden owners who want to tune their
# watering systems and save water ("to water or wait for rain")

# API should show accurate prediction, amount and probable hour when it should rain.
# With good rain sensor we can build powerful watering controller that can checkmate
# commercial systems.



from flask import Flask, render_template, redirect, url_for, request
import requests

# OpenWeatherMap credentials
API_OWM_KEY = "ENTER_YOUR_OWN_API_KEY"

# Put your own longitude/latitude data
parameters = {
    "lon": "11.988070",
    "lat": "50.783487",
    "units": "metric",
    "cnt": 5,
    "appid": API_OWM_KEY,
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]

rain_dict = {}

for item in range(0, 5):
    pop_value = weather_data[item]["pop"]
    if pop_value > 0:
        rain_3h_amount = weather_data[item]["rain"]["3h"]
    else:
        rain_3h_amount = 0
    date_timestamp = weather_data[item]["dt_txt"]
    rain_dict[date_timestamp] = {'Probability of rain': int(pop_value*100), 'Rain amount': rain_3h_amount}


app = Flask(__name__)
app.config['SECRET_KEY'] = 'gd(*FKjhnFHJkjuhyfd78UDGFYU'


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html", rain_dict=rain_dict)


if __name__ == "__main__":
    app.run(debug=True)