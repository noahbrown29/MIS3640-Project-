import requests
import json
import urllib.request

APIKEY = '3b46a7354bd3fe80c56d46f63a46a5dc'
city_name = input('Enter the city name:')
base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={APIKEY}&units=imperial'



print(base_url)
f = urllib.request.urlopen(base_url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
print(response_data)
