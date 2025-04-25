from imports import *

receiver_public = ECC.import_key(Path("shared/keys/public_key.pem").read_text())

# receiver_public= ECC.import_key(Path("G:\PythonCodes\Encryption\Secure_Messenger\shared\keys\public_key.pem")).read_text()
print("nnnnnnnnnnnnn")
aes_key= get_random_bytes(32)
print(("Receiver public key: ", receiver_public))
print("aes_key",aes_key)
my_message= b"I am Iron Man !!"
cipher= AES.new(aes_key,AES.MODE_CBC)
ciphertext= cipher.encrypt(pad(my_message,AES.block_size))
print("11111111111111111111111ciphertext111111",ciphertext)
iv=cipher.iv
print("iv",iv)
sender_priv=ECC.generate(curve='P-256')
shared_point= sender_priv.