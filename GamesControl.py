import CityGame as City
import  GameGuessNumber as Numbers
import GameRealOrFake as GeneratorGame
import PythonPet as pet
import CheckInput as check

IsInGame = False

def ChooseGame():
    IsInGame = False
    print("Which game do you want to play?\n")
    print("0 - return to commands")
    print("1 - Cities")
    print("2 - Guess the number")
    print("3 - Real city or not")

    
    game_id = int(check.GetResponse("Write a number 1-2-3: ", ["0","1","2","3"]))

    if  game_id == 0:
        return

    if game_id == 1:
        print("Let's play Cities!")
        IsInGame = True
        City.StartGame()

    if game_id == 2: 
         print("Let's play Guess the number!")
         IsInGame = True
         Numbers.StartGame()

    if game_id == 3:
        print("Let's play Real city or not!")
        IsInGame = True
        GeneratorGame.StartGame()
