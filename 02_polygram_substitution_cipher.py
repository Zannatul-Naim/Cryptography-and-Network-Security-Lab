
enc_rules = {}
dec_rules = {}

with open('./polygram_blocks.txt', 'r') as file:
    content = file.read()
    words = content.split() 

for i in range(0, len(words), 2):
    enc_rules[words[i]] = words[i + 1]
    dec_rules[words[i + 1]] = words[i]


# encryption function
def encrypt(plaintxt):
    ciphertext = ""
    block = ""

    for i in range(len(plaintxt)):

        if i and i%3 == 0:
            ciphertext += enc_rules[block]
            block = ""
        block += plaintxt[i]

    ciphertext += enc_rules[block]
    return ciphertext

# decryption function
def decrypt(ciphertext):
    plaintxt = ""
    block = ""

    for i in range(len(ciphertext)):

        if i and i%3 == 0:
            plaintxt += dec_rules[block]
            block = ""
        block += ciphertext[i]

    plaintxt += dec_rules[block]
    return plaintxt

plaintext = "universityofrajshahi"
print(f"Original:  {plaintext}")    
encrypted = encrypt(plaintext)
print(f"Encrypted: {encrypted}")
decrypted = decrypt(encrypted)
print(f"Decrypted: {decrypted}")


# output:
# Original:  universityofrajshahi
# Encrypted: jhrcrnoxsdatptagkmcs
# Decrypted: universityofrajshahi