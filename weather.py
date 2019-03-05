#import requests



#api_address='http://api.openweathermap.org/data/2.5/weather?q=&appid=3371747f2cc96f96f53f3da617aa3f91'

#city = input('City Name :')

#url = api_address + city

#json_data = requests.get(url).json()

#format_add = json_data[0]

#print(json_data)

import requests

from pprint import pprint



city = input('Enter your city : ')



url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=3371747f2cc96f96f53f3da617aa3f91&units=metric'.format(city)



res = requests.get(url)



data = res.json()



temp = data['main']['temp']

wind_speed = data['wind']['speed']



latitude = data['coord']['lat']

longitude = data['coord']['lon']



description = data['weather'][0]['description']

cel = 'Temperature : {} degree celcius'


far = (((temp) *(9/5)+32))
print(far)
