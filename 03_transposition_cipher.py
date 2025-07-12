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
    h = len(cipher_txt) // w

    # break into columns first
    cols = [cipher_txt[i*h:(i+1)*h] for i in range(w)]

    # read row-wise
    plain_txt = ''
    for i in range(h):
        for col in cols: 
            plain_txt += col[i]

    # remove padding if exists
    plain_txt = plain_txt.rstrip("_")

    return plain_txt

w = int(input())
plain_text = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING UNIVERSITY OF RAJSHAHI BANGLADESH"

encrypted = encrypt_transposition(plain_text, w)
print("Encrypted: ", encrypted)

decrypted = decrypt_transposition(encrypted, w)
print("Decrypted: ", decrypted)
