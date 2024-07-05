from typing import List

from sqlalchemy.orm.exc import DetachedInstanceError

from app.model.func import round_size
from app.model.orm import DoorFragmentData, MaterialData


class DoorFragment:
    def __init__(self, model: DoorFragmentData, profile, rigel):
        from app.model import Profile, Rigel
        self._model: DoorFragmentData = model
        self._profile: Profile = profile
        self._rigel: Rigel = rigel

        self._merged_fragments: List[DoorFragment] = []

        self._height: float = 0
        self._width: float = 0
        self._number_in_scheme: int = 0

    @property
    def material(self):
        return self._model.material

    @property
    def number_in_scheme(self):
        return self._number_in_scheme

    @number_in_scheme.setter
    def number_in_scheme(self, value: int):
        self._number_in_scheme = value

    @property
    def id(self):
        return self._model.id

    @id.setter
    def id(self, value):
        self._model.id = value

    @property
    def visible_height(self):
        return round_size(self._height - self.is_have_sealant * self._profile.sealant)

    @property
    def visible_width(self):
        return round_size(self.width - self.is_have_sealant * self._profile.sealant)

    @property
    def col_width(self):
        x2 = self._model.x2
        width = self._width
        for fragment in sorted(self._merged_fragments, key=lambda f: (f.x, f.y), reverse=True):
            if fragment.x <= x2 and fragment.y == self._model.y:
                width -= fragment.width + self._rigel.center_width
                x2 = fragment.x
        return width

    @property
    def row_height(self):
        y2 = self._model.y2
        height = self._height
        for fragment in sorted(self._merged_fragments, key=lambda f: (f.y, f.x), reverse=True):
            if fragment.y <= y2 and fragment.x == self._model.x:
                height -= fragment.height + self._rigel.center_width
                y2 = fragment.y
        return height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def x(self):
        return self._model.x

    @property
    def y(self):
        return self._model.y

    @property
    def x2(self):
        return self._model.x2

    @property
    def y2(self):
        return self._model.y2

    @property
    def is_have_sealant(self):
        return self._model.material.is_have_sealant if self._model.material else False

    @property
    def material_name(self):
        return None if self._model.material is None else self._model.material.name

    @property
    def fragment_container_id(self):
        return self._model.fragment_container_id

    @fragment_container_id.setter
    def fragment_container_id(self, value: int):
        self._model.fragment_container_id = value

    @property
    def fragment_container(self):
        try:
            return self._model.fragment_container
        except DetachedInstanceError:
            return None

    @fragment_container.setter
    def fragment_container(self, value):
        self._model.fragment_container = value

    @property
    def merged_fragments(self):
        return self._merged_fragments

    @merged_fragments.setter
    def merged_fragments(self, fragments: List):
        for fragment in fragments:
            fragment.fragment_container = self._model
        self._merged_fragments = fragments

    @property
    def model(self):
        return self._model

    def set_material_model(self, model: MaterialData):
        self._model.material = model

    def merge(self, fragments: List['DoorFragment']):
        for fragment in sorted(fragments, key=lambda f: (f.y, f.x)):
            if fragment.x > self._model.x2:
                self._model.x2 = fragment.x
            if fragment.y > self._model.y2:
                self._model.y2 = fragment.y
            fragment.fragment_container_id = self._model.id
            fragment.fragment_container = self._model

        self._merged_fragments = fragments

    def unmerge(self):
        self._model.x2, self._model.y2 = self._model.x, self._model.y

        for fragment in self._merged_fragments:
            fragment.fragment_container = None
            fragment.fragment_container_id = None

        self._merged_fragments.clear()

    def update(self):
        x2, y2 = self._model.x, self._model.y
        for fragment in sorted(self._merged_fragments, key=lambda f: (f.y, f.x)):
            if fragment.x > x2:
                self.width += fragment.width + self._rigel.center_width
                x2 = fragment.x
            if fragment.y > y2:
                self.height += fragment.height + self._rigel.center_width
                y2 = fragment.y
