import random
import string

def generate_random_password(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by sampling characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if _name_ == "_main_":
    try:
        length = int(input("Enter the length of the password: "))
        if length < 1:
            print("Password length must be at least 1.")
        else:
            password = generate_random_password(length)
            print("Generated password:", password)
    except ValueError:
        print("Please enter a valid integer for the password length.")
