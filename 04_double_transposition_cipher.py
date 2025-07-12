import math 

def encrypt_transposition(plain_txt, w):
    # remove spaces
    # plain_txt = plain_txt.replace(" ", "")

    # pad with '_' if not divisible by width
    while len(plain_txt) % w != 0: 
        plain_txt += '_'

    # break into rows
    rows = [plain_txt[i:i+w] for i in range(0, len(plain_txt), w)]

    # read column-wise
    cipher_txt = ''
    for col in range(w):
        for row in rows: 
            cipher_txt += row[col]
    return cipher_txt

def decrypt_transposition(cipher_txt, w):
    total_chars = len(cipher_txt)
    h = math.ceil(total_chars / w)

    # Calculate number of full-height columns
    num_full_cols = total_chars % w
    if num_full_cols == 0:
        num_full_cols = w

    cols = []
    start = 0
    for i in range(w):
        col_height = h if i < num_full_cols else h - 1
        cols.append(cipher_txt[start:start + col_height])
        start += col_height

    # Reconstruct row-wise
    plain_txt = ''
    for i in range(h):
        for col in cols:
            if i < len(col):
                plain_txt += col[i]

    return plain_txt.rstrip('_')

def double_transposition_encryption(plain_txt, w1, w2=0):
    if w2 == 0: 
        w2 = w1
    first_pass = encrypt_transposition(plain_txt, w1)
    # print("\nFirst pass of Encryption: ", first_pass)
    second_pass = encrypt_transposition(first_pass, w2)

    return second_pass

def double_transposition_decryption(cipher_txt, w1, w2=0):
    if w2 == 0: 
        w2 = w1
    first_pass = decrypt_transposition(cipher_txt, w2)
    # print("\nFirst pass of Decryption: ", first_pass)
    second_pass = decrypt_transposition(first_pass, w1)

    return second_pass

# w = int(input())

w = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15]

for width in w: 
        
    plain_text = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING UNIVERSITY OF RAJSHAHI BANGLADESH"

    # print("\nOriginal Plain text: ", plain_text)
    encrypted = double_transposition_encryption(plain_text, width)
    # print("Encrypted: ", encrypted)

    decrypted = double_transposition_decryption(encrypted, width)
    # print("Decrypted: ", decrypted)

    if plain_text == decrypted:
        print(f"Width:{width} OK!")
    else:
        print(f"Width: {width} ERROR!")
