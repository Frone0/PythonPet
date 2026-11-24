import GamesControl as Game
from PetStats import Pet
import time


my_pet = Pet("")

def StartZero():
    global my_pet
    my_pet = Pet(input("Make a name for your pet: "))
    print(f"Hi i am {my_pet.name}, your pet")
    print("You should look after me!!!")
    MainPanel()

def GiveCommand():
    print("Enter 0 to see list of comands")
    command = int(input("Choose what you want to do <3:"))

    if(command == 0):
        MainPanel()
    
    if(command == 1):
        ShowStats()
    
    if(command == 2):
        FeedThePet()

    if(command == 3):
        Game.ChooseGame()

def MainPanel():
    print("To check commands ids - 0")
    print("To see my stats - 1")
    print("To feed me - 2")
    print("To play games - 3")

    GiveCommand()

def ShowStats():
    my_pet.UpdateData()

    print(f"Name: {my_pet.name}")
    print(f"Happiness: {my_pet.happiness}")
    print(f"Health: {my_pet.health}")
    print(f"fullness: {my_pet.fullness}")

    GiveCommand()

def FeedThePet():
    my_pet.FeedThePet()
    print("am am am")
    time.sleep(1)
    GiveCommand()
    
