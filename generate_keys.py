# generate_keys.py
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# --- Generate the private key ---
# The private key is the secret part, keep it safe!
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# --- Derive the public key from the private key ---
# The public key can be shared with anyone.
public_key = private_key.public_key()

# --- Save the private key to a file ---
with open("private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption() # No password protection
    ))

# --- Save the public key to a file ---
with open("public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print(" Public and private keys have been generated and saved.")
