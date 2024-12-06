class Animal:

    kingdom = "Animalia"
    all_animals = []

    def __init__(self, name, species):
        self.name = name
        self.species = species
        super().__init__()
        self.all_animals.append(self)

    def speak(self):
        print("The animal makes a noise.")

    def __str__(self):
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}', Species: '{self.species}'"
