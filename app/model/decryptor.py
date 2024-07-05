import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

backend = default_backend()
iterations = 100_000


def _derive_key(password: bytes, salt: bytes, iters: int = iterations) -> bytes:
    """Derive a secret key from a given password and salt"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt,
        iterations=iters, backend=backend)
    return b64e(kdf.derive(password))


def password_encrypt(message: bytes, password: bytes, iters: int = iterations) -> bytes:
    salt = secrets.token_bytes(16)
    key = _derive_key(password, salt, iters)
    return b64e(
        b'%b%b%b' % (
            salt,
            iters.to_bytes(4, 'big'),
            b64d(Fernet(key).encrypt(message)),
        )
    )


def password_decrypt(token: bytes, password: bytes) -> bytes:
    decoded = b64d(token)
    salt, iteration, token = decoded[:16], decoded[16:20], b64e(decoded[20:])
    iters = int.from_bytes(iteration, 'big')
    key = _derive_key(password, salt, iters)
    return Fernet(key).decrypt(token)


class EncryptData:
    """ file format: postgres-user;postgres-admin """

    @staticmethod
    def _write_user(password: bytes, text: bytes):
        user_encrypted, admin_encrypted = EncryptData._read()
        with open('data.bin', 'bw') as file:
            file.write(password_encrypt(text, password) + b';' + admin_encrypted.encode())

    @staticmethod
    def _write_admin(password, text: bytes):
        user_encrypted, admin_encrypted = EncryptData._read()
        with open('data.bin', 'bw') as file:
            file.write(user_encrypted.encode() + b';' + password_encrypt(text, password))

    @staticmethod
    def _read() -> (bytes, bytes):
        with open('data.bin', 'br') as file:
            return file.read().decode().split(';')

    @staticmethod
    def user_postgres_password(password: bytes):
        return password_decrypt(EncryptData._read()[0].encode(), password)

    @staticmethod
    def admin_postgres_password(password: bytes):
        return password_decrypt(EncryptData._read()[1].encode(), password)

    @staticmethod
    def change_user_password(password: bytes, new_password: bytes, new_postgres_password: bytes = None):
        if new_postgres_password is None:
            new_postgres_password = EncryptData.user_postgres_password(password)
        else:
            new_postgres_password = new_postgres_password
        EncryptData._write_user(new_password, new_postgres_password)

    @staticmethod
    def change_admin_password(password: bytes, new_password: bytes, new_postgres_password: bytes = None):
        if new_postgres_password is None:
            new_postgres_password = EncryptData.admin_postgres_password(password)
        else:
            new_postgres_password = new_postgres_password
        EncryptData._write_admin(new_password, new_postgres_password)

    @staticmethod
    def change_user_postgres_password(password: bytes, new_password: bytes):
        EncryptData._write_user(password, new_password)

    @staticmethod
    def change_admin_postgres_password(password: bytes, new_password: bytes):
        EncryptData._write_admin(password, new_password)
