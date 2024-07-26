from sqlalchemy import desc, func, String

from app.errors import Error
from .decryptor import EncryptData
from .order import Order
from .orm import UserData, OrderData, Database, CustomerModel, ProfileData, RigelData, MaterialData, ColorData
from .orm.order_preview import OrderPreview


class App:
    def __init__(self):
        self._user: UserData = UserData()

    @property
    def user_name(self):
        return self._user.name

    def login(self, password: str, user_password: str) -> str:
        """ if correct - save user data and return None, else error_text """

        # check encrypt password
        try:
            postgres_password = EncryptData.user_postgres_password(password.encode())
        except:
            return Error.WRONG_APP_PASSWORD

        # check postgres password
        if error_text := Database.init(postgres_password):
            return error_text

        # check user password
        with Database.Session() as session:
            if user := session.query(UserData).filter_by(password=user_password).first():
                self._user = user
            else:
                return Error.WRONG_USER_PASSWORD

    def create_order(self):
        with Database.Session() as session:
            session.add(OrderData(responsible_user_id=self._user.id))
            session.commit()

    @staticmethod
    def search_orders(text: str, search_by: str, _asc: bool, limit: int) -> iter:
        """ search by {'date', 'customer', 'number'}  return: id, preview_text"""

        order_by = OrderPreview.id if _asc else desc(OrderPreview.id)
        search_by = {
            'date': OrderPreview.date, 'customer': OrderPreview.customer, 'number': OrderPreview.number
        }[search_by]

        with Database.Session() as session:
            orders = session.query(OrderPreview).filter(search_by.startswith(text)).order_by(order_by).limit(limit).all()

        return orders

    @staticmethod
    def search_customers(text: str) -> iter:
        with Database.Session() as session:
            return session.query(
                CustomerModel.id, CustomerModel.name
            ).filter(CustomerModel.name.ilike(f'%{text}%'), CustomerModel.on_delete != True).all()

    @staticmethod
    def search_profiles(text: str) -> iter:
        with Database.Session() as session:
            return session.query(
                ProfileData.id, ProfileData.name
            ).filter(ProfileData.name.ilike(f'%{text}%'), ProfileData.on_delete != True).all()

    @staticmethod
    def search_rigels(text: str) -> iter:
        with Database.Session() as session:
            return session.query(
                RigelData.id, RigelData.name
            ).filter(RigelData.name.ilike(f'%{text}%'), RigelData.on_delete != True).all()

    @staticmethod
    def get_order_by_id(order_id: int) -> Order:
        with Database.Session() as session:
            return Order(
                session.query(OrderData).filter(OrderData.id == order_id).first()
            )

    @staticmethod
    def search_materials(text: str) -> iter:
        with Database.Session() as session:
            return session.query(
                MaterialData.id, MaterialData.name, MaterialData.is_have_sealant
            ).filter(MaterialData.name.ilike(f'%{text}%'), MaterialData.on_delete != True).all()

    @staticmethod
    def search_colors(text: str) -> iter:
        with Database.Session() as session:
            return session.query(
                ColorData.id, ColorData.name
            ).filter(ColorData.name.ilike(f'%{text}%'), ColorData.on_delete != True).all()
