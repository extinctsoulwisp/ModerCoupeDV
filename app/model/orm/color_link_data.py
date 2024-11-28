from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
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

    one_c_id: Mapped[String] = mapped_column(String)
