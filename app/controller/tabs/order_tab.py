import datetime
import subprocess
from typing import List

from PySide6.QtCore import QDate
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QDialog, QMenu, QListView

from app.model import Order, App, Material, DoorFragment
from app.ui import Ui_OrderTab
from . import Tab
from app import Error
from .. import error_box, confirm_decorator, response_decorator, confirm_box
from ..dialogs import DoorDialog, ProfileSearchDialog, CustomerSearchDialog, RigelSearchDialog, MaterialSearchDialog
from ..dialogs.color_search_dialog import ColorSearchDialog
from ..door_controller import DoorController
from ...model.func import round_size
from ...model.orm import MaterialData, DoorFragmentData

guide_count_state = [True, False, None]


class OrderTab(Tab):
    def __init__(self, app: App, ui_app, order: Order):
        from .. import DoorFragmentController
        super().__init__("icons/document.svg", "Форм", app, ui_app, order.id)
        self._ui: Ui_OrderTab = Ui_OrderTab()
        self._ui.setupUi(self._widget)
        self._order: Order = order
        self._doors: List[DoorController] = []
        for door in self._order.doors: self._add_door_controller(door)

        self._selected_door_fragment: DoorFragmentController or None = None
        self._selected_material: Material = Material(MaterialData())
        self._rigel_is_not_changed = True

        self._setup()
        self._update_view()

    def rename_tab(self, new_name: str):
        self.list_item.setText(new_name)

    def change_system(self, state: bool):
        self._ui.c_bot_system.setText("Нижняя опорная" if state else "Верхняя подвесная")
        self._ui.lbl_guide_decor.setVisible(not state)
        self._ui.c_guide_decor.setVisible(not state)

    def _setup(self):
        self._ui.btn_exit.clicked.connect(lambda *_: self._ui_app.close_tab(self))
        self._ui.btn_save.clicked.connect(self.save_in_db)
        self._ui.btn_add_door.clicked.connect(self._add_door)
        self._ui.btn_customer.clicked.connect(self._choice_customer)
        self._ui.btn_profile.clicked.connect(self._choice_profile)
        self._ui.btn_rigel.clicked.connect(self._choice_rigel)
        self._ui.btn_update.clicked.connect(self._update_scheme)
        self._ui.r_material.clicked.connect(self._choice_material)
        self._ui.btn_color.clicked.connect(self._choice_color)
        self._ui.btn_document.clicked.connect(self._create_pdf)
        self._ui.inp_quide_long.setValidator(QRegularExpressionValidator(r"[0-9]+"))
        self._ui.inp_overlap_count.setValidator(QRegularExpressionValidator(r"[0-9]+"))
        self._ui.ch_need_shlegel.toggled.connect(
            lambda: self._ui.ch_need_shlegel.setText("Нужен" if self._ui.ch_need_shlegel.isChecked() else "Не нужен")
        )
        self._ui.c_bot_system.stateChanged.connect(self.change_system)
        self._ui.c_set_config.setView(QListView())
        self._ui.c_delivery_config.setView(QListView())
        self._ui.c_pack_config.setView(QListView())

    def _update_model(self):
        self._order.doorway_height = self._ui.inp_height.value()
        self._order.doorway_width = self._ui.inp_width.value()
        self._order.guide_long = int(t) if (t := self._ui.inp_quide_long.text()) else 0
        create_date = self._ui.inp_date.date()
        self._order.create_date = datetime.date(create_date.year(), create_date.month(), create_date.day())
        self._order.number = self._ui.inp_order_number.value()
        out_date = self._ui.inp_date_uot.date()
        self._order.out_date = datetime.date(out_date.year(), out_date.month(), out_date.day())
        self._order.description = self._ui.inp_description.toPlainText()
        self._order.overlap_count = int(t) if (t := self._ui.inp_overlap_count.text()) else None

        self._order.need_shlegel = self._ui.ch_need_shlegel.isChecked()

        self._order.is_2_line = guide_count_state[self._ui.c_guide.currentIndex()]

        self._order.set_config_id = self._ui.c_set_config.currentIndex() + 1
        self._order.pack_config_id = self._ui.c_pack_config.currentIndex() + 1
        self._order.delivery_config_id = self._ui.c_delivery_config.currentIndex() + 1

        self._order.part_number = v if (v := self._ui.inp_order_number_part.value()) else None

        self._order.additional_materials = self._ui.inp_additional_materials.toPlainText()
        if self._ui.c_bot_system.isChecked():
            self._order.quide_decor = None
        else:
            self._order.quide_decor = self._ui.c_guide_decor.value()

    def _add_door_controller(self, door, pos: int = None):
        if pos is None:
            pos = self._ui.scheme_widget.layout().count() - 1
        door_controller = DoorController(door)
        self._ui.scheme_widget.layout().insertWidget(pos, door_controller.widget)
        for fragment_controller in door_controller.fragments:
            door_controller.ui.frame.layout().addWidget(
                fragment_controller.widget,
                fragment_controller.door_fragment.y,
                fragment_controller.door_fragment.x,
                fragment_controller.door_fragment.y2 - fragment_controller.door_fragment.y + 1,
                fragment_controller.door_fragment.x2 - fragment_controller.door_fragment.x + 1,
            )
            fragment_controller.widget.mousePressEvent = lambda *_, fc=fragment_controller: \
                self.door_fragment_click_func(fc)
        self._doors.append(door_controller)
        return door_controller

    def _add_door(self):
        self._update_model()

        if self._rigel_is_not_changed:
            if confirm_box(f"'{self._order.rigel.name}' - правильно выбран ригель?"):
                self._rigel_is_not_changed = False
            else:
                return

        door_dialog = DoorDialog()
        if door_dialog.exec() == QDialog.DialogCode.Accepted:
            new_door = self._order.create_door(door_dialog.cols_count, door_dialog.rows_count)
            for i, col_size in enumerate(door_dialog.cols_sizes):
                if col_size:
                    new_door.set_column_size(i, col_size)
            for j, row_size in enumerate(door_dialog.rows_sizes):
                if row_size:
                    new_door.set_row_size(j, row_size)
            new_door.set_width(door_dialog.door_width, auto=not door_dialog.door_width)
            new_door.is_h_main_rigel = door_dialog.is_h_main_rigel
            self._add_door_controller(new_door)
            self._update_scheme()

    @confirm_decorator("Уверены, что хотите удалить дверь?")
    def delete_door(self, door: DoorController):
        door.delete()
        self._order.delete_door(door.door)
        self._doors.remove(door)
        del door
        self._update_scheme()

    @response_decorator
    def save_in_db(self):
        self._update_model()
        self._order.save_in_db()
        self._ui_app.refresh_order(self)

    def edit_door(self, door: DoorController):
        door_dialog = DoorDialog(door.door)
        door_model = door.door

        if door_dialog.exec() == QDialog.DialogCode.Accepted:
            if door.door.rows_count != door_dialog.rows_count or door.door.cols_count != door_dialog.cols_count:
                door.delete()
                self._doors.remove(door)
                del door

                to_remove = []
                for fragment in door_model.fragments:
                    fragment.unmerge()
                    if fragment.x >= door_dialog.cols_count or fragment.y >= door_dialog.rows_count:
                        to_remove.append(fragment)

                for fragment in to_remove:
                    door_model.fragments.remove(fragment)

                for i in range(door_dialog.rows_count):
                    for j in range(door_dialog.cols_count):
                        if door_model.fragment_at(i, j) is None:
                            door_model.fragments.append(DoorFragment(
                                DoorFragmentData(x=j, y=i, x2=j, y2=i),
                                rigel=self._order.rigel,
                                profile=self._order.profile
                            ))

                door_model.cols_count = door_dialog.cols_count
                door_model.rows_count = door_dialog.rows_count

                self._add_door_controller(door_model, door_model.number + 2)

            for i, col_size in enumerate(door_dialog.cols_sizes):
                door_model.set_column_size(i, col_size)

            for j, row_size in enumerate(door_dialog.rows_sizes):
                door_model.set_row_size(j, row_size)

            door_model.set_width(door_dialog.door_width, auto=not door_dialog.door_width)
            door_model.is_h_main_rigel = door_dialog.is_h_main_rigel

        self._update_model()
        self._update_scheme()

    def _choice_customer(self):
        customer_dialog = CustomerSearchDialog(self._app)

        if customer_dialog.exec() == QDialog.DialogCode.Accepted and self._order.customer.id != customer_dialog.selected_id:
            self._order.customer.change_model_from_id(customer_dialog.selected_id)

            self._update_model()
            self._update_view()

    def _choice_color(self):
        color_dialog = ColorSearchDialog(self._app)

        if color_dialog.exec() == QDialog.DialogCode.Accepted and self._order.profile_color.id != color_dialog.selected_id:
            self._order.profile_color.change_model_from_id(color_dialog.selected_id)

            self._update_model()
            self._update_view()

    def _choice_profile(self):
        profile_dialog = ProfileSearchDialog(self._app)

        if profile_dialog.exec() == QDialog.DialogCode.Accepted and self._order.profile.id != profile_dialog.selected_id:
            self._order.profile.change_model_from_id(profile_dialog.selected_id)

            self._update_model()
            self._update_view()

    def _choice_rigel(self):
        customer_dialog = RigelSearchDialog(self._app)

        if customer_dialog.exec() == QDialog.DialogCode.Accepted and self._order.rigel.id != customer_dialog.selected_id:
            self._order.rigel.change_model_from_id(customer_dialog.selected_id)

            self._update_model()
            self._update_view()

    def _choice_material(self):
        material_dialog = MaterialSearchDialog(self._app)

        if material_dialog.exec() == QDialog.DialogCode.Accepted:
            self._selected_material.change_model_from_id(material_dialog.selected_id)
            for material in self._order.using_materials:
                if material.id == material_dialog.selected_id:
                    self._selected_material.model = material
                    break

            self._ui.r_material.setText(self._selected_material.name)
            self._update_model()
            self._update_view()

    def _update_view(self):
        self._ui.inp_height.setValue(self._order.doorway_height)
        self._ui.inp_width.setValue(self._order.doorway_width)
        self._ui.inp_quide_long.setText(str(t) if (t := self._order.guide_long) else "")
        self._ui.inp_date.setDate(QDate(
            self._order.create_date.year,
            self._order.create_date.month,
            self._order.create_date.day
        ))
        self._ui.inp_responsibility.setText(str(self._order.responsible.number))
        self._ui.inp_order_number.setValue(self._order.number)
        self._ui.inp_date_uot.setDate(QDate(
            self._order.out_date.year,
            self._order.out_date.month,
            self._order.out_date.day
        ))
        self._ui.inp_description.setText(self._order.description)

        self._ui.btn_customer.setText(self._order.customer.name)
        self._ui.btn_profile.setText(self._order.profile.name)
        self._ui.btn_rigel.setText(self._order.rigel.name)
        self._ui.btn_color.setText(self._order.profile_color.name)

        self._ui.inp_overlap_count.setText(str(t) if (t := self._order.overlap_count) is not None else "")

        self._ui.ch_need_shlegel.setChecked(self._order.need_shlegel)
        self._ui.c_guide.setCurrentIndex(guide_count_state.index(self._order.is_2_line))

        self._ui.c_set_config.setCurrentIndex(self._order.set_config_id - 1)
        self._ui.c_pack_config.setCurrentIndex(self._order.pack_config_id - 1)
        self._ui.c_delivery_config.setCurrentIndex(self._order.delivery_config_id - 1)

        self._ui.inp_additional_materials.setText(self._order.additional_materials)
        self._ui.inp_order_number_part.setValue(0 if (v := self._order.part_number) is None else v)

        self._ui.c_bot_system.setChecked(self._order.quide_decor is None)
        if self._order.quide_decor is not None:
            self._ui.c_guide_decor.setValue(self._order.quide_decor)

    def _update_scheme(self):
        self._update_model()
        self._order.update()
        scale = self._ui.scrollArea.height() / self._order.doorway_height * 0.8

        for door_controller in self._doors:
            door_controller.update()
            for fragment_controller in door_controller.fragments:
                door_controller.ui.frame.layout().removeWidget(fragment_controller.widget)
                door_controller.ui.frame.layout().addWidget(
                    fragment_controller.widget,
                    fragment_controller.door_fragment.y,
                    fragment_controller.door_fragment.x,
                    fragment_controller.door_fragment.y2 - fragment_controller.door_fragment.y + 1,
                    fragment_controller.door_fragment.x2 - fragment_controller.door_fragment.x + 1,
                )
                door_controller.ui.frame.layout().setSpacing(self._order.rigel.center_width * scale)
                fragment_controller.widget.setFixedHeight(fragment_controller.door_fragment.height * scale)
                fragment_controller.widget.setFixedWidth(fragment_controller.door_fragment.width * scale)
                fragment_controller.update()
        self._ui.doors_height.setText(str(round_size(self._order.doorway_height - self._order.profile.guide)))

    def _door_by_fragment(self, door_fragment_controller) -> DoorController:
        for door in self._doors:
            for fragment in door.fragments:
                if fragment.door_fragment is door_fragment_controller.door_fragment:
                    return door

    def door_fragment_click_func(self, fragment):
        from .. import DoorFragmentController
        fragment: DoorFragmentController

        if self._ui.r_material.isChecked():
            fragment.door_fragment.set_material_model(self._selected_material.model)

        elif self._ui.r_unmerge.isChecked():
            fragment.door_fragment.unmerge()

        elif self._ui.r_delete_door.isChecked():
            self.delete_door(self._door_by_fragment(fragment))

        elif self._ui.r_edit_door.isChecked():
            self.edit_door(self._door_by_fragment(fragment))

        elif self._ui.r_double.isChecked():
            for fragment_ in self._door_by_fragment(fragment).fragments:
                fragment_.door_fragment.unmerge()
            self.double_door(self._door_by_fragment(fragment))

        elif self._ui.r_merge.isChecked():
            if self._selected_door_fragment is None:
                self._selected_door_fragment = fragment
                fragment.is_selected = True
            elif fragment is self._selected_door_fragment:
                self._selected_door_fragment = None
                fragment.is_selected = False
            elif self._door_by_fragment(self._selected_door_fragment) is not self._door_by_fragment(fragment):
                error_box(Error.CANT_MERGE_DIFFERENT_DOORS_FRAGMENTS)
                self._selected_door_fragment._is_selected = False
                self._selected_door_fragment = None
            elif (self._selected_door_fragment.x > fragment.x or
                  self._selected_door_fragment.y > fragment.y):
                error_box(Error.CANT_MERGE_DOORS_FRAGMENTS)
                self._selected_door_fragment._is_selected = False
                self._selected_door_fragment = None
            else:
                selected_fragments = []
                for selected_fragment in self._door_by_fragment(fragment).fragments:
                    if (self._selected_door_fragment.x <= selected_fragment.x <= fragment.x and
                            self._selected_door_fragment.y <= selected_fragment.y <= fragment.y and
                            selected_fragment is not self._selected_door_fragment):
                        if (selected_fragment.door_fragment.merged_fragments or
                                self._selected_door_fragment.door_fragment.merged_fragments or
                                fragment.door_fragment.merged_fragments or
                                selected_fragment.door_fragment.fragment_container):
                            error_box(Error.CANT_MERGE_MERGED_DOORS_FRAGMENTS)
                            return
                        selected_fragments.append(selected_fragment.door_fragment)

                self._selected_door_fragment.door_fragment.merge(selected_fragments)
                self._selected_door_fragment._is_selected = False
                self._selected_door_fragment = None

        self._update_scheme()

    @confirm_decorator("Удалить заказ из базы?")
    def delete(self):
        self._order.delete()
        self._ui_app.close_tab(self, confirm=False)

    def double_door(self, door: DoorController):
        new_door = self._order.double_door(door.door)
        self._add_door_controller(new_door)
        self._update_scheme()

    def _create_pdf(self):
        menu = QMenu(self.widget)
        menu.setStyleSheet(
            "QMenu {"
            "   margin: 0;"
            "   color: white;"
            "}"
            "QMenu::item {"
            "   padding: 5px 20px;"
            "   background-color: rgb(39, 50, 56);"
            "}"
            "QMenu::item:selected {"
            "   background-color: rgb(69, 75, 84);"
            "}"
            "QMenu::separator {"
            "   background-color: rgb(69, 75, 84);"
            "}"
        )

        action = menu.addAction("Наряд")
        action.triggered.connect(lambda: self.create_assigment_doc())
        action = menu.addAction("Наряд без рисунка")
        action.triggered.connect(lambda: self.create_assigment_doc(scheme=False))
        action = menu.addAction("Рисунок")
        action.triggered.connect(lambda: self.create_assigment_doc(document=False))
        action = menu.addAction("Заявка на плиточный")
        action.triggered.connect(lambda: self.create_material_doc(is_for_glass=False))
        action = menu.addAction("Заявка на стекольный")
        action.triggered.connect(lambda: self.create_material_doc(is_for_glass=True))

        menu.exec(self._ui.btn_document.mapToGlobal(self._ui.btn_document.rect().bottomLeft()))

    @property
    def order(self):
        return self._order

    def create_material_doc(self, is_for_glass: bool):
        self._update_scheme()
        try:
            subprocess.call(['start', '', self._order.create_material_doc(is_for_glass)], shell=True)
        except Exception as e:
            error_box(str(e))

    def create_assigment_doc(self, document=True, scheme=True):
        self._update_scheme()
        try:
            subprocess.call(['start', '', self._order.create_assigment_doc(document, scheme)], shell=True)
        except Exception as e:
            error_box(str(e))
