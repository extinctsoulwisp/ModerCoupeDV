from sqlalchemy import Column, Integer, ForeignKey, SMALLINT

from app.model.orm import Database


class OrderNumberPartData(Database.Base):
    __tablename__ = 'order_number_part'
    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    number = Column(SMALLINT, nullable=True)
