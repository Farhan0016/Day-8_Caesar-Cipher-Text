#Caesar Cipher

#In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher,
# Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter
# some fixed number of positions down the alphabet. For example, with a right shift of 3, A would be
# replaced by D, B would become E, and so on.

#import logo from art.py
from art import logo

#ceaser function for encrypt or decrypt the plaintext
def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    #Traverse each character present in start_text
    for char in start_text:
        #If the letter is numbers, symblos or spaces it remains unchanged
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_index = (position + shift_amount) % 26
            end_text += alphabet[new_index]

    #Print the end result
    print(f"Here's the {cipher_direction}d result: {end_text}")


#declare the list of alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#print the logo from art.py when the program starts.
print(logo)

should_continue = True
while should_continue:
    #Take inputs from user
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int( input("Type the shift number:\n") )

    #Call the caeser function to encrypt or decrypt the message
    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)

    #Ask the user if they want to go again
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye")
