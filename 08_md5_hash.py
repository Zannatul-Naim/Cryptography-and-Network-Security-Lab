import hashlib

# Get user input
data = input()

# Encode the string and compute MD5 hash
md5_hash = hashlib.md5(data.encode())

# Print the hexadecimal representation of the hash
print("MD5 Hash:", md5_hash.hexdigest())
