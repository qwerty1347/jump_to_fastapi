from pathlib import Path


def get_file_extension(file_name: str) -> str:
    """
    업로드 파일의 확장자명을 반환하는 함수

    Args:
        file_name (str): 업로드 파일의 이름

    Returns:
        str: 업로드 파일의 확장자명
    """
    return Path(file_name).suffix.lstrip('.')


def is_allowed_extension(file_name: str, allowed_extensions: dict) -> bool:
    """
    업로드 파일의 확장자가 허용된 목록인지 확인하는 함수

    Args:
        file_name (str): 업로드 파일의 이름
        allowed_extensions (dict): 허용된 확장자 목록

    Returns:
        bool: 허용된 확장자 목록에 포함되어 있으면 True, 아니면 False
    """
    return get_file_extension(file_name) in allowed_extensions