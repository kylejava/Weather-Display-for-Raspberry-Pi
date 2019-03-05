import requests



api_address='http://api.openweathermap.org/data/2.5/weather?q=&appid=3371747f2cc96f96f53f3da617aa3f91'

city = input('City Name :')

url = api_address + city

json_data = requests.get(url).json()

format_add = json_data[0]

print(json_data)
