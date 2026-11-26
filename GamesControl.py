import CityGame as City
import  GameGuessNumber as Numbers

IsInGame = False

def ChooseGame():
    IsInGame = False
    print("Which game do you want to play?")
    print("1 - Cities")
    print("2 - Guess the number")
    print("3 - City name generator")

    game_id = int(input("Write a number 1-2: "))

    if game_id == 1:
        print("Let's play Cities!")
        IsInGame = True
        City.StartGame()

    if game_id == 2: 
         print("Let's play Guess the number!")
         IsInGame = True
         Numbers.StartGame()
