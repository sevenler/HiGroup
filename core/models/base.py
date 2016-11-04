from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def install_model(engine):
    """Sync model into database, Invoked from application
    """
    Base.metadata.create_all(bind=engine)
    print "Models Installed"

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    edited_time = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    created_time = Column(DateTime(), default=datetime.now)

    def __repr__(self):
        return '<%s: %d>' % (self.__class__.__name__, self.id)

    @property
    def json(self):
        raise NotImplementedError

    def update(self, update_dict):
        [setattr(self, key, value) for key, value in update_dict.iteritems()]
