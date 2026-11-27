import json
from pathlib import Path
from PetStats import Pet

file_path = Path("Pet.json")

def SaveThePet(pet):
     with open("Pet.json", "w") as file:
            json.dump(pet.ToDict(), file, indent=2)

def LoadThePet():

    PetDict = {}
    with open("Pet.json", "r") as file:
            PetDict = json.load(file)

    pet = Pet(PetDict["name"])

    pet.fullness = PetDict["fullness"]
    pet.happiness = PetDict["happiness"]
    pet.lastUpdate = PetDict["LastUpdate"]
    pet.age = PetDict["age"]

    return pet
    

    