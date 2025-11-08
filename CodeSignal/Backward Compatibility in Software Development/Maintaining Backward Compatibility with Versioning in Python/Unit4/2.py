class EmailNotifier:
    def send_email(self, recipient, message):
        return f"Sending email to {recipient}: {message}"

class SMSNotifier:
    def send_sms(self, phone_number, message):
        return f"Sending SMS to {phone_number}: {message}"

class NotificationAdapter:
    def __init__(self):
        self.email = EmailNotifier()
        self.sms = SMSNotifier()
        
    def send_notification(self, identifier, message):
        # TODO: Implement this method to use SMSNotifier or EmailNotifier 
        # depending on whether the identifier is a phone number or an email.
        #pass
        if identifier.isnumeric():
            return self.sms.send_sms(identifier, message)
        else:
            return self.email.send_email(identifier, message)
