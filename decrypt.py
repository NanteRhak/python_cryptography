# decrypt.py
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# --- Load the encrypted message from the file ---
with open("ciphertext.bin", "rb") as f:
    ciphertext = f.read()

# --- Load the private key from the file ---
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None # No password was set
    )

# --- Decrypt the message ---
# The padding scheme must match the one used for encryption
decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f"Decrypted message: {decrypted_message.decode()}")
