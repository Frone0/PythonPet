import random
import colors as color
import TextsAppearingEffect as TextEff

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
       print("\nYour city should start with letter:" + color.YELLOW + GetLastletterOfCityName(PetCity) + color.RESET) 
       PlayerCity = input("Name your city (or 'quit'): ").strip().lower()

       if(PlayerCity == "quit"):
           print(color.RED + "Game is over" + color.RESET)
           return
       if PlayerCity not in cities:
           print(color.RED + "I don't know thit city." + color.RESET)
           continue
       if(PlayerCity in UsedCities):
           print(color.RED + "This city was already used!" + color.RESET)
           continue 
       if(GetFirstLetterOfCityName(PlayerCity) == GetLastletterOfCityName(PetCity)):
               UsedCities.append(PlayerCity)
               PetCity = FindCityByLetter(GetLastletterOfCityName(PlayerCity))

               if(PetCity == None):
                   print(color.GREEN + "You Won" + color.RESET)
                   break

               if(PetCity not in UsedCities):     
                   UsedCities.append(PetCity)            
                   TextEff.MakeTextEffect("My city is\n" + color.YELLOW + PetCity + color.RESET,False)
       else:
           print(color.RED + "Wrong first letter" + color.RESET)
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