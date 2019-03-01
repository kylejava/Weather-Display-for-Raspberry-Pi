import datetime
import time
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
            print(users_city)
        else:

            while(new_city == "y"):
                add_city(city, users_city)
                new_city = input("Would you like to enter another city? (Y/N)")
                print(users_city)
        while(LCD == True):
            print(users_city[0])
            print(("Time in ") + (users_city[0]) + str(datetime.datetime.utcnow().strftime("%H:%M:%S")))

main()
