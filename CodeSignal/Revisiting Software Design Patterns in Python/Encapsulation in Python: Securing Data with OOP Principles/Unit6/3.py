# Define the Animal interface with a method `make_sound` that prints an action.
class Animal:
    def __init__(self, species):
        self._animal = species
    def make_sound(self):
        pass
# TODO: Create a class for Tiger. This class should encapsulate a species name and implement the make_sound method.
class Tiger(Animal):
    def make_sound(self):
        print(f"{self._animal} makes sound")
# TODO: Create a class for Elephant. This class should also encapsulate a species name and implement the make_sound method.
class Elephant(Animal):
    def make_sound(self):
        print(f"{self._animal} makes sound")

# Create a class named Zoo. This class should manage a list of animals. It should include methods to add animals and to make all animals in the zoo make a sound.
class Zoo:
    def __init__(self):
        self.__alist = list()
    def add_animals(self, species):
        self.__alist.append(species)
    def make_sound(self):
        for spec in self.__alist:
            spec.make_sound() 
            
# TODO: Instantiate the Zoo, add instances of Tiger and Elephant to it, and perform a sound check for all animals. Comment on your use of encapsulation and polymorphism.
zoo = Zoo()
animal_list = [Tiger("Bengal Tiger"), Elephant("African Elephant")]
for a in animal_list:
    zoo.add_animals(a)
zoo.make_sound()
