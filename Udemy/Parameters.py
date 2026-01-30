# Day 8 - 100 Days of Code

# Caesar Cipher
print(f"\n---- Welcome to Caesar Cipher Generator! ----")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("\nWhat process to be done? (encode | decode) : ").lower()
text = input("\nThe message : ").lower()
shift = input("\nThe shift value for the process : ")

def encrypt(original_text, shift_amount):
    cipher_text = ''
    
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    
    print(f"\n____ Encoded text : {cipher_text} ____")

encrypt(text, shift)