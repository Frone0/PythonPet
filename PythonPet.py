import GamesControl as Game
from PetStats import Pet
import time
import TextsAppearingEffect as TextEff
import colors as color
import CheckInput as check
import SaveloadPet as save


file_path = save.file_path



my_pet = Pet("")

def StartZero():
    global my_pet
    
    if(file_path.exists()):
        my_pet = save.LoadThePet() 
        TextEff.MakeTextEffect("Hi!!! i was waiting for you!",False)

    else:
          my_pet = Pet(input("Make a name for your pet: "))
          TextEff.MakeTextEffect(f"Hi i am {my_pet.name}, your pet",False)
          TextEff.MakeTextEffect("You should look after me!!!",False)

          save.SaveThePet(my_pet)

    MainPanel()
    GiveCommand()

def GiveCommand():

    while True:
        print("\n")
        print("Enter 0 to see list of comands")
        command = int(check.GetResponse("Choose what you want to do <3:",["0","1","2","3","4"]))

        save.SaveThePet(my_pet)

    
        if(command == 0):
            MainPanel()
        
        elif(command == 1):
            ShowStats()
        
        elif(command == 2):
            FeedThePet()
    
        elif(command == 3):
            Game.ChooseGame()

        elif(command == 4):
            TextEff.MakeTextEffect(f"Bye! {my_pet.name} will wait for you <3", False)
            input("Press Enter to close...")
            return
        else:
            print(color.RED +"Unknown command!" + color.RESET)

def MainPanel():
    TextEff.MakeTextEffect("To check commands ids - 0", True)
    TextEff.MakeTextEffect("To see my stats - 1", True)
    TextEff.MakeTextEffect("To feed me - 2", True)
    TextEff.MakeTextEffect("To play games - 3", True)
    TextEff.MakeTextEffect("To exit - 4", True)

    return


def ShowStats():
    my_pet.UpdateData()

    print(f"Name: {my_pet.name}")
    print(f"age: {int(my_pet.age)}")
    print(f"Health: {int(my_pet.health)}")
    print(f"fullness: {int(my_pet.fullness)}")


def FeedThePet():
    my_pet.FeedThePet()
    TextEff.MakeTextEffect("am am am", False)
    time.sleep(1)
