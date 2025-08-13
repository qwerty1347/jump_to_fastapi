from app.domain.pybo.answer.models.answer import Answer
from app.domain.pybo.question.models.question import Question
from app.domain.pybo.user.models.user import User


class VoteRepository():
    def __init__(self):
        pass
    
    
    async def vote_question(self, user: User, question: Question):
        """
        특정 질문에 추천을 처리하는 비동기 서비스

        매개변수:
        - user (User): 추천을 처리하는 사용자
        - question (Question): 추천을 처리하는 Question

        반환값:
        - None: None을 반환
        """
        question.voter.append(user)
        
        
    async def vote_answer(self, user: User, answer: Answer):
        """
        특정 답변에 추천을 처리하는 비동기 서비스

        매개변수:
        - user (User): 추천을 처리하는 사용자
        - answer (Answer): 추천을 처리하는 Answer

        반환값:
        - None: None을 반환
        """
        answer.voter.append(user)