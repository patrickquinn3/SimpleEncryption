# this program is a simple encryption cipher

# libraries
import random
import string

# using the string library to import different characters
chars = '' + string.punctuation + string.digits + string.ascii_letters

# turns each character into individual element
chars = list(chars)

# uses chars as a key then shuffles the order 
key = chars.copy()
random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key  : {key}")

# ENCRYPTION
plaint_text = input("Enter a message: ")
cipher_text = ''

# iterates over ever letter in plain text, assigns random character
for letter in plaint_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f'original message: {plaint_text}')
print(f'encrypted message: {cipher_text}')

# DECRYPTION
cipher_text = input("Enter previous encrypted message: ")
plaint_text = ''

# reverse operation for encryption
for letter in cipher_text:
    index = key.index(letter)
    plaint_text += chars[index]

print(f'encrypted message: {cipher_text}')
print(f'original message: {plaint_text}')