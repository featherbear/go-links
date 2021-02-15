from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes


def pad(data):
    length = 16 - (len(data) % 16)
    return (data + chr(length)*length).encode('utf-8')

def unpad(data):
    data = data.decode('utf-8')
    return data[:-ord(data[-1])]

# def decrypt(encrypted, key):
#     encrypted = b64decode(encrypted)
#     IV = encrypted[:16]
#     aes = AES.new(key, AES.MODE_CBC, IV)
#     return unpad(aes.decrypt(encrypted[16:]))

def generate(message, password):
    SALT = get_random_bytes(16)
    key = PBKDF2(password, SALT, 32, count=100000, hmac_hash_module=SHA256)
    aes = AES.new(key, AES.MODE_CBC, SALT)
    return b64encode(SALT + aes.encrypt(pad(message)))
