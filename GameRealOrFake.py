from Paths import DataPath
import random
import CityNameGenerator as Generator
import PythonPet as main
import TextsAppearingEffect as TextEff
import CheckInput as check
import colors as color



score = 0

with open(DataPath("CitysList"), encoding="utf-8") as f:
    cities = [line.strip().lower() for line in f if line.strip()]

isReal = False

def StartGame():
    TextEff.MakeTextEffect("In this game you are getting city names", False)
    TextEff.MakeTextEffect("and you should decide wheter it is real or not", False)
    Game()

def Game():

    global score

    while True:
        print(" ")
        if random.randint(1, 2) == 1:
            print(Generator.Generation("."))
            isReal = False
        else:
            print(random.choice(cities))
            isReal = True

        print(" ")
    
        TextEff.MakeTextEffect("Is this a real city?",True)
        TextEff.MakeTextEffect("yes - 1",True)
        TextEff.MakeTextEffect("no - 2",True)

        
        PlayerInput = check.GetResponse("Choose: ", ["1","2","quit"])
        
        if(PlayerInput == "quit"):
            if score > 0:
               AnswerColor =  color.GREEN
            else:
               AnswerColor =  color.RED

            print("Your score: " + AnswerColor + str(score) + color.RESET)
            return
    
        chosednumber = int(PlayerInput)
    
        
        if chosednumber == 1: 
            playerChose = True 
        else: 
            playerChose = False
    
        if playerChose == isReal:
            print(color.GREEN + "Right!" + color.RESET)
            score += 1
        else:
            print(color.RED + "Wrong!" + color.RESET) 
            score -= 1
    
