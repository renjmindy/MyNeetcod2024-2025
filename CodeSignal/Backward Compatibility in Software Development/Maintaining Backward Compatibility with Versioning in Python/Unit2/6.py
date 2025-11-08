from datetime import datetime

class Logger:
    def log(self, message, timestamp=False, tag=None, to_file=False):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if timestamp:
            message = current_time + " - " + message
        if tag:
            message = "[" + tag + "] " + message
        if to_file:
            with open("log.txt", "a") as file:
                file.write(message + "\n")
            
        # Hint: here is how you get a current date:
        

        print(message)
