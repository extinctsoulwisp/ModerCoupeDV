from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, REAL, DECIMAL
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import Mapped, mapped_column

from . import Database


class RigelColorModel(Database.Base):
    __tablename__ = 'rigel_color'

    rigel_id: Mapped[Integer] = mapped_column(ForeignKey('rigel.id'), primary_key=True)
    color_id: Mapped[Integer] = mapped_column(ForeignKey('color.id'), primary_key=True)


class ProfileColorModel(Database.Base):
    __tablename__ = 'profile_color'

    profile_id: Mapped[Integer] = mapped_column(ForeignKey('profile.id'), primary_key=True)
    color_id: Mapped[Integer] = mapped_column(ForeignKey('color.id'), primary_key=True)


class RigelColor1cModel(Database.Base):
    __tablename__ = 'rigel_color_1c'

    rigel_id: Mapped[Integer] = mapped_column(ForeignKey('rigel.id'), primary_key=True)
    color_id: Mapped[Integer] = mapped_column(ForeignKey('color.id'), primary_key=True)

    one_c_id: Mapped[String] = mapped_column(String, nullable=True)


class ProfileColor1cModel(Database.Base):
    __tablename__ = 'profile_color_1c'

    profile_id: Mapped[Integer] = mapped_column(ForeignKey('profile.id'), primary_key=True)
    color_id: Mapped[Integer] = mapped_column(ForeignKey('color.id'), primary_key=True)

    top_guide_2: Mapped[String] = mapped_column(String, nullable=True)
    bottom_guide_2: Mapped[String] = mapped_column(String, nullable=True)
    top_guide_1: Mapped[String] = mapped_column(String, nullable=True)
    bottom_guide_1: Mapped[String] = mapped_column(String, nullable=True)
    top_movable_guide: Mapped[String] = mapped_column(String, nullable=True)
    decorative_guide: Mapped[String] = mapped_column(String, nullable=True)
    plug: Mapped[String] = mapped_column(String, nullable=True)
    top_horizontal: Mapped[String] = mapped_column(String, nullable=True)
    bottom_horizontal: Mapped[String] = mapped_column(String, nullable=True)
    vertical: Mapped[String] = mapped_column(String, nullable=True)
    sealant: Mapped[String] = mapped_column(String, nullable=True)
    shlegel: Mapped[String] = mapped_column(String, nullable=True)
    wheels: Mapped[String] = mapped_column(String, nullable=True)


class Config1cData(Database.Base):
    __tablename__ = 'config_1c'
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    config_name: Mapped[String] = mapped_column(String, nullable=True)
    config_id: Mapped[SMALLINT] = mapped_column(SMALLINT, nullable=True)
    config_value: Mapped[String] = mapped_column(String, nullable=False, default="")

    one_c_id: Mapped[String] = mapped_column(String, nullable=True)


class Nomenclature1cData(Database.Base):
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    one_c_id = mapped_column(String, nullable=True, primary_key=True)
    name: Mapped[String] = mapped_column(String, nullable=True)
    price: Mapped[DECIMAL] = mapped_column(REAL, nullable=True)
    unit: Mapped[String] = mapped_column(String, nullable=True)
    category: Mapped[String] = mapped_column(String, nullable=True)

    on_delete: Column[Boolean] = Column(Boolean, default=False)


class Customer1cData(Database.Base):
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    one_c_id = mapped_column(String, nullable=True, primary_key=True)
    name: Mapped[String] = mapped_column(String, nullable=True)

    on_delete: Column[Boolean] = Column(Boolean, default=False)