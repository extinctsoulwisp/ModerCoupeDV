from sqlalchemy import Column, Integer, String, REAL, Boolean

from . import Database


class RigelData(Database.Base):
    __tablename__ = 'rigel'

    id: Column[Integer] = Column(Integer, primary_key=True)
    name: Column[String] = Column(String, default='')
    center_width: Column[REAL] = Column(REAL, default=0)
    depth: Column[REAL] = Column(REAL, default=0)

    on_delete: Column[Boolean] = Column(Boolean, default=False)
