def generate_random_key_file(filename, length):
    import random
    key = ''.join(chr(random.randint(0, 255)) for _ in range(length))
    with open(filename, 'wb') as f:  # Write as binary
        f.write(key.encode('latin1'))  # Use latin1 to preserve byte values
    print(f"Generated {length}-char random key to '{filename}'")

def load_random_key(filename, length):
    with open(filename, 'rb') as f:
        key_bytes = f.read(length)
        if len(key_bytes) < length:
            raise ValueError("Random key is too short.")
        return key_bytes.decode('latin1')  # decode as latin1 to preserve 1:1 byte mapping

def otp_encrypt_unicode(plaintext, key):
    ciphertext = ''
    for p, k in zip(plaintext, key):
        c_val = (ord(p) + ord(k)) % 256
        ciphertext += chr(c_val)
    return ciphertext

def otp_decrypt_unicode(ciphertext, key):
    plaintext = ''
    for c, k in zip(ciphertext, key):
        p_val = (ord(c) - ord(k) + 256) % 256
        plaintext += chr(p_val)
    return plaintext

# === Example Usage ===
if __name__ == "__main__":
    plaintext = "Hello, World! -- 123"  # Unicode characters

    key_file = "unicode_key.bin"
    generate_random_key_file(key_file, len(plaintext))

    key = load_random_key(key_file, len(plaintext))

    print("Plaintext: ", plaintext)
    print("Key Used (raw bytes):", list(ord(c) for c in key))

    cipher = otp_encrypt_unicode(plaintext, key)
    print("Cipher (encoded repr):", cipher.encode('latin1'))  # shows raw byte values

    recovered = otp_decrypt_unicode(cipher, key)
    print("Recovered: ", recovered)
