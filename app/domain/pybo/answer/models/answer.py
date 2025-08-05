from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from databases.mysql.base import Base, TimestampMixin


class Answer(Base, TimestampMixin):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"))
    question = relationship("Question", backref="answers")