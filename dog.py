class Dog:

    def __init__(self, name, species, breed):
        self.name = name
        self.species = species
        self.breed = breed

    def __str__(self):
        return f"Kingdom: 'Animalia', Name: '{self.name}', Species '{self.species}', Breed: '{self.breed}'"

    def speak(self):
        print("The dog barks.")