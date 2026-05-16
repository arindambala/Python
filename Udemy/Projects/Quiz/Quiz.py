# Day 17 - 100 Days of Code

print(f"\n---- Quiz ^ Master ----\n")

# Custom Class
class User:
    # pass # Keyword to bypass Indentation
    def __init__(self, id, name): # Constructor
        self.id = id
        self.name = name
        self.followers = 0 # Default

user_one = User('007', 'Bond')
# user_one.id = '007'
# user_one.name = 'Bond'

print(f"Name : {user_one.name} | ID : {user_one.id} | Followers : {user_one.followers}")