from http import HTTPStatus
from fastapi import HTTPException, UploadFile

from common.utils.file import is_allowed_extension

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'pdf'}

def validate_upload_file(file: UploadFile):
    """
    업로드 파일을 확인하고, 허용된 확장자 목록(ALLOWED_EXTENSIONS) 내에 존재하는지 확인하는 함수

    Args:
        file (UploadFile): 업로드할 파일

    Raises:
        HTTPException: 파일이 허용되지 않은 경우
    """
    if not is_allowed_extension(file.filename, ALLOWED_EXTENSIONS):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="지원하지 않는 파일입니다.")