from sqlalchemy import Column, Integer, ForeignKey, Boolean, SMALLINT
from sqlalchemy.orm import relationship

from . import Database, MaterialData, Nomenclature1cData


class DoorFragmentData(Database.Base):
    __tablename__ = 'door_fragment'

    id: Column[Integer] = Column(Integer, primary_key=True)
    x: Column[SMALLINT] = Column(SMALLINT, nullable=False)
    y: Column[SMALLINT] = Column(SMALLINT, nullable=False)
    x2: Column[SMALLINT] = Column(SMALLINT, nullable=False)
    y2: Column[SMALLINT] = Column(SMALLINT, nullable=False)
    sealant_: Column[bool] = Column(Boolean, default=False)

    material_id: Column[Integer] = Column(Integer, ForeignKey("Nomenclature1cData.id"), nullable=True)
    tape_id: Column[Integer] = Column(Integer, ForeignKey("Nomenclature1cData.id"), nullable=True)

    fragment_container_id: Column[Integer] = Column(Integer, ForeignKey("door_fragment.id"), nullable=True)
    door_id: Column[Integer] = Column(Integer, ForeignKey("door.id", ondelete='CASCADE'), nullable=True)

    material = relationship(Nomenclature1cData, foreign_keys=[material_id], lazy='joined')
    tape = relationship(Nomenclature1cData, foreign_keys=[tape_id], lazy='joined')
    fragment_container = relationship("DoorFragmentData", remote_side=[id])
