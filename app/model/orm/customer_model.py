from sqlalchemy import Column, Integer, String, Boolean

from . import Database


class CustomerModel(Database.Base):
    __tablename__ = 'customer'

    id: Column[Integer] = Column(Integer, primary_key=True)
    name: Column[String] = Column(String(250), nullable=False)

    on_delete: Column[Boolean] = Column(Boolean, default=False)
