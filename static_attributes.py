#static attributes - are good for totals, shared constants, counters, class level configurations

class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1
    
    def display_user(self):
        print(f"Username: {self.username}. Email: {self.email}.")
    def displaty_user_count(self):
        print(f"Total number of users: {User.user_count}")


user1 = User("John", " QXm0A@example.com")
user2 = User("Jane", "lY7eO@example.com")
print(User.user_count)
print(user1.user_count)
print(user2.user_count)