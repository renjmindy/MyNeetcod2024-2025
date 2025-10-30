class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof Woof!"

class Cat(Animal):
    def make_sound(self):
        return f"Meow Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())
