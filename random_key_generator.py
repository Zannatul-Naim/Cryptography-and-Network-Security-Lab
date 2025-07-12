import random
import string

def generate_random_key_file(filename, length):
    # Create a string of random uppercase letters
    key = ''.join(random.choices(string.ascii_uppercase, k=length))
    
    # Write the key to file
    with open(filename, 'w') as f:
        f.write(key)
    
    print(f"Random key of length {length} saved to '{filename}'.")

# Example: generate a key of 1 million letters
generate_random_key_file("random_key.txt", 1000000)
