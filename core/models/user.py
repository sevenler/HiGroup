from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text
)

from sqlalchemy.orm import backref, relationship
from base import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    email = Column(String(100))
    password = Column(String(100))
    name = Column(String(100))
    description = Column(String(100))

    cell_phone = Column(String(15), index=True, unique=True)
    avatar_url = Column(String(100))
    first_login = Column(DateTime(), default=datetime.now)
    loc_uid = Column(Integer, nullable=True)

    last_login = Column(DateTime())
    is_active = Column(Boolean())
    access_token = Column(String(100))
