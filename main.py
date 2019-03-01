import datetime
import time
import keyboard
import pytz
def add_city(city , users_city):
        city = input("Enter name of city: ")
        users_city.append(city)
        return(users_city)


def main():
        time = datetime.datetime.utcnow().strftime("%H:%M:%S")
        LCD = True
        users_city = []

        city = input("Enter Name of city: ")
        users_city.append(city)
        new_city = input("Would you like to enter another city? (Y/N)")
        if(new_city != "y"):
            print(users_city[0])
        else:

            while(new_city == "y"):
                add_city(city, users_city)
                new_city = input("Would you like to enter another city? (Y/N)")
        while(LCD == True):
            users_city_len = len(users_city)
            for i in range(0 , users_city_len):
                    print(users_city[i])

main()
