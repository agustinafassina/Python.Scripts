import string
import random

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''

    # Combine all the selected character sets
    all_chars = lowercase + uppercase + digits + special

    # Ensure at least one character set is selected
    if not all_chars:
        raise ValueError("At least one character set must be selected.")

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    password = generate_password(length=16, use_uppercase=True, use_digits=True, use_special=True)
    print("Generated password:", password)