from typing import List

from app.model import Color
from app.model.customer import Customer
from app.model.door import Door
from app.model.orm import OrderData, Database, DoorData, DoorFragmentData, MaterialData, CustomColSize, CustomRowSize, \
    OrderNumberPartData, DeliveryConfigData, SetConfigData, PackConfigData
from app.model.profile import Profile
from app.model.rigel import Rigel


class Order:
    def __init__(self, model: OrderData):
        self._model: OrderData = model

        self._profile: Profile = Profile(self._model.profile)
        self._rigel: Rigel = Rigel(self._model.rigel)
        self._customer: Customer = Customer(self._model.customer)
        self._color: Color = Color(self._model.color)
        self._doors: List[Door] = sorted(
            [Door(model, self._profile, self._rigel) for model in self._model.doors],
            key=lambda door: door.number
        )
        self._deleted_materials: set[MaterialData] = set()

    @property
    def id(self):
        return self._model.id

    @property
    def responsible(self):
        return self._model.responsible

    @property
    def part_number(self):
        return self._model.part_number[0].number if self._model.part_number else None

    @part_number.setter
    def part_number(self, value: int):
        if self._model.part_number:
            self._model.part_number[0].number = value
        else:
            self._model.part_number.append(OrderNumberPartData(number=value))

    @property
    def color(self):
        return self._model.color

    @property
    def delivery_config_name(self):
        with Database.Session() as session:
            return session.query(DeliveryConfigData.name).filter(
                DeliveryConfigData.id == self._model.delivery_config_id).first()[0]

    @property
    def set_config_name(self):
        with Database.Session() as session:
            return session.query(SetConfigData.name).filter(
                SetConfigData.id == self._model.set_config_id).first()[0]

    @property
    def pack_config_name(self):
        with Database.Session() as session:
            return session.query(PackConfigData.name).filter(
                PackConfigData.id == self._model.pack_config_id).first()[0]

    @property
    def doors(self):
        return self._doors

    @property
    def set_config_id(self):
        return self._model.set_config_id

    @property
    def delivery_config_id(self):
        return self._model.delivery_config_id

    @property
    def pack_config_id(self):
        return self._model.pack_config_id

    @property
    def door_count(self):
        return len(self._doors)

    @property
    def doorway_height(self):
        return self._model.doorway_height

    @property
    def doorway_width(self):
        return self._model.doorway_width

    @property
    def guide_long(self):
        return self._model.guide_long

    @property
    def create_date(self):
        return self._model.create_date

    @property
    def out_date(self):
        return self._model.out_date

    @property
    def number(self):
        return self._model.number

    @property
    def visible_number(self):
        return (f"{self._model.responsible.number}"
                f"{'0' * (3 - len(str(self._model.number)))}{self._model.number}"
                f"{f'/{self.part_number}' if self.part_number else ''}")

    @property
    def description(self):
        return self._model.description

    @property
    def profile_color(self):
        return self._color

    @property
    def overlap_count(self):
        return self._model.overlap_count

    @property
    def need_shlegel(self):
        return self._model.is_need_shlegel

    @property
    def is_2_line(self):
        return self._model.is_2_line

    @property
    def additional_materials(self):
        return self._model.additional_materials

    @property
    def grouped_rigels(self):
        rigels = {}
        for rigel in [r for door in self._doors for r in door.rigels]:
            if rigels.get(rigel[4]) is None:
                rigels[rigel[4]] = 1
            else:
                rigels[rigel[4]] += 1
        return rigels

    def create_door(self, cols_c: int, rows_c: int) -> Door:
        door_model = DoorData(
            cols_count=cols_c, rows_count=rows_c, number=len(self._doors), custom_width=0, is_h_main_rigel=True)
        for i in range(rows_c):
            for j in range(cols_c):
                door_model.fragments.append(DoorFragmentData(
                    x=j, y=i, x2=j, y2=i
                ))
        new_door = Door(door_model, self._profile, self._rigel)
        self._doors.append(new_door)
        return new_door

    @property
    def quide_decor(self):
        return self._model.quide_decor

    def delete_door(self, door: Door):
        for fragment in door.fragments:
            if fragment.material:
                self._deleted_materials.add(fragment.material)

        if door.model in self._model.doors:
            self._model.doors.remove(door.model)
        self._doors.remove(door)

        for i, door in enumerate(self._doors):
            door.number = i

    def update(self):
        if not len(self._doors):
            return

        overlap_count = len(self._doors) - 1 if self._model.overlap_count is None else self._model.overlap_count
        custom_size_doors = [door.width for door in self._doors if not door.is_auto_width]

        auto_door_width = (self._model.doorway_width + overlap_count * self._profile.overlap_width -
                           self._model.is_need_shlegel * len(self._doors) * self._profile.shlegel -
                           sum(custom_size_doors)) // (len(self._doors) - len(custom_size_doors))

        new_door_height = self._model.doorway_height - self._profile.guide

        for door in self._doors:
            if door.is_auto_width:
                door.set_width(auto_door_width)
            door.height = new_door_height
            door.update()

        self.group_fragments()

    def group_fragments(self):
        group_fragments = {}
        door_fragments = [fragment for door in self._doors for fragment in door.fragments
                          if not fragment.fragment_container]
        sorted_fragment_number = 1

        for fragment in door_fragments:
            if group_fragments.get(fragment.material_name) is None:
                group_fragments[fragment.material_name] = {}
            if group_fragments[fragment.material_name].get((fragment.visible_height, fragment.visible_width)) is None:
                group_fragments[fragment.material_name][(fragment.visible_height, fragment.visible_width)] = \
                    [1, sorted_fragment_number]
                fragment.number = sorted_fragment_number
                sorted_fragment_number += 1
            else:
                group_fragments[fragment.material_name][(fragment.visible_height, fragment.visible_width)][0] += 1
            fragment.number_in_scheme = group_fragments[fragment.material_name][(fragment.visible_height,
                                                                                 fragment.visible_width)][1]

        return group_fragments

    def save_in_db(self):
        self._model.doors = [door.get_model_to_save() for door in self._doors]
        self._model.rigel = self._rigel.get_model_to_save()
        self._model.profile = self._profile.get_model_to_save()
        self._model.customer = self._customer.get_model_to_save()
        self._model.color = self._color.get_model_to_save()

        with Database.Session() as session:
            session.add(self._model)
            session.commit()
            session.refresh(self._model)

    def double_door(self, door: Door):
        door_model = DoorData(
            cols_count=door.cols_count,
            rows_count=door.rows_count,
            number=len(self._doors),
            custom_width=door.custom_width,
            is_h_main_rigel=door.is_h_main_rigel,
        )
        for fragment in door.fragments:
            door_model.fragments.append(DoorFragmentData(
                x=fragment.x, y=fragment.y, x2=fragment.x2, y2=fragment.y2,
                material=fragment.material, fragment_container=fragment.fragment_container
            ))
        for n, size in door.custom_cols.items():
            door_model.custom_cols.append(CustomColSize(n=n, size=size))
        for n, size in door.custom_rows.items():
            door_model.custom_rows.append(CustomRowSize(n=n, size=size))
        new_door = Door(door_model, self._profile, self._rigel)
        self._doors.append(new_door)
        return new_door

    @doorway_height.setter
    def doorway_height(self, value):
        self._model.doorway_height = value

    @doorway_width.setter
    def doorway_width(self, value):
        self._model.doorway_width = value

    @guide_long.setter
    def guide_long(self, value):
        self._model.guide_long = value

    @create_date.setter
    def create_date(self, value):
        self._model.create_date = value

    @number.setter
    def number(self, value):
        self._model.number = value

    @out_date.setter
    def out_date(self, value):
        self._model.out_date = value

    @description.setter
    def description(self, value):
        self._model.description = value

    @property
    def customer(self):
        return self._customer

    @property
    def profile(self):
        return self._profile

    @property
    def rigel(self):
        return self._rigel

    @overlap_count.setter
    def overlap_count(self, value):
        self._model.overlap_count = value

    @need_shlegel.setter
    def need_shlegel(self, value):
        self._model.is_need_shlegel = value

    @is_2_line.setter
    def is_2_line(self, value):
        self._model.is_2_line = value

    @set_config_id.setter
    def set_config_id(self, value):
        self._model.set_config_id = value

    @pack_config_id.setter
    def pack_config_id(self, value):
        self._model.pack_config_id = value

    @delivery_config_id.setter
    def delivery_config_id(self, value):
        self._model.delivery_config_id = value

    @additional_materials.setter
    def additional_materials(self, value):
        self._model.additional_materials = value

    @property
    def using_materials(self) -> list[MaterialData]:
        materials = set()
        for door in self._doors:
            for fragment in door.fragments:
                if fragment.material is not None:
                    materials.add(fragment.material)
        return list(materials.union(self._deleted_materials))

    def delete(self):
        with Database.Session() as session:
            session.delete(self._model)
            session.commit()

    def create_assigment_doc(self, document=True, scheme=True):
        from app.model.pdf import create_assigment_doc, create_scheme_doc

        if document:
            pdf = create_assigment_doc(self, scheme)
        else:
            pdf = create_scheme_doc(self)
        return pdf

    def create_material_doc(self, is_for_glass: bool):
        from app.model.pdf import create_material_doc

        return create_material_doc(
            self, is_for_glass, *(m for m in self.using_materials if m.is_have_sealant == is_for_glass))

    def create_customer_doc(self):
        from app.model.pdf import create_customer_doc

        return create_customer_doc(self)

    @quide_decor.setter
    def quide_decor(self, value):
        self._model.quide_decor = value
