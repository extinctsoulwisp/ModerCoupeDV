from .orm import MaterialData, Database


class Material:
    def __init__(self, model: MaterialData):
        self._model: MaterialData = model

    @property
    def name(self):
        return self._model.name

    @property
    def is_have_sealant(self):
        return self._model.name

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    def change_model_from_id(self, material_id: int):
        with Database.Session() as session:
            self._model = session.query(MaterialData).filter_by(id=material_id).first()

    @staticmethod
    def add_to_db(name: str, is_have_sealant: bool):
        with Database.Session() as session:
            session.add(MaterialData(name=name, is_have_sealant=is_have_sealant))
            session.commit()
