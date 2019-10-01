#! python3
# Prints the weather for a location from the command line with fake appId

import json
import requests
import sys

# Compute location from command line args
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()

location = 'shanghai'

# Download the JSON data from OpenWeatherMap.org's API
url = 'https://openweathermap.org/data/2.5/forecast?q=%s,us&mode=json&appid=b6907d289e10d714a6e88b30761fae22' % (location)
print('url is %s' % url)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a python file
weatherData = json.loads(response.text)
# Print weather desc
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])