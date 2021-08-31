class PartyAnimal:
    x = 0

    def __init__(self, nam) -> None:
        self.name = nam
        print("I am constructed", self.name)

    def party(self):
        self.x = self.x + 1
        print("So far",self.x)
    

class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()