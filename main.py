


def main():

        users_city = []
        city = raw_input("Enter Name of city: ")
        users_city.append(city)
        new_city = raw_input("Would you like to enter another city? (Y/N)")
        while(new_city == "y"):
            city = raw_input("Enter name of city: ")
            users_city.append(city)
            new_city = raw_input("Would you like to enter another city? (Y/N)")
main()
