import subprocess
from typing import Iterable

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

from app.data import USER, ADMIN, HOST, PORT, DATABASE


class Database:
    Session: sessionmaker
    engine: create_engine
    _Base: declarative_base = declarative_base(metadata=MetaData())
    _first_connect: bool = False

    @classmethod
    def init(cls, password, is_user=True) -> str:
        try:
            cls.engine = create_engine(f"postgresql+psycopg2://{USER if is_user else ADMIN }"
                                       f":{password.decode()}@{HOST}:{PORT}/{DATABASE}", echo=True)
            connection = cls.engine.connect()
            cls.Session = sessionmaker(bind=cls.engine)
            connection.close()
            _first_connect = True
        except Exception as e:
            return str(e)

    @classmethod
    def test_connection(cls) -> str:
        try:
            session = cls.Session()
            session.close()
        except Exception as e:
            return str(e)

    @classmethod
    def archive(cls):
        raise Exception(1)

    @classmethod
    def init_superuser(cls):
        cls.engine = create_engine(f"postgresql+psycopg2://postgres:1234@{HOST}:{PORT}/mc3", echo=True)
        connection = cls.engine.connect()
        cls.Session = sessionmaker(bind=cls.engine)
        connection.close()

    class Base(_Base):
        __abstract__ = True

        def __init_subclass__(cls, **kwargs):
            if not hasattr(cls, '__tablename__'):
                cls.__tablename__ = cls.__name__

        def __iter__(self):
            for column in type(self).__table__.columns:
                if column.name != 'id':
                    yield column.name, getattr(self, column.name)

        def __getitem__(self, key: str, *keys: str):
            """ instance['field.attached_field'] """
            obj = self
            for attr_name in key.split('.'):
                obj = obj.__getattribute__(attr_name)
            for attr_name in keys:
                obj = obj.__getattribute__(attr_name)
            return obj

        def __setitem__(self, key: str, value):
            """ instance['field.attached_field']  = value"""
            key = key.split('.')
            if len(key) == 1:
                self.__setattr__(key[0], value)
            else:
                self[*key[:-1]].__setattr__(key[-1], value)

        def all_instances(self):
            any_ = []
            for d in type(self).__dict__.keys():
                value = self.__getattribute__(d)
                if isinstance(value, Iterable):
                    for i in value:
                        if hasattr(i, 'all_instances'):
                            any_ += [i, *i.all_instances()]
                if hasattr(value, 'all_instances'):
                    any_ += [value, *value.all_instances()]
            return any_

    @classmethod
    def init_local(cls):
        cls.engine = create_engine(f"sqlite:///modern_coupe.db")
        connection = cls.engine.connect()
        cls.Session = sessionmaker(bind=cls.engine)
        connection.close()
