from sqlalchemy import Column, Integer, ForeignKey, SMALLINT

from . import Database


class CustomColSize(Database.Base):
    __tablename__ = 'custom_col_size'

    id: Column[Integer] = Column(Integer, primary_key=True)
    n: Column[SMALLINT] = Column(SMALLINT, nullable=False)
    size: Column[SMALLINT] = Column(SMALLINT, nullable=False)
    door_id: Column[Integer] = Column(Integer, ForeignKey('door.id', ondelete='CASCADE'))
