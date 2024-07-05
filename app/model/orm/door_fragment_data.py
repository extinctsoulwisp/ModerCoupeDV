from sqlalchemy import Column, Integer, ForeignKey, Boolean, SMALLINT
from sqlalchemy.orm import relationship

from . import Database, MaterialData


class DoorFragmentData(Database.Base):
    __tablename__ = 'door_fragment'

    id: Column[Integer] = Column(Integer, primary_key=True)
    x: Column[SMALLINT] = Column(SMALLINT, nullable=False)
    y: Column[SMALLINT] = Column(SMALLINT, nullable=False)
    x2: Column[SMALLINT] = Column(SMALLINT, nullable=False)
    y2: Column[SMALLINT] = Column(SMALLINT, nullable=False)

    material_id: Column[Integer] = Column(Integer, ForeignKey("material.id"), nullable=True)
    fragment_container_id: Column[Integer] = Column(Integer, ForeignKey("door_fragment.id"), nullable=True)
    door_id: Column[Integer] = Column(Integer, ForeignKey("door.id", ondelete='CASCADE'), nullable=False)

    material = relationship(MaterialData, lazy='joined')
    fragment_container = relationship("DoorFragmentData", remote_side=[id])
