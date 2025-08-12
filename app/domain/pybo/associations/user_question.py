from sqlalchemy import Column, ForeignKey, Integer, Table

from databases.mysql.base import Base


question_voter = Table(
    'question_voters',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('question_id', Integer, ForeignKey('questions.id'), primary_key=True)
)