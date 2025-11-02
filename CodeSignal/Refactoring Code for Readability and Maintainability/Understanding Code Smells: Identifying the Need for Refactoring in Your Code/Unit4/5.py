class Profile:
    def __init__(self, username, email):
        self.__username = username
        self.__email = email
    def display(self):
        print(f"User: {self.__username}, Email: {self.__email}")

class Authentication:
    def __init__(self, password_hash):
        self.__password = password_hash
    def authenticate(self, attempted_password_hash):
        return self.__password == attempted_password_hash
        
class Setting:
    def __init__(self, theme, notifications_enabled):
        self._theme = theme
        self._notice = notifications_enabled
    def update_theme(self, new_theme):
        self._theme = new_theme
    def toggle_notifications(self):
        self._notice = not self._notice

class User:
    def __init__(self, username, email, password_hash, theme, notifications_enabled):
        #self.username = username
        #self.email = email
        #self.password_hash = password_hash
        #self.theme = theme
        #self.notifications_enabled = notifications_enabled
        self.profile = Profile(username, email)
        self.auth = Authentication(password_hash)
        self.setting = Setting(theme, notifications_enabled)
    
    def display_profile(self):
        #print(f"User: {self.username}, Email: {self.email}")
        self.profile.display()

    def authenticate(self, attempted_password_hash):
        #return self.password_hash == attempted_password_hash
        return self.auth.authenticate(attempted_password_hash)

    def update_theme(self, new_theme):
        #self.theme = new_theme
        self.setting.update_theme(new_theme)

    def toggle_notifications(self):
        #self.notifications_enabled = not self.notifications_enabled
        self.setting.toggle_notifications()

    def display_full_user_details(self):
        print("User Details:")
        #self.display_profile()
        self.profile.display()
        print(f"Theme: {self.setting._theme}")
        self.toggle_notifications()
        print(f"Notifications Enabled: {self.setting._notice}")

USER_NAME = "JaneDoe"
USER_EMAIL = "jane@example.com"
USER_PASSWORD_HASH = "5f4dcc3b5aa765d61d8327deb882cf99" # placeholder hash for 'password'
USER_THEME = "Dark"
USER_NOTIFICATIONS_ENABLED = True

user = User(USER_NAME, USER_EMAIL, USER_PASSWORD_HASH, USER_THEME, USER_NOTIFICATIONS_ENABLED)
user.display_full_user_details()

attempted_password_hash = "5f4dcc3b5aa765d61d8327deb882cf99" # placeholder hash for 'password'
authentication_result = user.authenticate(attempted_password_hash)
print(f"Authentication successful: {user.authenticate("5f4dcc3b5aa765d61d8327deb882cf99")}")
