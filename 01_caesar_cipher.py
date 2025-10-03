
def caesar(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

plaintext = "UNIVERSITY OF RAJSHAHI"
print(f"Original:  {plaintext}")

encrypted = caesar(plaintext, 3)
print(f"Encrypted: {encrypted}")

decrypted = caesar(encrypted, -3)
print(f"Decrypted: {decrypted}")

# output:
# Original:  UNIVERSITY OF RAJSHAHI
# Encrypted: XQLYHUVLWB RI UDMVKDKL
# Decrypted: UNIVERSITY OF RAJSHAHI