from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from databases.mysql.base import Base, TimestampMixin

from app.domain.pybo.associations import answer_voter


class Answer(Base, TimestampMixin):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"))
    question = relationship("Question", backref="answers")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="answer_users")
    voter = relationship("User", secondary=answer_voter, backref="answer_voters", lazy="selectin")