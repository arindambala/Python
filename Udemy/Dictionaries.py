# Day 9 - 100 Days of Code

# Secret Auction
print(f"\n---- Welcome to the Anonymous Auction! ----")

'''prog_dict = {
    'Bug': "An error that prevents code to run as expected.",
    'Function': "A peice of code that one can call over & over again.",
    'Loop': "An action of doing something repeatedly.",
}

print(prog_dict)
print(prog_dict['Bug'])
# print(prog_dict['Bog']) | KeyError

prog_dict['Object'] = "An instance of a class."
print(prog_dict)
print(prog_dict['Object'])
# emp_dict = {}

prog_dict['Bug'] = "A moth in a computer."
print(prog_dict)

for _ in prog_dict:
    print(_) # Keys
    print(prog_dict[_]) # Values '''

''' capitals = {
    'France': "Paris",
    'Germany': "Berlin",
}

travel_log = {
    'France': ["Paris", "Lille", "Dijon"],
    'Germany': ["Stuttgart", "Berlin", "Hamburg"],
} # Nested List in Dictionary

print(travel_log['France'][1]) # Lille

# nested_list = ['A', 'B', ['C', 'D']] # 2-D List
# print(nested_list[2][1]) # D

travel_logged = {
    'France': {
        "Times Visited": 12,
        "Cities Visited": ["Paris", "Lille", "Dijon"]
    },
    'Germany': {
        "Times Visited": 5,
        "Cities Visited": ["Stuttgart", "Berlin"],
    },
}

print(travel_logged['Germany']["Cities Visited"][0]) # Stuttgart '''

def the_highest_bidder(bids_dict):
    won = ""
    highest_bid = 0
    for bidder in bids_dict:
        bid_amount = bids_dict[bidder]
        
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            won = bidder
    
    print(f"\n\n____ The highest bidder was {won} with a bid of ${highest_bid} ! ____")

bids = {} # Empty Dictionary

bid_continue = True
while bid_continue:
    name = input("\n\nThy name? : ")
    price = int(input("\nThy bid? : $"))
    bids[name] = price
    
    should_continue = input("\n\nAny more bidders? (yes | no) : ").lower()
    
    if should_continue == 'no':
        bid_continue = False
        the_highest_bidder(bids)
    elif should_continue == 'yes':
        print("\n" * 3)
    else:
        print("\n\n____ INVALID! Please provide the appropriate option! ____")