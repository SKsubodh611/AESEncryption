from Crypto.Cipher import AES
from Crypto.PublicKey import ECC
from Crypto.Util.Padding import unpad
from pathlib import Path

# Load keys
receiver_priv = ECC.import_key(Path("shared/keys/private_key.pem").read_text())
sender_pub = ECC.import_key(Path("shared/data/public_key.pem").read_text())

# ECDH shared secret
shared_point = receiver_priv.d * sender_pub.pointQ
shared_secret = int(shared_point.x).to_bytes(32, 'big')

# Decrypt AES key
encrypted_key = Path("shared/data/key.enc").read_bytes()
cipher_unwrap = AES.new(shared_secret, AES.MODE_ECB)
aes_key = unpad(cipher_unwrap.decrypt(encrypted_key), AES.block_size)

# Decrypt message
iv = Path("shared/data/iv.bin").read_bytes()
ciphertext = Path("shared/data/message.enc").read_bytes()
cipher = AES.new(aes_key, AES.MODE_CBC, iv=iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print("🔓 Decrypted message:", plaintext.decode())
