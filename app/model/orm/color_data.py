from sqlalchemy import Column, Integer, String, Boolean

from . import Database


class ColorData(Database.Base):
    __tablename__ = 'color'
    id: Column[Integer] = Column(Integer, primary_key=True)
    name: Column[String] = Column(String, default='')
    on_delete: Column[Boolean] = Column(Boolean, default=False)
