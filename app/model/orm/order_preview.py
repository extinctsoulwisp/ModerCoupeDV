from sqlalchemy import Date, Column, String, Integer
from sqlalchemy.orm import Mapped

from app.model.orm import Database


class OrderPreview(Database.Base):
    __tablename__ = 'order_preview'

    id: Mapped = Column(Integer, primary_key=True)
    date = Column(Date)
    customer = Column(String)
    number = Column(String)
    profile = Column(String)
    description = Column(String)
