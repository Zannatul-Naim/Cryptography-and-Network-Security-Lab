
def load_random_key(filename, length):
    with open(filename, 'r+') as f:
        key = f.read().strip()
        
        if len(key) < length:
            raise ValueError("file have not enough characters.")
        
        key_to_return = key[:length]
        remaining_key = key[length:]

        f.seek(0)
        f.truncate()
        f.write(remaining_key)
    
    return key_to_return


def otp_encrypt(plaintext):
    key = load_random_key("i1.txt", len(plaintext))
    ciphertext = ''
    for p, k in zip(plaintext, key):
        p_val = ord(p) - 64
        k_val = ord(k) - 64
        c_val = (p_val + k_val) % 26
        print(f"p = {p_val}, k = {k_val}, c = {c_val}")
        ciphertext += chr(c_val + 64)
    return key, ciphertext

# def otp_encrypt(plaintext):
#     key = load_random_key("i1.txt", len(plaintext))
#     ciphertext = ''
#     for p, k in zip(plaintext, key):
#         p_val = ord(p) - ord('A') + 1   # A = 1
#         k_val = ord(k) - ord('A') + 1   # A = 1
#         c_val = (p_val + k_val - 1) % 26
#         if c_val == 0:
#             c_val = 26
#         ciphertext += chr(c_val - 1 + ord('A'))  # Convert back to letter
#     return key, ciphertext



def otp_decrypt(ciphertext):
    key = load_random_key("i2.txt", len(ciphertext))
    plaintext = ''
    for c, k in zip(ciphertext, key):
        c_val = ord(c) - 64
        k_val = ord(k) - 64
        p_val = (c_val - k_val + 26) % 26
        print(f"p = {p_val}, k = {k_val}, c = {c_val}")
        plaintext += chr(p_val + 64)
    return key, plaintext

# def otp_decrypt(ciphertext):
#     key = load_random_key("i2.txt", len(ciphertext))
#     plaintext = ''
#     for c, k in zip(ciphertext, key):
#         c_val = ord(c) - ord('A') + 1
#         k_val = ord(k) - ord('A') + 1
#         p_val = (c_val - k_val + 26) % 26
#         if p_val == 0:
#             p_val = 26
#         plaintext += chr(p_val - 1 + ord('A'))
#     return key, plaintext



if __name__ == "__main__":
    plaintext = "ABC"

    print("\nPlaintext: ", plaintext)

    key1, cipher = otp_encrypt(plaintext)
    print("\n\nCiphertext:", cipher)
    print("Key Used:  ", key1)

    key2, recovered_plain_text = otp_decrypt(cipher)

    print("\n\nRecovered: ", recovered_plain_text)
    print("Key Used:  ", key2)
