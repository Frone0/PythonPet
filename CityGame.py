import random
import PythonPet as main
with open("CitysList", encoding="utf-8") as f:
    cities = [line.strip().lower() for line in f if line.strip()]


UsedCities = []
PetCity = "null"
PlayerCity = "null"


def StartGame():
    PetCity = GetRandomCity()
    print("I will start with:\n" + PetCity)

    UsedCities.append(PetCity)
    UsedCities.clear()

    while True:
       print("Your city should start with letter:" + GetLastletterOfCityName(PetCity))
       PlayerCity = input("Name your city (or 'quit'): ").strip().lower()

       if(PlayerCity == "quit"):
           print("Game is over")
           main.GiveCommand()
           break
       if PlayerCity not in cities:
           print("I don't know that city.")
           continue
       if(PlayerCity in UsedCities):
           print("This city was already used!")
           continue 
       if(GetFirstLetterOfCityName(PlayerCity) == GetLastletterOfCityName(PetCity)):
               UsedCities.append(PlayerCity)
               PetCity = FindCityByLetter(GetLastletterOfCityName(PlayerCity))

               if(PetCity == None):
                   print("You Won")
                   break

               if(PetCity not in UsedCities):     
                   UsedCities.append(PetCity)            
                   print("My city is\n" + PetCity)
       else:
           print("Wrong first letter")
           continue


         
def FindCityByLetter(letter):
    options = [c for c in cities if c[0] == letter and c not in UsedCities]
    if not options:
        return None
    
    return random.choice(options)


def GetRandomCity():
    return random.choice(cities)

def GetFirstLetterOfCityName(name):
    return name[0]



def GetLastletterOfCityName(name): 
    i = -1
    while True:
        if name[i].isalpha():
           return name[i]
        else:
           i -= 1
           continue