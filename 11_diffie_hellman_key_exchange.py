import random

# Step 1: Publicly shared prime number (p) and primitive root (g)
p = 23    # prime number
g = 5     # primitive root modulo p

print(f"Prime number (p): {p}")
print(f"Primitive root (g): {g}")

# Step 2: Each party chooses a private key (kept secret)
Xa = random.randint(2, p - 2)  # Alice's private key
Xb = random.randint(2, p - 2)  # Bob's private key

print("\nPrivate Keys (kept secret):")
print(f"Alice's private key (a): {Xa}")
print(f"Bob's private key (b): {Xb}")

# Step 3: Each party computes their public key to share
A = pow(g, Xa, p)  # Alice's public key
B = pow(g, Xb, p)  # Bob's public key


print(f"Alice's public key A = {A}")
print(f"Bob's public key B = {B}")

# Step 4: Each party computes the shared secret key
secret_key_alice = pow(B, Xa, p)  # (YA^Xa) mod p
secret_key_bob = pow(A, Xb, p)    # (YA^Xb) mod p

print("\nComputed Shared Secret Keys:")
print(f"Alice's computed key: {secret_key_alice}")
print(f"Bob's computed key:   {secret_key_bob}")

# Step 5: Both should be identical
if secret_key_alice == secret_key_bob:
    print("Exchange Successfull!")
else:
    print("Keys do not match!")
