class Dog:
    kingdom = "Animilia"

    def __init__(self, name, species, breed):
        self.name = name
        self.species = species
        self.breed = breed
        super().__init__()

    def __str__(self):
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}', Species '{self.species}', Breed: '{self.breed}'"

    def speak(self):
        print("The dog barks.")