from .orm import CustomerModel, Database


class Customer:
    def __init__(self, model: CustomerModel):
        self._model: CustomerModel = model

    @property
    def id(self):
        return self._model.id

    @property
    def name(self):
        return self._model.name

    def change_model_from_id(self, customer_id: int):
        with Database.Session() as session:
            self._model = session.query(CustomerModel).filter_by(id=customer_id).first()

    @staticmethod
    def add_to_db(name: str):
        with Database.Session() as session:
            session.add(CustomerModel(name=name))
            session.commit()

    def get_model_to_save(self):
        return self._model

