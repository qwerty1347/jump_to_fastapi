import os


def get_file_extension(file_name: str) -> str:
    """
    업로드 파일의 확장자명을 반환

    Args:
        file_name (str): 업로드 파일의 이름

    Returns:
        str: 업로드 파일의 확장자명
    """
    return os.path.splitext(file_name)[1].lower()[1:]


def is_valid_extension(allowed_extensions: dict, file_name: str) -> bool:
    """
    업로드 파일의 확장자가 허용된 목록인지 확인

    Args:
        allowed_extensions (dict): 허용된 확장자 목록
        file_name (str): 업로드 파일의 이름

    Returns:
        bool: 허용된 확장자 목록에 포함되어 있으면 True, 아니면 False
    """
    return get_file_extension(file_name) in allowed_extensions