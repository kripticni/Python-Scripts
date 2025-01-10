from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

data = input('Insert the data: ')
key = input('Insert the key: ')
nonce = input('Insert the nonce: ')

cipher = AES.new(key.encode(), AES.MODE_EAX, nonce.encode())
print(unpad(cipher.decrypt(data.encode()), AES.block_size).decode())
