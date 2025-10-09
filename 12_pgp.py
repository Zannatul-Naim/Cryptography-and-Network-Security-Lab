from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os, base64

# Key generation
def generate_rsa_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return private_key, private_key.public_key()

# Signing 
def sign(message_bytes, priv):
    return priv.sign(message_bytes, asym_padding.PSS(
        mgf=asym_padding.MGF1(hashes.SHA256()), salt_length=asym_padding.PSS.MAX_LENGTH
    ), hashes.SHA256())

def verify(message_bytes, signature, pub):
    try:
        pub.verify(signature, message_bytes, asym_padding.PSS(
            mgf=asym_padding.MGF1(hashes.SHA256()), salt_length=asym_padding.PSS.MAX_LENGTH
        ), hashes.SHA256())
        return True
    except:
        return False

#  Hybrid encryption
def encrypt(message_bytes, recipient_pub):
    aes_key = AESGCM.generate_key(bit_length=256)
    aesgcm = AESGCM(aes_key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, message_bytes, None)
    enc_key = recipient_pub.encrypt(aes_key, asym_padding.OAEP(
        mgf=asym_padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None
    ))
    return {"enc_key": enc_key, "nonce": nonce, "ciphertext": ciphertext}

def decrypt(enc_package, recipient_priv):
    aes_key = recipient_priv.decrypt(enc_package["enc_key"], asym_padding.OAEP(
        mgf=asym_padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None
    ))
    aesgcm = AESGCM(aes_key)
    return aesgcm.decrypt(enc_package["nonce"], enc_package["ciphertext"], None)


if __name__ == "__main__":
    # Generate sender (Alice) and recipient (Bob) keys
    alice_priv, alice_pub = generate_rsa_keys()
    bob_priv, bob_pub = generate_rsa_keys()

    message = b"UNIVERSITY OF RAJSHAHI"

    # Sign message
    signature = sign(message, alice_priv)
    signed_message = signature + message  # simple concatenation

    # Encrypt signed message
    encrypted_package = encrypt(signed_message, bob_pub)

    # Bob decrypts
    decrypted = decrypt(encrypted_package, bob_priv)

    # Extract signature and message
    sig_len = 256  # RSA-2048 signature size in bytes
    received_sig = decrypted[:sig_len]
    received_msg = decrypted[sig_len:]

    # Verify signature
    valid = verify(received_msg, received_sig, alice_pub)

    print("Decrypted message:", received_msg.decode())
    print("Signature valid?", valid)
