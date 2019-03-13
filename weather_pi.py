#This code is for the raspberry pi,
#You will need to put this on your raspberry pi
# You will also need to attach an lcd display on to the raspberry pi in order to use it
#install lcddriver.py, there should be a link to it on my github
#Also you do not need to import keyboard



import datetime
import time
import keyboard
import requests
import sys
from pprint import pprint
import lcddriver

display = lcddriver.lcd()
def add_city(weather_for_city , users_city):
    city = raw_input("Enter name of city: ")
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=3371747f2cc96f96f53f3da617aa3f91&units=metric'.format(city)
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
    LCD = True
    users_city = []
    city = raw_input("Enter Name of city: ")
    users_city.append(city)
    new_city = raw_input("Would you like to enter another city? (Y/N)")

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=3371747f2cc96f96f53f3da617aa3f91&units=metric'.format(city)

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
            display.lcd_display_string(("Time: ") +(datetime.datetime.now().strftime("%H:%M:%S")) , 2)
            time.sleep(1)
            display.lcd_clear()

    else:
        while(new_city == "y"):
            add_city(weather_for_city, users_city)

            new_city = raw_input("Would you like to enter another city? (Y/N)")

        while(LCD == True):
            users_city_len = len(users_city)
            for i in range(0 , users_city_len):
                i = 0
                display.lcd_display_string("Current City", 1)
                display.lcd_display_string(users_city[0], 2)
                time.sleep(1)
                display.lcd_clear()
                display.lcd_display_string((("Weather: ") + (str(weather_for_city[i]))) , 1)
                display.lcd_display_string(("Time: ") +(datetime.datetime.now().strftime("%H:%M:%S")) , 2)
                time.sleep(1)
                display.lcd_clear()

                if(keyboard.is_pressed('1')):
                    display.lcd_clear()
                    i += 1
                    display.lcd_display_string("Current City", 1)
                    display.lcd_display_string(users_city[i], 2)
                    time.sleep(1)
                    display.lcd_clear()
                    display.lcd_display_string((("Weather: ") + (str(weather_for_city[i]))) , 1)
                    display.lcd_display_string(("Time: ") +(datetime.datetime.now().strftime("%H:%M:%S")) , 2)
                    time.sleep(1)
                    display.lcd_clear()


                elif(keyboard.is_pressed('2')):
                    i += 2
                    print("Time" + datetime.datetime.utcnow().strftime("%H:%M:%S"))
                    print(("Weather in ") + str(users_city[i]) + (": ")+ str(weather_for_city[i]))
                else:

                display.lcd_clear()



                if(keyboard.is_pressed('1')):
                    display.lcd_clear()
                    i += 1
                    display.lcd_display_string("Current City", 1)
                    display.lcd_display_string(users_city[i], 2)
                    time.sleep(1)
                    display.lcd_clear()
                    display.lcd_display_string((("Weather: ") + (str(weather_for_city[i]))) , 1)
                    display.lcd_display_string(("Time: ") +(datetime.datetime.now().strftime("%H:%M:%S")) , 2)
                    time.sleep(1)
                    display.lcd_clear()


                elif(keyboard.is_pressed('2')):
                    i += 2
                    print("Time" + datetime.datetime.utcnow().strftime("%H:%M:%S"))
                    print(("Weather in ") + str(users_city[i]) + (": ")+ str(weather_for_city[i]))
                else:
                    pass
    print(users_city)
    print(weather_for_city)

main()
