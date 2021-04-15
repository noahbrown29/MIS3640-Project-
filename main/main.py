import pycountry
import ccy
from  geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime
from forex_python.converter import CurrencyRates
import requests
import json
import urllib.request

def weather(city_name):
    APIKEY = '3b46a7354bd3fe80c56d46f63a46a5dc'
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={APIKEY}&units=imperial'
    f = urllib.request.urlopen(base_url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    temperature = response_data['main']['temp']
    feels_like = response_data['main']['feels_like']
    return temperature, feels_like

def exchangerates(country_currency):
    c = CurrencyRates()
    try:
        exchange_rate = c.get_rate('USD', country_currency)
    except:
        exchange_rate = "Not Available :("
    return exchange_rate

def time(time_zone):
    IST = pytz.timezone(time_zone)
    return datetime.now(IST)

def main():
    geolocator = Nominatim(user_agent="cityinfogather")
    tf = TimezoneFinder()
    city_name = input('What city are you traveling to: ').strip().capitalize().replace(' ', '+')
    country_name = input('What country are you traveling to: ').strip().capitalize()
    try:
        country = pycountry.countries.get(name = country_name)
        loc = geolocator.geocode(city_name+','+ country_name)
        latitude = loc.latitude
        longitude = loc.longitude
        timezone = tf.timezone_at(lng=longitude, lat=latitude)
        current_time = time(timezone)
        current_time = current_time.strftime('%Y:%m:%d %H:%M:%S')
    except:
        current_time = "Not Available :("
    try:
        country_currency = ccy.countryccy(country.alpha_2)
        exchangerate = exchangerates(country_currency)
    except:
        exchangerate = "Not Available :("
   
    temperature, feels_like = weather(city_name)

    print([exchangerate, temperature, feels_like, current_time])
    return exchangerate, temperature, feels_like, current_time

main()






