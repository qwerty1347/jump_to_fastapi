from passlib.context import CryptContext


crypt_context = CryptContext(schemes=["md5_crypt"], deprecated="auto")


def hash_context(plain: str) -> str:
    return crypt_context.hash(plain)


def verify_context(plain: str, hashed: str) -> bool:
    return crypt_context.verify(plain, hashed)