import itertools
import string

# Function to generate all possible combinations of characters
def generate_combinations(characters, length):
    return itertools.product(characters, repeat=length)

# Function to check if the combination matches the target password
def crack_password(target_password):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    for length in range(1, 9):  # Searching password lengths from 1 to 8
        for combo in generate_combinations(characters, length):
            guess = ''.join(combo)
            print(f"Trying: {guess}")
            if guess == target_password:
                return f"Password found: {guess}"
    return "Password not found within the given length range"

# Example usage
if __name__ == "__main__":
    target_password = input("Enter the target password: ")
    result = crack_password(target_password)
    print(result)
