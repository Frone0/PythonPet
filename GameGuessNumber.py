import random
import PythonPet as main
import colors as color


Number = 67

def StartGame():
    print("Guess the number from 1 to 1000")
    Number = random.randrange(1,1000)

    tryies = 0

    while True:
        while True:
            PlayerNumber = input("Make your guess:")
    
            if PlayerNumber.isnumeric():
                PlayerNumber = int(PlayerNumber)
                break
            else:
                continue

        tries += 1
    
        if(PlayerNumber == Number):
            print(color.GREEN + "Right! You won" + color.RESET)
            print("You have made: " + tries + " tries")
            main.GiveCommand()
            break
        else:
            if(PlayerNumber > Number):
                print( color.YELLOW + "The chosen number is smaler than: " + color.RESET + str(PlayerNumber))
                continue
            else:
                print( color.YELLOW + "The chosen number is bigger than: " + color.RESET + str(PlayerNumber))
                continue