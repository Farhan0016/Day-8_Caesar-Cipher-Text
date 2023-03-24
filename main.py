#step 1

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text, shift):
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     #e.g.
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
#     cipher_text = ""
#     plain_text_length = len(plain_text)
#     print(f"Length of the plain text: {plain_text_length} characters")
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_index = (position+shift) % plain_text_length
#         cipher_text += alphabet[new_index]
#         print(f"{position} {letter} = {new_index} {alphabet[new_index]}")
#
#     print(f"The encoded text is: {cipher_text}")
#
#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#
# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# encrypt(text, shift)

#Step 2
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = (position + shift_amount)
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")
#
# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(plain_text, shift_amount):
#   #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#   #e.g.
#   #cipher_text = "mjqqt"
#   #shift = 5
#   #plain_text = "hello"
#   #print output: "The decoded text is hello"
#   plain_text_length = len(plain_text)
#   cipher_text = ""
#   print(f"Length of the plain text: {plain_text_length} characters")
#   for letter in plain_text:
#       position = alphabet.index(letter)
#       new_index = (position - shift_amount)
#       cipher_text += alphabet[new_index]
#
#   print(f"The decoded text is: {cipher_text}")
#
#
# #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == 'encrypt':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decrypt':
#     decrypt(plain_text=text, shift_amount=shift)
# else:
#     print("Invalid type of conversion")

#Step 3:
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#
# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for char in start_text:
#         # TODO-3: What happens if the user enters a number/symbol/space?
#         # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#         # e.g. start_text = "meet me at 3"
#         # end_text = "•••• •• •• 3"
#         position = alphabet.index(char)
#         new_position = (position + shift_amount) % 26
#         end_text += alphabet[new_position]
#
#     print(f"Here's the {cipher_direction}d result: {end_text}")
#
#
# # TODO-1: Import and print the logo from art.py when the program starts.
# from art import logo
# print(logo)
# # TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# # e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# # If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# # Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
# should_continue = True
#
# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#
#     # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#     # Try running the program and entering a shift number of 45.
#     # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#     # Hint: Think about how you can use the modulus (%).
#
#     caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#     result = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
#     if result == "no":
#         should_continue = False
#         print("Goodbye")


#final
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

    for letter in start_text:
        #If the letter is numbers, symblos or spaces it remains unchanged
        if letter not in alphabet:
            end_text += letter
        else:
            position = alphabet.index(letter)
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