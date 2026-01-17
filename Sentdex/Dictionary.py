# Dictionaries
dict = { "Age": 22, "Rank": "Gold" } # Key => Value mapping | Keys must be unique & mutable
print(type(dict)) # <class 'dict'>
print(dict) # {'Age': 22, 'Rank': 'Gold'}

print(dict["Age"]) # 22

dict["Peak"] = "Iron"
print(dict) # {'Age': 22, 'Rank': 'Gold', 'Peak': 'Iron'}