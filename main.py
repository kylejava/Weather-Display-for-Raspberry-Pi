#this code is for the computer
#I made this code before applying it on the raspberry pi in order to sort out my algorithm
#This code is in python 3 while the main_pi.py is in python 2.7


import datetime
import time
import keyboard
import requests
import sys
from pprint import pprint

def add_city(weather_for_city , users_city):
    city = input("Enter name of city: ")
    users_city.append(city)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=3371747f2cc96f96f53f3da617aa3f91&units=metric'.format(city)
    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    cel = 'Temperature : {} degree celcius'
    new_far = (((temp) *(9/5)+32))
    weather_for_city= []
    weather_for_city.append(new_far)
    return(users_city)
    return (weather_for_city)





def main():
    LCD = True
    users_city = []
    city = input("Enter Name of city: ")
    users_city.append(city)
    new_city = input("Would you like to enter another city? (Y/N)")

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=3371747f2cc96f96f53f3da617aa3f91&units=metric'.format(city)
    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    cel = 'Temperature : {} degree celcius'
    far = (((temp) *(9/5)+32))

    weather_for_city= []
    weather_for_city.append(far)
    if(new_city != "y"):
        while(LCD == False):
            print("Weather in " + users_city[0] + ": "+ str(far))
            print("Time: " + datetime.datetime.now().strftime("%H:%M:%S"))
    else:
        while(new_city == "y"):
            add_city(city, users_city)

            new_city = input("Would you like to enter another city? (Y/N)")

        while(LCD == False):
            users_city_len = len(users_city)
            for i in range(0 , users_city_len):
                i = 0
                print("Time" + datetime.datetime.utcnow().strftime("%H:%M:%S"))
                print(("Weather in ") + str(users_city[i]) + (": ")+ (str(far)))
                if(keyboard.is_pressed('a')):
                    i += 1
                    while(keyboard.is_pressed('a')):
                        print("Time" + datetime.datetime.utcnow().strftime("%H:%M:%S"))
                        print(("Weather in ") + str(users_city[i]) + (": ")+ str(far))
                else:
                    pass
    print(users_city)
    print(weather_for_city)
main()
