from datetime import datetime
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Text,
    ForeignKey
)

from base import BaseModel

class Group(BaseModel):
    __tablename__ = 'group'

    title = Column(String(100))
    description = Column(Text())
    max_partner_number = Column(Integer())
    joined_partner_number = Column(Integer())
    user_level_expectation = Column(Integer())
    created_user_id = Column(Integer(), ForeignKey('user.id'), nullable=False)

class GroupPartner(BaseModel):
    __tablename__= 'group_partner'

    group_id = Column(Integer(), ForeignKey('group.id'), nullable=False)
    user_id = Column(Integer(), ForeignKey('user.id'), nullable=False)

class GroupCheckIn(BaseModel):
    __tablename__ = 'group_check_in'

    group_id = Column(Integer(), ForeignKey('group.id'), nullable=False)
    user_id = Column(Integer(), ForeignKey('user.id'), nullable=False)
    checkin_datetime = Column(DateTime(), default=datetime.now)
