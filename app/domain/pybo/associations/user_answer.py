from sqlalchemy import Column, ForeignKey, Integer, Table

from databases.mysql.base import Base


answer_voter = Table(
    'answer_voters',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('answer_id', Integer, ForeignKey('answers.id'), primary_key=True)
)