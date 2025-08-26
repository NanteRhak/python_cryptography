# encrypt.py
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# The message to encrypt
message = b"Your secret data goes here."

# --- Load the public key from the file ---
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# --- Encrypt the message ---
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# --- Save the encrypted message to a file ---
with open("ciphertext.bin", "wb") as f:
    f.write(ciphertext)

print(f"Original message: {message.decode()}")
print("Message encrypted and saved to 'ciphertext.bin'")
