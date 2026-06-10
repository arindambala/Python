# Day 26 - 100 Days of Code

import pandas

print(f"\n---- NATO ^ Alphabet ----\n")

data = pandas.read_csv('nato_phonetics.csv')
# print(data)
# print(data.to_dict())

phonetics = {row.letter: row.code for (_, row) in data.iterrows()}
# print(phonetics)

word = input("\nEnter a word : ").upper()
try:
    equiv = [phonetics[letter] for letter in word]
except KeyError:
    print("\nINVALID! Only aphabets allowed! \n")
else:
    print(f'NATO Equivalence : {equiv}')