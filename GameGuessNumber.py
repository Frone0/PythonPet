import random
Number = 67

def StartGame():
    print("Guess the number from 1 to 1000")
    Number = random.randrange(1,1000)

    while True:
        PlayerNumber = int(input("Make your guess:"))
    
        if(PlayerNumber == Number):
            print("Right! You won")
            break
        else:
            if(PlayerNumber > Number):
                print("The chosen number is smaler than" + str(PlayerNumber))
                continue
            else:
                print("The chosen number is bigger than" + str(PlayerNumber))
                continue