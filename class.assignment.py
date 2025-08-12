class pet:
    def __init__(self, name, species, hunger_level):
        self.name = name
        self.species = species
        self.hunger_level = hunger_level

    def miaow(self):
        print(f"{self.name }"," says Mioaw")  


my_cat = pet("kitty","Panthera","low")

my_cat.miaow()
    