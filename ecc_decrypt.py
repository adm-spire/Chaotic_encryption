from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import padding , hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Load the recipient's private key
with open("recipient_private_key.pem", "rb") as f:
    private_key_data = f.read()
recipient_private_key = serialization.load_pem_private_key(
    private_key_data,
    password=None,
    backend=default_backend()
)

# Deserialize the encrypted key and recipient's public key
with open("encrypted_key.bin", "rb") as f:
    encrypted_key = f.read()
with open("recipient_public_key.pem", "rb") as f:
    public_key_data = f.read()
recipient_public_key = serialization.load_pem_public_key(
    public_key_data,
    backend=default_backend()
)

# Derive the shared secret using ECDH key agreement
shared_secret = recipient_private_key.exchange(ec.ECDH(), recipient_public_key)

# Derive the symmetric encryption key from the shared secret
hkdf = HKDF(
    algorithm=hashes.SHA256(),
    length=32,  # Length of the symmetric key (AES-256)
    salt=None,
    info=b'encryption key',
    backend=default_backend()
)
symmetric_key = hkdf.derive(shared_secret)

# Decrypt the encrypted data
cipher = Cipher(algorithms.AES(symmetric_key), modes.ECB(), backend=default_backend())
decryptor = cipher.decryptor()

# Unpad the decrypted data
unpadder = padding.PKCS7(128).unpadder()
decrypted_data = unpadder.update(decryptor.update(encrypted_key)) + unpadder.finalize()

# Convert the decrypted data from bytes to string
chaotic_key = decrypted_data.decode()

print("Decrypted Chaotic Key:", chaotic_key)
