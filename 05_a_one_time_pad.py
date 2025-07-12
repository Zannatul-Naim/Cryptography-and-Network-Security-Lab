def load_random_key(filename, length):
    with open(filename, 'r') as f:
        key = f.read().strip()
    
    if len(key) < length:
        raise ValueError("Random key file does not contain enough characters.")
    
    return key[:length]

def otp_encrypt(plaintext, key):
    ciphertext = ''
    for p, k in zip(plaintext, key):
        p_val = ord(p) - ord('A')
        k_val = ord(k) - ord('A')
        c_val = (p_val + k_val) % 26
        ciphertext += chr(c_val + ord('A'))
    return ciphertext

def otp_decrypt(ciphertext, key):
    plaintext = ''
    for c, k in zip(ciphertext, key):
        c_val = ord(c) - ord('A')
        k_val = ord(k) - ord('A')
        p_val = (c_val - k_val + 26) % 26
        plaintext += chr(p_val + ord('A'))
    return plaintext

# === Example Usage ===
if __name__ == "__main__":
    plaintext = "UNIVERSITY OF RAJSHAHI"  # must be uppercase A–Z only
    key = load_random_key("random_key.txt", len(plaintext))

    print("Plaintext: ", plaintext)
    print("Key Used:  ", key)

    cipher = otp_encrypt(plaintext, key)
    print("Ciphertext:", cipher)

    recovered = otp_decrypt(cipher, key)
    print("Recovered: ", recovered)
