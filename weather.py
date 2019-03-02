import requests



api_address='api.openweathermap.org/data/2.5/forecast?id=524901&APPID=3371747f2cc96f96f53f3da617aa3f91'

city = input('City Name :')

url = api_address + city

json_data = requests.get(url).json()

format_add = json_data['base']

print(format_add)
