# TODO: Implement support for SMS and Push notifications, not changing the default method's behavior to keep backward compatibility

class NotificationService:
    def send_notification(self, message, recipient, notification_type=None):
        # Simulates sending an email
        #print(f"Sending email to {recipient}: {message}")
        if notification_type is not None: 
            notification_type.send_notification(message, recipient)
        else: 
            # Simulates sending an email
            print(f"Sending email to {recipient}: {message}")
        
class EmailNotification:
    def send_notification(self, message, recipient):
        # Simulates sending an email
        print(f"Sending email to {recipient}: {message}")
        
class SMSNotification:
    def send_notification(self, message, recipient):
        # Simulates sending an email
        print(f"Sending SMS to {recipient}: {message}")
        
class PushNotification:
    def send_notification(self, message, recipient):
        # Simulates sending an email
        print(f"Sending Push Notification to {recipient}: {message}")
        
