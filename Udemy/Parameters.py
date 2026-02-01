# Day 8 - 100 Days of Code

# Caesar Cipher
print(f"\n---- Welcome to Caesar Cipher Generator! ----")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Encryption
# def encrypt(original_text, shift_amount):
#     cipher_text = ''
    
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
    
#     print(f"\n____ Encoded text : {cipher_text} ____")

# Decryption
# def decrypt(encrypted_text, shift_amount):
#     cipher_text = ''
    
#     for letter in encrypted_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
    
#     print(f"\n____ Decoded text : {cipher_text} ____")

# Cipher
def caesar(original_text, shift_amount, endode_or_decode):
    cipher_text = ''
    
    if endode_or_decode == 'decode':
        shift_amount *= -1
    
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    
    print(f"\n\n____The {endode_or_decode}d text : {cipher_text} ! ____\n\n")

# encrypt(text, shift)
# decrypt(text, shift)

should_continue = True
while should_continue:
    direction = input("\nThe process to be done? (encode | decode) : ").lower()
    text = input("\nThe message : ").lower()
    shift = int(input("\nThe shift value for the process : "))
    
    caesar(text, shift, direction)
    
    restart = input("\nShould the process continue? (yes | no) : ").lower()
    
    if restart == 'no':
        should_continue = False
        print("\n\n____ Ight bet! Goodbye! ____\n\n")