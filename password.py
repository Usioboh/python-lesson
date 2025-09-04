import random

let = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
sym = "!@#$%^&*?"

characters = let + num + sym

len = int(input("Enter password length: "))

password = ""
for i in range(len):
    password += random.choice(characters)

print("Your password is:", password)
