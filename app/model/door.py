from typing import List

from .door_fragment import DoorFragment
from .func import round_size
from .orm import DoorData, CustomColSize, CustomRowSize
from .profile import Profile
from .rigel import Rigel


class Door:
    def __init__(self, model: DoorData, profile: Profile, rigel: Rigel):
        self._model: DoorData = model
        self._profile: Profile = profile
        self._rigel: Rigel = rigel

        self._fragments: List[DoorFragment] = [DoorFragment(model, profile, rigel)
                                               for model in self._model.fragments]

        for fragment in self._fragments:
            fragment.merged_fragments = self.get_merged_fragments(fragment.id)

        self._custom_cols: List[CustomColSize] = self._model.custom_cols if self._model.custom_cols is not None else []
        self._custom_rows: List[CustomRowSize] = self._model.custom_rows if self._model.custom_rows is not None else []

        self._width: int = 0 if not self._model.custom_width else self._model.custom_width
        self._height: int = 0

    def get_merged_fragments(self, fragment_container_id):
        return [fragment for fragment in self._fragments
                if fragment.fragment_container_id and fragment.model.fragment_container_id == fragment_container_id]

    def add_fragment(self, fragment: DoorFragment):
        self._fragments.append(fragment)

    @property
    def number(self):
        return self._model.number

    @property
    def id(self):
        return self._model.id

    @id.setter
    def id(self, value):
        self._model.id = value

    @property
    def is_h_main_rigel(self):
        return self._model.is_h_main_rigel

    @is_h_main_rigel.setter
    def is_h_main_rigel(self, value: bool):
        self._model.is_h_main_rigel = value

    @number.setter
    def number(self, value: int):
        self._model.number = value

    @property
    def cols_count(self):
        return self._model.cols_count

    @property
    def rows_count(self):
        return self._model.rows_count

    @cols_count.setter
    def cols_count(self, value: int):
        self._model.cols_count = value

    @rows_count.setter
    def rows_count(self, value: int):
        self._model.rows_count = value

    @property
    def custom_rows(self):
        return {row.n: row.size for row in self._custom_rows if row.size}

    @property
    def custom_cols(self):
        return {col.n: col.size for col in self._custom_cols if col.size}

    @property
    def cols(self):
        cols = [0 for _ in range(self._model.cols_count + 1)]
        for fragment in self._fragments:
            cols[fragment.x] = fragment.col_width
        return cols

    @property
    def rows(self):
        rows = [0 for _ in range(self._model.rows_count + 1)]
        for fragment in self._fragments:
            rows[fragment.y] = fragment.row_height
        return rows

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @property
    def visible_width(self):
        return round_size(self._width)

    @property
    def visible_height(self):
        return round_size(self._height)

    @property
    def custom_width(self):
        return self._model.custom_width

    def set_width(self, value, auto=True):
        self._model.custom_width = int(value * (not auto))
        self._width = value

    @property
    def fragments(self):
        return self._fragments

    @property
    def is_auto_width(self):
        return not self._model.custom_width

    @property
    def rigels(self):
        """external, internal_1, internal_2, is_horizontal, size"""
        def count_size(ex_pos, pos_1, pos_2, is_h):
            centers = self._rigel.center_width * (pos_2 - pos_1 - 1)
            if is_h:
                depth_1 = self._rigel.depth if pos_1 else self._profile.v_depth
                depth_2 = self._rigel.depth if pos_2 < self._model.cols_count else self._profile.v_depth
                size = round_size(sum(self.cols[pos_1:pos_2]) - depth_1 - depth_2 + centers)
            else:
                depth_1 = self._rigel.depth if pos_1 else self._profile.h_top_depth
                depth_2 = self._rigel.depth if pos_2 < self._model.rows_count else self._profile.h_bot_depth
                size = round_size(sum(self.rows[pos_1:pos_2]) - depth_1 - depth_2 + centers)
            return ex_pos, pos_1, pos_2, is_h, size

        horizontal, vertical = [], []
        main_sizes, sub_sizes = [], []

        for i in range(1, self._model.rows_count + 1):
            for j in range(1, self._model.cols_count + 1):
                fragment = self.fragment_at(i - 1, j - 1)

                if fragment.y2 < i < self._model.rows_count:
                    horizontal.append((i, j - 1, j, True))
                if fragment.x2 < j < self._model.cols_count:
                    vertical.append((j, i - 1, i, False))

        main, sub = (horizontal, sorted(vertical)) if self._model.is_h_main_rigel else (sorted(vertical), horizontal)
        print(main, sub)

        last_rigel = None
        for i, rigel in enumerate(main):
            if last_rigel is None:
                last_rigel = rigel
                i == len(main) - 1 and main_sizes.append(count_size(*rigel))
            elif last_rigel[0] == rigel[0] and last_rigel[2] == rigel[1]:
                last_rigel = (last_rigel[0], last_rigel[1], rigel[2], rigel[3])
                i == len(main) - 1 and main_sizes.append(count_size(*last_rigel))
            else:
                main_sizes.append(count_size(*last_rigel))
                i == len(main) - 1 and main_sizes.append(count_size(*rigel))
                last_rigel = rigel

        last_rigel = None
        for i, rigel in enumerate(sub):
            if last_rigel is None:
                last_rigel = rigel
                i == len(sub) - 1 and sub_sizes.append(count_size(*rigel))
            elif (last_rigel[0] == rigel[0] and last_rigel[2] == rigel[1] and
                    not any(map(lambda r: (last_rigel[1] < r[0] < rigel[2]) and (r[1] < rigel[0] < r[2]), main_sizes))):
                last_rigel = (last_rigel[0], last_rigel[1], rigel[2], rigel[3])
                i == len(sub) - 1 and sub_sizes.append(count_size(*last_rigel))
            else:
                sub_sizes.append(count_size(*last_rigel))
                i == len(sub) - 1 and sub_sizes.append(count_size(*rigel))
                last_rigel = rigel

        return main_sizes + sub_sizes

    def set_column_size(self, n, size):
        """ """
        for col in self._custom_cols:
            if col.n == n:
                if size:
                    col.size = size
                else:
                    self._custom_cols.remove(col)
        else:
            if size:
                self._custom_cols.append(CustomColSize(n=n, size=size))

    def fragment_at(self, y, x) -> DoorFragment:
        for fragment in self._fragments:
            if not fragment.fragment_container and fragment.x <= x <= fragment.x2 and fragment.y <= y <= fragment.y2:
                return fragment

    def set_row_size(self, n, size):
        """ """
        for row in self._custom_rows:
            if row.n == n:
                if size:
                    row.size = size
                else:
                    self._custom_rows.remove(row)
        else:
            if size:
                self._custom_rows.append(CustomRowSize(n=n, size=size))

    def update(self):
        """ """
        auto_width = ((self._width - self._profile.width - self._rigel.center_width *
                       (self._model.cols_count - 1) - sum(self.custom_cols.values())) /
                      (self._model.cols_count - len(list(self.custom_cols.keys()))))
        auto_height = ((self._height - self._profile.height - self._rigel.center_width *
                        (self._model.rows_count - 1) - sum(self.custom_rows.values())) /
                       (self._model.rows_count - len(list(self.custom_rows.keys()))))

        for fragment in self._fragments:
            fragment.width = custom_width if (custom_width := self.custom_cols.get(fragment.x)) else auto_width
            fragment.height = custom_height if (custom_height := self.custom_rows.get(fragment.y)) else auto_height
        for fragment in self._fragments:
            fragment.update()

    def get_model_to_save(self):
        self._model.fragments = [fragment.model for fragment in self._fragments]
        self._model.custom_cols = self._custom_cols
        self._model.custom_rows = self._custom_rows
        return self._model
    @property
    def model(self):
        return self._model
