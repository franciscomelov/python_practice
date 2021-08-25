class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far",self.x)

an = PartyAnimal()

for _ in range(4):
    an.party()

print(dir(an))
print(help(an))