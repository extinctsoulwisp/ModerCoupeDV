import enum

from sqlalchemy import Column, Integer, String, Date, func, Boolean, ForeignKey, SMALLINT
from sqlalchemy.orm import relationship

from . import Database, DeliveryConfigData, PackConfigData, SetConfigData, ProfileData, CustomerModel, RigelData, \
    DoorData, UserData, ColorData
from .order_number_part import OrderNumberPartData


class OrderData(Database.Base):
    __tablename__ = 'order'

    id: Column[Integer] = Column(Integer, primary_key=True)
    doorway_height: Column[SMALLINT] = Column(SMALLINT, nullable=False, default=500)
    doorway_width: Column[SMALLINT] = Column(SMALLINT, nullable=False, default=500)
    guide_long: Column[SMALLINT] = Column(SMALLINT, nullable=False, default=0)
    create_date: Column[Date] = Column(Date, nullable=False, default=func.current_date())
    out_date: Column[Date] = Column(Date, nullable=False, default=func.current_date())
    number: Column[SMALLINT] = Column(SMALLINT, nullable=False, default=0)
    description: Column[String] = Column(String, nullable=False, default="")
    overlap_count: Column[SMALLINT] = Column(SMALLINT, nullable=True)
    is_need_shlegel: Column[Boolean] = Column(Boolean, nullable=False, default=True)
    is_2_line: Column[Boolean] = Column(Boolean, nullable=True)
    quide_decor: Column[SMALLINT] = Column(SMALLINT, nullable=True)
    additional_materials: Column[String] = Column(String, nullable=False, default="")
    price: Column[int] = Column(Integer, default=0)

    delivery_config_id: Column[Integer] = Column(Integer, ForeignKey("delivery_config.id"), default=1)
    color_id: Column[Integer] = Column(Integer, ForeignKey("color.id"), default=1)
    pack_config_id: Column[Integer] = Column(Integer, ForeignKey("pack_config.id"), default=1)
    set_config_id: Column[Integer] = Column(Integer, ForeignKey("set_config.id"), default=1)
    profile_id: Column[Integer] = Column(Integer, ForeignKey("profile.id"), default=1)
    customer_id: Column[Integer] = Column(Integer, ForeignKey("customer.id"), default=1)
    rigel_id: Column[Integer] = Column(Integer, ForeignKey("rigel.id"), default=1)
    responsible_user_id: Column[Integer] = Column(Integer, ForeignKey("user.id"), default=1)

    delivery_config = relationship(DeliveryConfigData, lazy='joined')
    color = relationship(ColorData, lazy='joined')
    pack_config = relationship(PackConfigData, lazy='joined')
    set_config = relationship(SetConfigData, lazy='joined')
    profile = relationship(ProfileData, lazy='joined')
    customer = relationship(CustomerModel, lazy='joined')
    rigel = relationship(RigelData, lazy='joined')
    doors = relationship(DoorData, lazy='joined')
    responsible = relationship(UserData, lazy='joined')
    part_number = relationship(OrderNumberPartData, lazy='joined')
    nomenclatures = relationship('OrderNomenclatures1cData', lazy='joined', uselist=True)
