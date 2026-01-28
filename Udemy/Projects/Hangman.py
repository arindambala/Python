# Day 7 - 100 Days of Code

import random

# HANGMAN_STAGES = ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''']


# Hangman
word_list = ['baroque', 'boondongle', 'fastidious', 'sycophant']

print(f"\n---- Welcome to Hangman! ----")

lives = 6

chosen_word = random.choice(word_list)
print(f"\nThe word to be guessed : {chosen_word}")

placeholder = ''
word_length = len(chosen_word)

for pos in range(word_length):
	placeholder += '_'
print(placeholder)

game_over = False
correct_guess = []

while not game_over:
	guess = input("\nWhat letter makes the guess? : ").lower()
	# print(guess)

	if guess in correct_guess:
		print(f"\n____ Already guessed : {guess} ! ____")

	display = ''

	for letter in chosen_word:
		if letter == guess:
			# print("\n____ IGHT, guessed letter is in the word! ____")
			display += letter
			correct_guess.append(letter)
		elif letter in correct_guess:
			display += letter
		else:
			# print("\n____ NOPE, guessed letter is not in the word! ____")
			display += '_'

	print(display)
	
	if guess not in chosen_word:
		lives -= 1
		print(f"\n____ Already guessed : {guess} , overruled ! ____")
		if lives == 0:
			game_over = True
			print(f"\n__!__ The man has been granted : JUDAS CRADLE, for {chosen_word} __!__")
	
	if '_' not in display:
		game_over = True
		print("\n__!__ The man has been granted : CLEMENCY __!__")

	# print(HANGMAN_STAGES)