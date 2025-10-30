# TODO: Define a class named Camera that encapsulates camera details.
class Camera:
    def __init__(self, resolution, price):
    # TODO: Initialize the class with a resolution and price. Ensure that price is not negative using encapsulation principles.
        self.__resolution = resolution
        self.set_price(price)

    # TODO: Write a getter method for the resolution.
    def get_resolution(self):
        return self.__resolution
        
    # TODO: Write a setter method for the price that checks for non-negative values before setting.
    def set_price(self, price):
        if price >= 0: self.__price = price

# Example usage:
my_camera = Camera('1080p', 250)
my_camera.set_price(300)         # Attempt to update the price to a valid non-negative value.
my_camera.set_price(-50)         # Attempt to set a negative price which should be validated against.
print(my_camera.get_resolution())# Print the resolution to verify getter method.
