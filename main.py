from animal import Animal
from dog import Dog

if __name__ == "__main__":

    animal1 = Animal("Generic", "Unkown")
    print(animal1)
    animal1.speak()

    dog1 = Dog("Buddy", "Canine", "Golden Retriever")
    print(dog1)
    dog1.speak()

    print("All Animals:")
    for animal in Animal.all_animals:
        print(animal)
