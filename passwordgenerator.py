import random
import string

# take input from user
length = int(input("Enter the desired password length: "))

# characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# display result
print("Generated Password:", password)
