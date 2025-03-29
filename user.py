from datetime import datetime
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
    


    # def say_hi_user(self, user):
    #     print(f"Sending message to {user.username}: Hi {user.username} it's {self.username}")

    # def clean_email(self):
    #     self.email = self.email.lower().strip()


    # def get_email(self):
    #     print(f"Email accessed at {datetime.now()}")
    #     return self._email
    
    # def set_email(self, new_email):
    #     if "@" in new_email:
    #         self._email = new_email


user1 = User("John", " QXm0A@example.com    ", "password123")
user1.email = "jeremy@me.com"
print(user1.email)