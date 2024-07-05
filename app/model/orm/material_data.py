from sqlalchemy import Column, Integer, String, Boolean

from . import Database


class MaterialData(Database.Base):
    __tablename__ = 'material'
    id: Column[Integer] = Column(Integer, primary_key=True)
    name: Column[String] = Column(String, default='')
    is_have_sealant: Column[Boolean] = Column(Boolean, default=False)

    on_delete: Column[Boolean] = Column(Boolean, default=False)