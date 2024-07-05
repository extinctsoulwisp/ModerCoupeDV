

from sqlalchemy.orm import declarative_base

from app.model import EncryptData, App
from app import Error
from app.model.orm import Database, UserData


class AdminApp(App):
    def __init__(self):
        super().__init__()
        self._user = UserData(name="Администратор")

    def login(self, password: bytes, user_password: bytes):
        try:
            password = EncryptData.admin_postgres_password(password)
            Database.init(password, is_user=False)
        except:
            return Error.WRONG_APP_PASSWORD

    @staticmethod
    def get_all(model: declarative_base):
        with Database.Session() as session:
            return session.query(model).all()

    @staticmethod
    def change_user_app_password(old_password: str, new_password: str):

        EncryptData.change_user_password(old_password.encode(), new_password.encode())

    @staticmethod
    def change_user_db_password(manager_password: str, new_password: str):
        EncryptData.change_user_postgres_password(manager_password.encode(), new_password.encode())

    @staticmethod
    def change_admin_app_password(old_password: str, new_password: str):
        EncryptData.change_admin_password(old_password.encode(), new_password.encode())

    @staticmethod
    def change_admin_db_password(old_password: str, new_password: str):
        EncryptData.change_admin_postgres_password(old_password.encode(), new_password.encode())

    @staticmethod
    def save(*models: declarative_base):
        with Database.Session() as session:
            for model in models:
                session.add(model)
            session.commit()

    @staticmethod
    def archive_db():
        Database.archive()
