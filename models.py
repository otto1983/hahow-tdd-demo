from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, DATETIME
from datetime import datetime

Base = declarative_base()


class Board(Base):
    __tablename__ = "board"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(64))
    created_time: datetime = Column(DATETIME)