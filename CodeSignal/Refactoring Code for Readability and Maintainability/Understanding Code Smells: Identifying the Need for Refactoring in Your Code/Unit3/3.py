# Notification class with separate methods for each notification type
class Notification:
    def send(self, something):
        #pass
        print(f"Sending {something}: {something}")
        
    #def send_email(self, message):
    #    print(f"Sending email: {message}")

    #def send_text(self, message):
    #    print(f"Sending text message: {message}")

    #def send_push(self, message):
    #    print(f"Sending push notification: {message}")

# Function to send notifications using specific methods based on type
#def send_notifications(notifications, message):
#    for notification in notifications:
#        if isinstance(notification, EmailNotification):
#            notification.send_email(message)
#        elif isinstance(notification, TextNotification):
#            notification.send_text(message)
#        elif isinstance(notification, PushNotification):
#            notification.send_push(message)

# Notification type classes just acting as placeholders for type checking
class EmailNotification(Notification):
    #def __init__(self, message):
    #    self.__message = message
    def send(self, message):
        print(f"Sending email: {message}")

class TextNotification(Notification):
    #def __init__(self, message):
    #    self.__message = message
    def send(self, message):
        print(f"Sending text message: {message}")

class PushNotification(Notification):
    #def __init__(self, message):
    #    self.__message = message
    def send(self, message):
        print(f"Sending push notification: {message}")

# List of notification objects
notifications = [
    EmailNotification(),
    TextNotification(),
    PushNotification()
]

messages = [
    "email",
    "text",
    "notice"
]

# Sending a message through different types of notifications
#send_notifications(notifications, "Your order has been shipped!")
for i, notification in enumerate(notifications):
    notification.send(messages[i])
print("Your order has been shipped!")
