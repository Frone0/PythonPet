import random
import json
from Paths import DataPath

file_path = DataPath("DictionaryOfLetters.json")

with open(DataPath("CitysList"), encoding="utf-8") as f:
    cities = [line.strip().lower() for line in f if line.strip()]

if(not file_path.exists()):

    for i, CityName in enumerate(cities):
        cities[i] = "." + CityName + "."
    
    
    
    DictionaryOfLetters = {"a" : {"b" : 1}}
    
    for word in cities:
        for letter in word:
            if letter not in DictionaryOfLetters:
                DictionaryOfLetters[letter] = {}
    
    
    
    for  word in (cities):
        letters = list(word)
    
        for i in range(len(letters) - 1):
                if letters[i + 1] in DictionaryOfLetters[letters[i]]:
                    DictionaryOfLetters[letters[i]][letters[i + 1]] += 1   
                else:
                    DictionaryOfLetters[letters[i]][letters[i + 1]] = 1  
                    
    with open(file_path, "w") as file:
        json.dump(DictionaryOfLetters, file, indent=2)
    

else:
    with open(file_path, "r") as file:
        DictionaryOfLetters = json.load(file)
   


def Generation(letter):
    print("")
    CityName = ""
    currentletter = letter.strip().lower()

    while True:
        
        keys = list(DictionaryOfLetters[currentletter].keys())
        Chances = list(DictionaryOfLetters[currentletter].values())

        nextletter = random.choices(keys,Chances)[0]


        if(nextletter == "."):
           return CityName 

        currentletter = nextletter
        CityName += currentletter
        #print(currentletter, end="", flush=True)
