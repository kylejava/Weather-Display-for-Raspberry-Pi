#This code is for the raspberry pi,
#You will need to put this on your raspberry pi
# You will also need to attach an lcd display on to the raspberry pi in order to use it
#install lcddriver.py, there should be a link to it on my github
#Also you do not need to import keyboard




import datetime
import time
import requests
import sys
from pprint import pprint
import lcddriver
import RPi.GPIO as GPIO


display = lcddriver.lcd()
def add_city(weather_for_city , users_city):
    city = raw_input("Enter name of city: ")
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid='YOUR API KEY'&units=metric'.format(city)
    res = requests.get(url)
    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    cel = 'Temperature : {} degree celcius'
    far = (((9.0/5.0) *(temp)+32))

    users_city.append(city)
    weather_for_city.append(str(far))
    return(users_city)





def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    button = GPIO.input(18)
    LCD = True
    users_city = []
    city = raw_input("Enter Name of city: ")
    users_city.append(city)
    new_city = raw_input("Would you like to enter another city? (Y/N)")

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=3371747f2cc96f96f53f3da617aa3f91&units=metric'.format(city)
    res = requests.get(url)
    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    cel = 'Temperature : {} degree celcius'
    far = (((9.0/5.0) *(temp)+32))

    weather_for_city= []
    weather_for_city.append(far)
    if(new_city != "y"):
        while(LCD == True):
            display.lcd_display_string("Current City", 1)
            display.lcd_display_string(users_city[0], 2)
            time.sleep(1)
            display.lcd_clear()
            display.lcd_display_string((("Weather: ") + (str(weather_for_city[0]))) , 1)
            display.lcd_display_string(("Time: ") +(datetime.datetime.now().strftime("%H:%M:%S"))
            time.sleep(1)
            display.lcd_clear()

    else:
        while(new_city == "y"):
            add_city(weather_for_city, users_city)

            new_city = raw_input("Would you like to enter another city? (Y/N)")



        while(LCD == True):
            users_city_len = len(users_city)
            for i in range(0 , users_city_len):
                while(i != users_city_len):
                        print("Hold Down Button Until City Changes To Change The Current City")
                        display.lcd_display_string("Current City", 1)
                        display.lcd_display_string(users_city[i], 2)
                        time.sleep(1)
                        display.lcd_clear()
                        display.lcd_display_string(("Weather: ") + (str(weather_for_city[i]))) ,1)
                        display.lcd_display_string(("Time: ") +(datetime.datetime.now().strftime("%H:%M:%S")) , 2)
                        time.sleep(1)
                        display.lcd_clear()
                        if(button == False):
                                i += 1
                            if(i == users_city_len):
                                i = 0
                        else:
                                pass



main()
