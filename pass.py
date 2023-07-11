import string
import secrets

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter the desired password length: "))
password = generate_password(password_length)
print("Generated Password:", password)

