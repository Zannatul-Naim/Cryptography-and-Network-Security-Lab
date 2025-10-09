import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    # Compute modular inverse of e
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def text_to_blocks(text, block_size):
    text_bytes = text.encode('utf-8')
    blocks = []
    for i in range(0, len(text_bytes), block_size):
        block = text_bytes[i:i+block_size]
        blocks.append(int.from_bytes(block, 'big'))
    return blocks

def blocks_to_text(blocks):
    text_bytes = b''.join([b.to_bytes((b.bit_length() + 7) // 8, 'big') for b in blocks])
    return text_bytes.decode('utf-8')

def encrypt_blocks(blocks, public_key):
    e, n = public_key
    return [pow(b, e, n) for b in blocks]

def decrypt_blocks(blocks, private_key):
    d, n = private_key
    return [pow(b, d, n) for b in blocks]


if __name__ == "__main__":
    p = 61
    q = 53
    public_key, private_key = generate_keys(p, q)
    e, n = public_key

    print("Public Key (e, n):", public_key)
    print("Private Key (d, n):", private_key)

    plaintext = input("\nEnter plaintext: ")

    # Determine block size so block < n
    max_bytes = max(1, (n.bit_length() // 8) - 1)
    print(f"Block size = {max_bytes} bytes")

    # Convert plaintext → blocks → encrypt → decrypt
    plain_blocks = text_to_blocks(plaintext, max_bytes)
    cipher_blocks = encrypt_blocks(plain_blocks, public_key)
    decrypted_blocks = decrypt_blocks(cipher_blocks, private_key)
    decrypted_text = blocks_to_text(decrypted_blocks)

    print("\nPlaintext Blocks:", plain_blocks)
    print("Encrypted Cipher Blocks:", cipher_blocks)
    print("Decrypted Blocks:", decrypted_blocks)
    print("Decrypted Text:", decrypted_text)
