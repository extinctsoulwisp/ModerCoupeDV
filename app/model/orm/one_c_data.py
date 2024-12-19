from enum import Enum

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, REAL, DECIMAL
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Database


class NomenclatureType(Enum):
    service = 0
    material = 1
    top_guide = 2
    bot_guide = 3
    top_movable_guide = 4
    guide_decor = 5
    plug = 6
    top_profile = 7
    bot_profile = 8
    rigel = 9
    vertical_profile = 10
    sealant = 11
    rollers = 12
    shlegel = 13


class RigelColorModel(Database.Base):
    __tablename__ = 'rigel_color'

    rigel_id: Mapped[Integer] = mapped_column(ForeignKey('rigel.id'), primary_key=True)
    color_id: Mapped[Integer] = mapped_column(ForeignKey('color.id'), primary_key=True)


class ProfileColorModel(Database.Base):
    __tablename__ = 'profile_color'

    profile_id: Mapped[Integer] = mapped_column(ForeignKey('profile.id'), primary_key=True)
    color_id: Mapped[Integer] = mapped_column(ForeignKey('color.id'), primary_key=True)


class Nomenclature1cData(Database.Base):
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, unique=True)
    one_c_id = mapped_column(String, nullable=True, index=True)
    name: Mapped[String] = mapped_column(String, nullable=True)
    price: Mapped[DECIMAL] = mapped_column(REAL, nullable=True)
    unit: Mapped[String] = mapped_column(String, nullable=True)
    category: Mapped[String] = mapped_column(String, nullable=True)
    save_as: Mapped[String] = mapped_column(String, nullable=True)

    on_delete: Column[Boolean] = Column(Boolean, default=False)


class RigelColor1cModel(Database.Base):
    __tablename__ = 'rigel_color_1c'

    rigel_id: Mapped[Integer] = mapped_column(ForeignKey('rigel.id'), primary_key=True)
    color_id: Mapped[Integer] = mapped_column(ForeignKey('color.id'), primary_key=True)

    one_c_id: Mapped[String] = mapped_column(ForeignKey(Nomenclature1cData.id), nullable=True)
    rigel: Mapped[Nomenclature1cData] = relationship(Nomenclature1cData, foreign_keys=[one_c_id], uselist=False,
                                                     lazy='joined')


