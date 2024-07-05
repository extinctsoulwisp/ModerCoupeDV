from sqlalchemy import Column, Integer, String

from . import Database


class SetConfigData(Database.Base):
    __tablename__ = 'set_config'

    id: Column[Integer] = Column(Integer, primary_key=True)
    name: Column[String] = Column(String(250), nullable=False)
