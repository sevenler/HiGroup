from core.models.base import install_model
from core.models.user import *
from core.models.group import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from tornado.options import define, options
from config import DEBUG, DB_PATH


define("debug", default=DEBUG, type=bool)
define("db_path", default=DB_PATH, type=str)

engine = create_engine(
    options.db_path, convert_unicode=True, echo=options.debug
)

install_model(engine)
session = scoped_session(sessionmaker(bind=engine))

__all__ = [engine, session]
