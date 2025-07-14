import time

from pathlib import Path
from fastapi import UploadFile

from common.constants.route import RouteConstants
from common.utils.file import get_file_extension
from config.settings import settings


async def save_file(file: UploadFile) -> Path:
    """
    주어진 업로드 파일을 저장하는 함수

    매개변수:
    - file (UploadFile): 저장할 업로드 파일

    반환값:
    - Path: 저장된 파일의 경로
    """
    contents = await file.read()
    upload_dir = Path(settings.UPLOAD_PATH) / RouteConstants.OCR.strip('/')
    file_name = f"{int(time.time())}.{get_file_extension(file.filename)}"
    file_path = upload_dir / file_name

    upload_dir.mkdir(parents=True, exist_ok=True)

    with open(file_path, 'wb') as f:
        f.write(contents)

    return file_path


async def delete_file(file_path: Path):
    """
    주어진 파일 경로의 파일을 삭제하는 함수

    매개변수:
    - file_path (Path): 삭제할 파일의 경로
    """
    if file_path.exists():
        file_path.unlink()