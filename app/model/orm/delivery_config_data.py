from sqlalchemy import Column, Integer, String

from . import Database


class DeliveryConfigData(Database.Base):
    __tablename__ = 'delivery_config'

    id: Column[Integer] = Column(Integer, primary_key=True)
    name: Column[String] = Column(String(250), nullable=False)
