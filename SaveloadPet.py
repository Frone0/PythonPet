import json
from Paths import SavePath
from PetStats import Pet

file_path = SavePath("Pet.json")

def SaveThePet(pet):
     with open(file_path, "w") as file:
            json.dump(pet.ToDict(), file, indent=2)

def LoadThePet():

    PetDict = {}
    with open(file_path, "r") as file:
            PetDict = json.load(file)

    pet = Pet(PetDict["name"])

    pet.fullness = PetDict["fullness"]
    pet.happiness = PetDict["happiness"]
    pet.lastUpdate = PetDict["LastUpdate"]
    pet.age = PetDict["age"]

    return pet
    

    