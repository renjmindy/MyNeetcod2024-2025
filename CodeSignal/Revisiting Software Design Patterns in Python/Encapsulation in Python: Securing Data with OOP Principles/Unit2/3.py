from abc import ABC, abstractmethod

# TODO: Define an abstract class `LightSource`
class LightSource(ABC):
    @abstractmethod
    # TODO: Define an abstract method for turning on the light source.
    def turn_on(self, source):
        pass

# TODO: Define a class `Lamp` derived from an abstract class
class Lamp(LightSource):
    # TODO: Implement the abstract method `turn_on` to turn the lamp on, returning a descriptive message.
    def turn_on(self, source):
        return f"Turn on {source}!!!"

# TODO: Create an instance of the Lamp class
lamp = Lamp()
# TODO: Call a method on the instance to call the `turn_on` method
print(lamp.turn_on('light'))
