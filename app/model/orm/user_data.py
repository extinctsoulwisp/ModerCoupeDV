from sqlalchemy import Column, Integer, String, SMALLINT, Boolean

from . import Database


class UserData(Database.Base):
    __tablename__ = 'user'

    id: Column[Integer] = Column(Integer, primary_key=True)
    number: Column[SMALLINT] = Column(SMALLINT, default=0, unique=True)
    name: Column[String] = Column(String(250), default='')
    password: Column[String] = Column(String(250), default='', unique=True)
    phone: Column[String] = Column(String(20), default='')

    on_delete: Column[Boolean] = Column(Boolean, default=False)
