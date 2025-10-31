# Create an interface SoundMaker with a method `make_sound` that prints an action.
class SoundMaker:
    def make_sound(self, voice):
        print(f"acting {voice}")
# Create an interface Eater with a method `eat` that prints an eating action.
class Eater:
    def eat(self):
        print("eating")
# Create a class Lion that inherits from both SoundMaker and Eater. Use encapsulation to hide the lion's name as a private attribute.
class Lion(SoundMaker, Eater):
    def __init__(self, name):
        self._name = name
# Create a Zoo class that uses composition to manage multiple animals. It should have methods to add animals and make all animals in the zoo make a sound.
class Zoo:
    def __init__(self):
        self.alist = list()
    def add_animals(self, animal):
        self.alist.append(animal)
    def make_sound(self, voice):
        for a in self.alist:
            print(f"{a._name}") 
            a.make_sound(voice)

# Instantiate the Zoo and Lion objects, add the Lion to the Zoo, and demonstrate making sounds. Remember to explain your use of encapsulation and composition in the comments.
zoo = Zoo()
lion = Lion("Tiger Lion")
zoo.add_animals(lion)
zoo.make_sound("Wow!!! Wow!!! Wow!!!")

