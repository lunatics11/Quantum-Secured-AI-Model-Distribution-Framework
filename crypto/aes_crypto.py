import hashlib
from cryptography.fernet import Fernet
import base64


def derive_key(shared_key):

    digest = hashlib.sha256(
        shared_key.encode()
    ).digest()

    return base64.urlsafe_b64encode(digest)


def encrypt_bytes(shared_key, data):

    key = derive_key(shared_key)

    cipher = Fernet(key)

    return cipher.encrypt(data)


def decrypt_bytes(shared_key, encrypted):

    key = derive_key(shared_key)

    cipher = Fernet(key)

    return cipher.decrypt(encrypted)