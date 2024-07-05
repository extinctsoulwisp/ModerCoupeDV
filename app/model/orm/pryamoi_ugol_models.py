from sqlalchemy import Column, Integer, String, Boolean, REAL, SMALLINT

from . import Database


class Nomenclature(Database.Base):
    __tablename__ = 'puNomenclature'

    id: Column[Integer] = Column(Integer, primary_key=True)
    name: Column[String] = Column(String(250), default='')
    overlap: Column[SMALLINT] = Column(SMALLINT, default=0)
    guide: Column[REAL] = Column(REAL, default=0)
    sealant: Column[REAL] = Column(REAL, default=0)
    shlegel: Column[REAL] = Column(REAL, default=0)
    is_open: Column[Boolean] = Column(Boolean, default=True)
    v_depth: Column[REAL] = Column(REAL, default=0)
    v_width: Column[REAL] = Column(REAL, default=0)
    h_top_depth: Column[REAL] = Column(REAL, default=0)
    h_bot_depth: Column[REAL] = Column(REAL, default=0)
    h_top_width: Column[REAL] = Column(REAL, default=0)
    h_bot_width: Column[REAL] = Column(REAL, default=0)

    on_delete: Column[Boolean] = Column(Boolean, default=False)
