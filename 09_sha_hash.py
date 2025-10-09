import hashlib

def sha_hash(text):

    # Convert text to bytes
    encoded_text = text.encode()

    # Create SHA-256 hash object
    sha_obj = hashlib.sha256(encoded_text)

    # Return hexadecimal digest
    return sha_obj.hexdigest()

if __name__ == "__main__":
    # Take user input
    user_input = input()

    # Generate hash
    result = sha_hash(user_input)

    # Display result
    print("SHA-256 hash: ", result)
