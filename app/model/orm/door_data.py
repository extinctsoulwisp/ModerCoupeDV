from sqlalchemy import Column, Integer, ForeignKey, Boolean, SMALLINT
from sqlalchemy.orm import relationship

from . import Database, DoorFragmentData, CustomColSize, CustomRowSize


class DoorData(Database.Base):
    __tablename__ = 'door'

    id: Column[Integer] = Column(Integer, primary_key=True)
    cols_count: Column[SMALLINT] = Column(SMALLINT, nullable=False)
    rows_count: Column[SMALLINT] = Column(SMALLINT, nullable=False)
    number: Column[SMALLINT] = Column(SMALLINT, nullable=False)
    custom_width: Column[SMALLINT] = Column(SMALLINT, nullable=False, default=0)
    is_h_main_rigel: Column[Boolean] = Column(Boolean, nullable=False, default=True)
    order_id: Column[Integer] = Column(Integer, ForeignKey("order.id", ondelete='CASCADE'))

    fragments = relationship(DoorFragmentData, lazy='joined')
    custom_cols = relationship(CustomColSize, lazy='joined')
    custom_rows = relationship(CustomRowSize, lazy='joined')
