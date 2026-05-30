# Day 26 - 100 Days of Code

import pandas

print(f"\n---- NATO ^ Alphabet ----\n")

data = pandas.read_csv('nato_phonetics.csv')
# print(data)
# print(data.to_dict())

phonetics = {row.letter: row.code for (_, row) in data.iterrows()}
# print(phonetics)

word = input("\nEnter a word : ").upper()
equiv = [phonetics[letter] for letter in word]
print(f'NATO Equivalence : {equiv}')