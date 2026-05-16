# Day 17 - 100 Days of Code

# Custom Class
class User:
    # pass # Keyword to bypass Indentation
    def __init__(self, id, name): # Constructor
        self.id = id
        self.name = name
        self.followers = 0 # Default
        self.following = 0
    
    def follow(self, user): # Method
        user.followers += 1
        self.following += 1

user_one = User('007', 'Bond')
# user_one.id = '007'
# user_one.name = 'Bond'
user_two = User('002', 'Fairbanks')

print(f"\nName : {user_one.name} | ID : {user_one.id} | Followers : {user_one.followers}")

user_one.follow(user_two)

print(f"\nFollowers : {user_one.followers} & {user_two.followers} | Following : {user_one.following} & {user_two.following} , respectively")