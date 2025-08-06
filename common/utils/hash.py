from passlib.context import CryptContext


crypt_context = CryptContext(schemes=["md5_crypt"], deprecated="auto")


def hash_context(plain: str) -> str:
    """
    평문 암호를 암호화된 암호로 변환

    매개변수:
        plain (str): 평문 암호

    반환값:
        str: 암호화된 암호
    """    
    return crypt_context.hash(plain)


def verify_context(plain: str, hashed: str) -> bool:
    """
    암호화된 암호를 평문 암호와 대조

    매개변수:
        plain (str): 평문 암호
        hashed (str): 암호화된 암호

    반환값:
        bool: 평문 암호가 일치하면 True, 아니면 False
    """    
    return crypt_context.verify(plain, hashed)