import os
os.system("clear")
from simple_term_menu import TerminalMenu 
from dog import Dog
import dogsSDK


def main_menu():
    options = ["Add Dog", "Delete Dog", "Get Info", "Feeding/Meds", "Grooming/Belongings", "Quit"]
    main_menu = TerminalMenu(options)
    info_options = ["All", "Large", "Small", "Search Name"]
    info_menu = TerminalMenu(info_options)

    quit = False

    while quit == False:
        optionsList = main_menu.show()
        optionsChoice = options[optionsList]

        if(optionsChoice == "Quit"):
            quit = True

        if(optionsChoice == "Add Dog"):
            name = input("Dog's name: ")
            owner = input("Owner's name: ")
            breed = input("Breed: ")
            size = input("Large or Small: ")
            age = input("Age: ")
            gender = input("Gender: ")
            feed_meds = input("Medication or special food required: ")
            grooming = input("Do they need grooming?: ")
            belongings = input("Do they have any belongings?: ")
            friendly = input("Are they friendly?: ")
            dog = Dog(name, owner, breed, size, age, gender, feed_meds, grooming, belongings, friendly)
            dogsSDK.add_dog(dog)

        if(optionsChoice == "Delete Dog"):
            name = input("Name: ")
            dogsSDK.delete_dog(name)

        if(optionsChoice == "Get Info"):
            optionsList = info_menu.show()
            optionsChoice = info_options[optionsList]
            if(optionsChoice == "All"):
                print(dogsSDK.get_dogs())
            if(optionsChoice == "Large"):
                print(dogsSDK.get_large_dogs())
            if(optionsChoice == "Small"):
                print(dogsSDK.get_small_dogs())
            if(optionsChoice == "Search Name"):
                name = input("Name: ")
                print(dogsSDK.get_info(name))

        if(optionsChoice == "Feeding/Meds"):
            print(dogsSDK.feed_meds())

        if(optionsChoice == "Grooming/Belongings"):
            print(dogsSDK.out_groom())
            print(dogsSDK.out_belongings())

        else:
            print(optionsChoice)

main_menu()