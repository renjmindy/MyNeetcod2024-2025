class Events:
    def __init__(self):
        self.events = list()
        
    def log_event(self, event):
        self.events.append(event)
        print(f"Event: {self.events}")

class Users:
    def __init__(self):
        self.users = list()
        self.evt = Events()

    def add_user(self, username, password):
        #global users
        user = {'username': username, 'password': password}
        self.users.append(user)
        self.evt.log_event(f"New user added: {username}")

    def update_password(self, username, new_password):
        #global users
        for user in self.users:
            if user['username'] == username:
                user['password'] = new_password
                self.evt.log_event(f"Password change for user: {username}")
                return
        print(f"User {username} not found")

    def display_user_info(self, username):
        for user in self.users:
            if user['username'] == username:
                print(f"Username: {username}")
                return
        print(f"User {username} not found")

    def remove_user(self, username):
        #global users
        user_to_remove = next((user for user in self.users if user['username'] == username), None)
        if user_to_remove:
            self.users.remove(user_to_remove)
            self.evt.log_event(f"User removed: {username}")
        else:
            print(f"No user found with username: {username}")

# Example usage of the merged and non-refactored code
users = Users()
users.add_user("Alice123", "password1")
users.add_user("Bob456", "password2")

users.display_user_info("Alice123")
users.update_password("Alice123", "new_password1")
users.remove_user("Alice123")
users.remove_user("UnknownUser")
