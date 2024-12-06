
if __name__ == "__main__":
    # TODO: Create an instance of the Animal class
    # TODO: Print the Animal instance
    # TODO: Call the method to make a generic animal sound

    # TODO: Create an instance of the Dog class
    # TODO: Print the Dog instance
    # TODO: Call the method to make the dog-specific sound

    # TODO print out all the animals

    from animal import Animal
    from dog import Dog

    animal1 = Animal("Buddy", "Canine")
    print(animal1)
    animal1.speak()

    dog1 = Dog("Buddy", "Canine", "Golden Retriever")
    print(dog1)
    dog1.speak()

    print(Animal.all_animals)

