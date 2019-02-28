

def add_city(city , users_city):
        city = raw_input("Enter name of city: ")
        users_city.append(city)
        new_city = raw_input("Would you like to enter another city? (Y/N)")


def main():
        users_city = []
        city = raw_input("Enter Name of city: ")
        users_city.append(city)
        new_city = raw_input("Would you like to enter another city? (Y/N)")
        while(new_city == "y"):
            print(add_city(users_city))
main()
