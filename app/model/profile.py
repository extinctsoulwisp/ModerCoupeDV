from .orm import ProfileData, Database


class Profile:
    def __init__(self, model: ProfileData):
        self._model: ProfileData = model

    @property
    def id(self):
        return self._model.id

    @property
    def h_top_depth(self):
        return self._model.h_top_depth

    @property
    def h_bot_depth(self):
        return self._model.h_bot_depth

    @property
    def v_depth(self):
        return self._model.v_depth

    @property
    def is_open(self):
        return self._model.is_open

    @property
    def sealant(self):
        return self._model.sealant

    @property
    def name(self):
        return self._model.name

    @property
    def width(self):
        return 2 * (self._model.v_width - self._model.v_depth)

    @property
    def v_width(self):
        return self._model.v_width

    @property
    def height(self):
        return self._model.h_bot_width + self._model.h_top_width - self._model.h_top_depth - self._model.h_bot_depth

    @property
    def overlap_width(self):
        return self._model.overlap

    @property
    def shlegel(self):
        return self._model.shlegel

    @property
    def guide(self):
        return self._model.guide

    def change_model_from_id(self, profile_id: int):
        with Database.Session() as session:
            self._model = session.query(ProfileData).filter_by(id=profile_id).first()

    def get_model_to_save(self):
        return self._model
