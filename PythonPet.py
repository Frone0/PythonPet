import GamesControl as Game
from PetStats import Pet
import time
import TextsAppearingEffect as TextEff
import colors as color

my_pet = Pet("")

def StartZero():
    global my_pet
    my_pet = Pet(input("Make a name for your pet: "))
    TextEff.MakeTextEffect(f"Hi i am {my_pet.name}, your pet",False)
    TextEff.MakeTextEffect("You should look after me!!!",False)
    MainPanel()

def GiveCommand():
    print("\n")
    print("Enter 0 to see list of comands")
    command = GetNumber("Choose what you want to do <3:")

    if(command == 0):
        MainPanel()
    
    elif(command == 1):
        ShowStats()
    
    elif(command == 2):
        FeedThePet()

    elif(command == 3):
        Game.ChooseGame()
    else:
        GiveCommand()

def MainPanel():
    TextEff.MakeTextEffect("To check commands ids - 0", True)
    TextEff.MakeTextEffect("To see my stats - 1", True)
    TextEff.MakeTextEffect("To feed me - 2", True)
    TextEff.MakeTextEffect("To play games - 3", True)

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
    TextEff.MakeTextEffect("am am am", False)
    time.sleep(1)
    GiveCommand()
    



def GetNumber(question):
 while True:
    answer = input(question)

    if len(answer) != 1:
        print(color.RED + "Please enter one digit number!" + color.RESET )
        continue

    try:
        number = int(answer)
        return number
        break
    except ValueError:
        print(color.RED + "Please enter a number" + color.RESET)