class ProfileColor1cModel(Database.Base):
    __tablename__ = 'profile_color_1c'

    profile_id: Mapped[Integer] = mapped_column(ForeignKey('profile.id'), primary_key=True)
    color_id: Mapped[Integer] = mapped_column(ForeignKey('color.id'), primary_key=True)

    top_guide_2_id: Mapped[int] = mapped_column(ForeignKey(Nomenclature1cData.id), nullable=True)
    bottom_guide_2_id: Mapped[int] = mapped_column(ForeignKey(Nomenclature1cData.id), nullable=True)
    top_guide_1_id: Mapped[int] = mapped_column(ForeignKey(Nomenclature1cData.id), nullable=True)
    bottom_guide_1_id: Mapped[int] = mapped_column(ForeignKey(Nomenclature1cData.id), nullable=True)
    top_movable_guide_id: Mapped[int] = mapped_column(ForeignKey(Nomenclature1cData.id), nullable=True)
    decorative_guide_id: Mapped[int] = mapped_column(ForeignKey(Nomenclature1cData.id), nullable=True)
    plug_id: Mapped[int] = mapped_column(ForeignKey(Nomenclature1cData.id), nullable=True)
    top_horizontal_id: Mapped[int] = mapped_column(ForeignKey(Nomenclature1cData.id), nullable=True)
    bottom_horizontal_id: Mapped[int] = mapped_column(ForeignKey(Nomenclature1cData.id), nullable=True)
    vertical_id: Mapped[int] = mapped_column(ForeignKey(Nomenclature1cData.id), nullable=True)
    sealant_id: Mapped[int] = mapped_column(ForeignKey(Nomenclature1cData.id), nullable=True)
    shlegel_id: Mapped[int] = mapped_column(ForeignKey(Nomenclature1cData.id), nullable=True)
    wheels_id: Mapped[int] = mapped_column(ForeignKey(Nomenclature1cData.id), nullable=True)

    top_guide_2: Mapped[Nomenclature1cData] = relationship(Nomenclature1cData, foreign_keys=[top_guide_2_id],
                                                           uselist=False, lazy='joined')
    bottom_guide_2: Mapped[Nomenclature1cData] = relationship(Nomenclature1cData, foreign_keys=[bottom_guide_2_id],
                                                              uselist=False, lazy='joined')
    top_guide_1: Mapped[Nomenclature1cData] = relationship(Nomenclature1cData, foreign_keys=[top_guide_1_id],
                                                           uselist=False, lazy='joined')
    bottom_guide_1: Mapped[Nomenclature1cData] = relationship(Nomenclature1cData, foreign_keys=[bottom_guide_1_id],
                                                              uselist=False, lazy='joined')
    top_movable_guide: Mapped[Nomenclature1cData] = relationship(Nomenclature1cData,
                                                                 foreign_keys=[top_movable_guide_id], uselist=False,
                                                                 lazy='joined')
    decorative_guide: Mapped[Nomenclature1cData] = relationship(Nomenclature1cData, foreign_keys=[decorative_guide_id],
                                                                uselist=False, lazy='joined')
    plug: Mapped[Nomenclature1cData] = relationship(Nomenclature1cData, foreign_keys=[plug_id], uselist=False,
                                                    lazy='joined')
    top_horizontal: Mapped[Nomenclature1cData] = relationship(Nomenclature1cData, foreign_keys=[top_horizontal_id],
                                                              uselist=False, lazy='joined')
    bottom_horizontal: Mapped[Nomenclature1cData] = relationship(Nomenclature1cData,
                                                                 foreign_keys=[bottom_horizontal_id], uselist=False,
                                                                 lazy='joined')
    vertical: Mapped[Nomenclature1cData] = relationship(Nomenclature1cData, foreign_keys=[vertical_id], uselist=False,
                                                        lazy='joined')
    sealant: Mapped[Nomenclature1cData] = relationship(Nomenclature1cData, foreign_keys=[sealant_id], uselist=False,
                                                       lazy='joined')
    shlegel: Mapped[Nomenclature1cData] = relationship(Nomenclature1cData, foreign_keys=[shlegel_id], uselist=False,
                                                       lazy='joined')
    wheels: Mapped[Nomenclature1cData] = relationship(Nomenclature1cData, foreign_keys=[wheels_id], uselist=False,
                                                      lazy='joined')


class Config1cData(Database.Base):
    __tablename__ = 'config_1c'
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    config_name: Mapped[String] = mapped_column(String, nullable=True)
    config_id: Mapped[SMALLINT] = mapped_column(SMALLINT, nullable=True)
    config_value: Mapped[String] = mapped_column(String, nullable=False, default="")

    one_c_id: Mapped[String] = mapped_column(String, nullable=True)
    is_service: Mapped[Boolean] = mapped_column(Boolean, default=True)


class Customer1cData(Database.Base):
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    one_c_id = mapped_column(String, nullable=True, primary_key=True)
    name: Mapped[String] = mapped_column(String, nullable=True)

    on_delete: Column[Boolean] = Column(Boolean, default=False)


class OrderNomenclatures1cData(Database.Base):
    order_id: Mapped[int] = mapped_column(ForeignKey('order.id'), primary_key=True)
    nomenclature_id: Mapped[int] = mapped_column(ForeignKey(Nomenclature1cData.id))
    quantity: Mapped[float] = mapped_column(REAL)
    price: Mapped[float] = mapped_column(REAL)
    type: Mapped[int] = mapped_column(SMALLINT)
    is_auto_nomenclature_id: Mapped[bool] = mapped_column(Boolean, default=True)
