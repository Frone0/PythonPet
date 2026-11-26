import random


with open("CitysList", encoding="utf-8") as f:
    cities = [line.strip().lower() for line in f if line.strip()]


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
 
currentletter = "."

def Game():
    print("")
    currentletter = input("Give the first letter: ").strip().lower()

    for i in range(10):
        keys = list(DictionaryOfLetters[currentletter].keys())
        Changes = list(DictionaryOfLetters[currentletter].values())

        print(currentletter, end="", flush=True)
        nextletter = random.choices(keys,Changes)[0]

        if(nextletter == "."):
           break 
        currentletter = nextletter
    Game()

Game()
    