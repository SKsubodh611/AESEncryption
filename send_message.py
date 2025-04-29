from Crypto.Cipher import AES
from Crypto.PublicKey import ECC
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from pathlib import Path

receiver_public = ECC.import_key(Path("shared/keys/public_key.pem").read_text())

# Generate AES key
aes_key = get_random_bytes(32)

# Encrypt message with AES
plaintext = b"This is a secret message! I am Iron Man"
cipher = AES.new(aes_key, AES.MODE_CBC)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
iv = cipher.iv

# ECDH shared secret
sender_priv = ECC.generate(curve="P-256")
shared_point = sender_priv.d * receiver_public.pointQ
shared_secret = int(shared_point.x).to_bytes(32, 'big')

# Encrypt AES key with shared secret
cipher_wrap = AES.new(shared_secret, AES.MODE_ECB)
encrypted_key = cipher_wrap.encrypt(pad(aes_key, AES.block_size))

# Save all components
Path("shared/data").mkdir(parents=True, exist_ok=True)
Path("shared/data/message.enc").write_bytes(ciphertext)
Path("shared/data/key.enc").write_bytes(encrypted_key)
Path("shared/data/iv.bin").write_bytes(iv)
Path("shared/data/public_key.pem").write_text(sender_priv.public_key().export_key(format="PEM"))

print("📤 Encrypted message saved.")
