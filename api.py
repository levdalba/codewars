import requests
from datetime import datetime
from pprint import pprint

url_api = "https://api.open-meteo.com/v1/forecast?latitude=13.754&longitude=100.5014&hourly=temperature_2m,relativehumidity_2m&timezone=Asia%2FBangkok"

result = requests.get(url_api)
results = result.json()
max_temperature = max(results["hourly"]['temperature_2m'])
temp_index = results["hourly"]['temperature_2m'].index(max_temperature)
hottest_day = results["hourly"]['time'][temp_index]
hottest_day_datetime = datetime.strptime(hottest_day, '%Y-%m-%dT%H:%M')


print(
    f"The hottest is {hottest_day_datetime} and temperature equals {max_temperature}℃ .")
