import random
import string


def generate_password(length=10):
    # Define character sets
    letters = string.ascii_letters  # a-z + A-Z
    digits = string.digits  # 0-9
    symbols = string.punctuation # !@#$% etc.

    # Combine all characters
    combine = letters + digits + symbols

    # Generate random password
    password = ''.join(random.choice(combine) for _ in range(length))
    return password


# Generate and display the password
print("Generated Password:", generate_password())