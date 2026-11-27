import time as t


class Pet:
    def __init__(self, name):
        self.name = name

        self.health = 100
        self.happiness = 100
        self.fullness = 80
        self.energy = 100
        self.age = 0

        self.lastUpdate = t.time()

    def NameThePet(self,Name):
        self.name = Name

    def FeedThePet(self):
        self.fullness = min(100,self.fullness + 10)

    def UpdateData(self):
        Now = t.time()
        passedTime = Now - self.lastUpdate
        self.lastUpdate = Now

        self.fullness = max(0,self.fullness - passedTime * 0.1)
        self.age = self.age + passedTime * 0.01

    def ToDict(self):
        return {"name" : self.name, "happiness" : self.happiness,
                "fullness" : self.fullness,"age": self.age,
                "LastUpdate": self.lastUpdate}

    
        
