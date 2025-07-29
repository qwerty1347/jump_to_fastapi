from app.domain.pybo.models.user import User


class UserRepository():
    def __init__(self):
        pass


    async def create_user(self, db, create_dto) -> User:
        """
        User를 생성하는 비동기 메서드

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - create_dto (dict): User 생성을 위한 폼 데이터를 전달합니다.

        반환값:
        - User: 생성된 User 하나가 포함된 성공 응답을 반환합니다.
        """
        user = User(**create_dto)
        db.add(user)
        await db.flush()
        await db.refresh(user)
        return user