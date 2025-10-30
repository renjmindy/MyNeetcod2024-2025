from abc import ABC, abstractmethod

class CommunicationDevice(ABC):
    
    @abstractmethod
    def send_message(self, content):
        # TODO: How do you implement an abstract method?
        pass

class Radio(CommunicationDevice):

    # TODO: Implement the method to send a message using radio communication
    # Hint: The method should return a string indicating the message has been sent through radio waves.
    def send_message(self, message):
        return f"Sending through radio waves: {message}"

walkie_talkie = Radio()
print(walkie_talkie.send_message("Roger that!"))
