from .orm import Database, ColorData


class Color:
    def __init__(self, model: ColorData):
        self._model: ColorData = model

    @property
    def id(self):
        return self._model.id

    @property
    def name(self):
        return self._model.name

    def change_model_from_id(self, color_id: int):
        with Database.Session() as session:
            self._model = session.query(ColorData).filter_by(id=color_id).first()

    @staticmethod
    def add_to_db(name: str):
        with Database.Session() as session:
            session.add(ColorData(name=name))
            session.commit()

    def get_model_to_save(self):
        return self._model
