from .orm import RigelData, Database


class Rigel:
    def __init__(self, model: RigelData):
        self._model: RigelData = model

    @property
    def id(self):
        return self._model.id

    @property
    def name(self):
        return self._model.name

    @property
    def depth(self):
        return self._model.depth

    @property
    def center_width(self):
        return self._model.center_width

    def change_model_from_id(self, rigel_id: int):
        with Database.Session() as session:
            self._model = session.query(RigelData).filter_by(id=rigel_id).first()

    def get_model_to_save(self):
        return self._model
