from http import HTTPStatus
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.answer.schemas.request import AnswerQueryRequest, AnswerCreateRequest, AnswerUpdateRequest
from app.domain.pybo.answer.schemas.response import AnswerItemAffectedResponse, AnswerItemResponse
from app.domain.pybo.answer.repositories.repository import AnswerRepository
from app.domain.pybo.user.schemas.response import UserItemResponse


class AnswerService:
    def __init__(self):
        self.answer_repository = AnswerRepository()


    async def get_answers_by_question_id(self, db: AsyncSession, question_id: int) -> list[AnswerItemResponse]:
        """
        특정 질문 ID에 해당하는 answer 목록을 가져오는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - question_id (int): 특정 질문의 고유 ID를 전달합니다.

        반환값:
        - List[AnswerItemResponse]: 특정 질문에 해당하는 answer 목록이 포함된 성공 응답을 반환합니다.
        """
        response = await self.answer_repository.get_answers_by_question_id(db, question_id)
        return [AnswerItemResponse.model_validate(item) for item in response]


    async def get_answers(self, db: AsyncSession, query_dto: AnswerQueryRequest) -> list[AnswerItemResponse]:
        """
        answer 목록을 가져오는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - query_dto (AnswerQueryRequest): answer 목록을 가져올 때의
            옵션을 정의하는 데이터를 전달합니다.

        반환값:
        - List[AnswerItemResponse]: answer 목록이 포함된 성공 응답을 반환합니다.
        """
        skip = (query_dto.page - 1) * query_dto.size
        limit = query_dto.size
        response = await self.answer_repository.get_answers(db, skip, limit)

        return [AnswerItemResponse.model_validate(item) for item in response]


    async def find_answer(self, db: AsyncSession, answer_id: int) -> AnswerItemResponse:
        """
        answer 하나를 가져오는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - answer_id (int): answer 하나의 고유 ID를 전달합니다.

        반환값:
        - AnswerItemResponse: answer 하나가 포함된 성공 응답을 반환합니다.
        """
        async with db.begin():
            response = await self.answer_repository.find_answer(db, answer_id)

        if response is None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Answer not found")

        return AnswerItemResponse.model_validate(response)


    async def create_answer(self, db: AsyncSession, create_dto: AnswerCreateRequest, user: UserItemResponse) -> AnswerItemResponse:
        """
        answer 하나를 생성하는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - create_dto (AnswerCreateRequest): answer 생성을 위한 폼 데이터를 전달합니다.

        반환값:
        - AnswerItemResponse: 생성된 answer 하나가 포함된 성공 응답을 반환합니다.
        """
        data = {**create_dto.model_dump(), "user_id": user.id}

        async with db.begin():
            response = await self.answer_repository.create_answer(db, data)

        return AnswerItemResponse.model_validate(response)


    async def update_answer(self, db: AsyncSession, answer_id: int, update_dto: AnswerUpdateRequest) -> AnswerItemAffectedResponse:
        """
        answer 하나를 수정하는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - answer_id (int): answer 하나의 고유 ID를 전달합니다.
        - update_dto (AnswerUpdateRequest): answer 수정을 위한 데이터를 전달합니다.

        반환값:
        - AnswerItemAffectedResponse: 수정된 answer의 개수가 포함된 성공 응답을 반환합니다.
        """
        async with db.begin():
            response = await self.answer_repository.update_answer(db, answer_id, update_dto.model_dump())

        return AnswerItemAffectedResponse.model_validate({"rowcount": response})


    async def delete_answer(self, db: AsyncSession, answer_id: int) -> AnswerItemAffectedResponse:
        """
        answer 하나를 삭제하는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - answer_id (int): answer 하나의 고유 ID를 전달합니다.

        반환값:
        - AnswerItemAffectedResponse: 삭제된 answer의 개수가 포함된 성공 응답을 반환합니다.
        """
        async with db.begin():
            response = await self.answer_repository.delete_answer(db, answer_id)

        return AnswerItemAffectedResponse.model_validate({"rowcount": response})
