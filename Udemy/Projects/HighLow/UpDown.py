# Day 14 - 100 Days of Code

import random
from Data import data
# from Art import logo, vs

# print(logo)
print(f"\n---- Welcome to Higher or Lower! ----\n")

def format_data(account):
    """ Takes the account data and returns the printable format """
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_ans(player_guess, a_followers, b_followers):
    """ Takes a player's guess and the follower count to return if they got it correctly """
    if a_followers > b_followers:
        return player_guess == 'a'
    else:
        return player_guess == 'b'

score = 0
cont_game = True
account_b = random.choice(data)

while cont_game:
    print("\n")
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}. ")
    # print(vs)
    print(f"Against B : {format_data(account_b)}. ")

    guess = input("\nWhich account has more followers? (A | B) : ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_ans(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"\n|> LESSSGOO! You're correct! ~ CURRENT SCORE : {score} ")
    else:
        print(f"\n|> NOPE! That's incorrect! ~ FINAL SCORE : {score} ")
        cont_game = False