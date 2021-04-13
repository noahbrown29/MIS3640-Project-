import requests
import json
import urllib.request

# Asks the user to input their current currency, then desired currency and the amount to be converted
CURRENCY_1 = str(input("I want to go from this currency: "))
CURRENCY_2 = str(input("To this currency: "))
AMOUNT = float(input("What amount of money?: "))

url = f'https://api.exchangerate.host/convert?from={CURRENCY_1}&to={CURRENCY_2}&amount={AMOUNT}'
response = requests.get(url)
data = response.json()
# The code will output the conversion of the currency 
print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
print(response_data)