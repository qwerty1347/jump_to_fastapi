from http import HTTPStatus
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.question.schemas.request import QuestionCreateRequest, QuestionUpdateRequest, QuestionQueryRequest
from app.domain.pybo.question.schemas.response import QuestionItemAffectResponse, QuestionItemResponse
from app.domain.pybo.question.repositories.repository import QuestionRepository
from app.domain.pybo.user.schemas.response import UserItemResponse
from databases.mysql.session import async_session


class QuestionService():
    def __init__(self):
        self.question_repository = QuestionRepository()


    async def get_questions(self, db: AsyncSession, query_dto: QuestionQueryRequest) -> list[QuestionItemResponse]:
        """
        Question 리스트를 가져오는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - query_dto (QuestionQueryRequest): Question 리스트를 가져올 때의
            옵션을 정의하는 데이터를 전달합니다.

        반환값:
        - List[QuestionItemResponse]: Question 리스트가 포함된 성공 응답을 반환합니다.
        """
        skip = (query_dto.page - 1) * query_dto.size
        limit = query_dto.size
        response = await self.question_repository.get_questions(db, skip, limit)

        return [QuestionItemResponse.model_validate(item) for item in response]


    async def find_question(self, db: AsyncSession, question_id: int) -> QuestionItemResponse:
        """
        Question 하나를 가져오는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - question_id (int): Question 하나의 고유 ID를 전달합니다.

        반환값:
        - QuestionItemResponse: Question 하나가 포함된 성공 응답을 반환합니다.
        """
        response = await self.question_repository.find_question(db, question_id)

        if response is None:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Question not found")

        return QuestionItemResponse.model_validate(response)


    async def create_question(self, db: AsyncSession, create_dto: QuestionCreateRequest, user: UserItemResponse) -> QuestionItemResponse:
        """
        Question 하나를 생성하는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - create_dto (QuestionCreateRequest): Question 생성을 위한 폼 데이터를 전달합니다.
        - user (UserItemResponse): 사용자의 정보를 포함하는 UserItemResponse를 전달합니다.

        반환값:
        - QuestionItemResponse: 생성된 Question 하나가 포함된 성공 응답을 반환합니다.
        """
        data = {**create_dto.model_dump(), "user_id": user.id}

        async with db.begin():
            response = await self.question_repository.create_question(db, data)

        return QuestionItemResponse.model_validate(response)


    async def update_question_by_question_id(self, db: AsyncSession, question_id: int, update_dto: QuestionUpdateRequest, user: UserItemResponse) -> QuestionItemAffectResponse:
        """
        Question을 수정하는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - question_id (int): Question 하나의 고유 ID를 전달합니다.
        - update_dto (QuestionUpdateRequest): Question 수정을 위한 폼 데이터를 전달합니다.
        - user (UserItemResponse): 사용자의 정보를 포함하는 UserItemResponse를 전달합니다.

        반환값:
        - QuestionItemAffectResponse: 수정된 Question의 개수가 포함된 성공 응답을 반환합니다.
        """
        async with async_session() as db:
            question = await self.find_question(db=db, question_id=question_id)

        if question.user_id != user.id:
            raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="Forbidden user")

        async with db.begin():
            response = await self.question_repository.update_question_by_question_id(db, question_id, update_dto.model_dump(exclude_unset=True))

        return QuestionItemAffectResponse.model_validate({"rowcount": response})


    async def delete_question_by_question_id(self, db: AsyncSession, question_id: int, user: UserItemResponse) -> QuestionItemAffectResponse:
        """
        Question을 삭제하는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - question_id (int): Question 하나의 고유 ID를 전달합니다.
        - user (UserItemResponse): 사용자의 정보를 포함하는 UserItemResponse를 전달합니다.

        반환값:
         - QuestionItemAffectResponse: 삭제된 Question의 개수가 포함된 성공 응답을 반환합니다.
        """
        async with async_session() as db:
            question = await self.find_question(db=db, question_id=question_id)

        if question.user_id != user.id:
            raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="Forbidden user")

        async with db.begin():
            response = await self.question_repository.delete_question_by_question_id(db, question_id)

        return QuestionItemAffectResponse.model_validate({"rowcount": response})