class Logger:
    def __init__(self):
        self.version = 1
        self.messages = []
        self.len_messages = 0

    def set_version(self, version_number):
        self.version = version_number # TODO: Add validation to ensure version is either 1 or 2
        if not (self.version == 1 or self.version == 2): 
            raise ValueError
            return "Version_set: Invalid version number"

    def log(self, message):
        # If using version 2 but calling the old method, still log as per version 1.
        if self.len_messages + len(message) <= 500:
            self.len_messages += len(message)
            self.messages.append(message)
        else:
            print("Log_v1: Log size limit reached. Cannot add more messages.")

    def log_v2(self, message, severity):
        if self.version == 2:
            if self.len_messages + len(message) <= 500:
                self.len_messages += len(message)
                self.messages.append(severity+ ": " + message)
            else: print("Log_v2: Log size limit reached. Cannot add more messages.")
        else: print("Log_v2: Invalid version number")
            
    # TODO: Implement log_v2 method for version 2 functionality. This method should accept a message and a severity ("INFO", "WARNING", "ERROR")
    # and prepend the severity to the message before logging

    def get_logs(self):
        return self.messages

    # Note: Simulate the logging operation by appending messages to the self.messages list
