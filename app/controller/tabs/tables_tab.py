from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QSizePolicy, QMenu

from app.controller import response_decorator, clear_layout, error_box
from app.controller.list_items import SearchListItem, InstanceListItem
from app.controller.sql_table_controller import SQLTableController, NumSqlTableItem, StrSqlTableItem, BoolSqlTableItem, \
    NoEditTableItem
from app.controller.tabs import Tab
from app.model import AdminApp
from app.model.orm import UserData, ProfileData, RigelData, MaterialData, Database, ColorData, CustomerModel, \
    RigelColorModel, RigelColor1cModel
from app.ui import Ui_TablesTabNew


class DataTab(Tab):
    _app: AdminApp

    def __init__(self, app: AdminApp, ui_app):
        super().__init__("icons/edit.svg", "Данные", app, ui_app, -1)

        self._ui = Ui_TablesTabNew()
        self.db_session: Database.Session = Database.Session()
        self.cur_controller = None
        self._setup()

    def _setup(self):
        self._ui.setupUi(self._widget)
        self._ui.table.itemDoubleClicked.connect(lambda i: i.item_double_clicked())
        self._ui.btn_user.clicked.connect(lambda: self.update_table(
            SQLTableController(self._ui.table,
                               "Пользователи",
                               UserData,
                               UserData.id,
                               SQLTableController.SQLTableColumn("number", "Номер (Уникальный)", NumSqlTableItem),
                               SQLTableController.SQLTableColumn("password", "Пароль (Уникальный)", StrSqlTableItem),
                               SQLTableController.SQLTableColumn("phone", "Телефон", StrSqlTableItem),
                               SQLTableController.SQLTableColumn("name", "Имя", StrSqlTableItem),)
        ))
        self._ui.btn_profile.clicked.connect(lambda: self.update_table(
            SQLTableController(self._ui.table,
                               "Профиль",
                               ProfileData,
                               ProfileData.id,
                               SQLTableController.SQLTableColumn("overlap", "Перехлест", NumSqlTableItem),
                               SQLTableController.SQLTableColumn("guide", "Направляющая", NumSqlTableItem),
                               SQLTableController.SQLTableColumn("sealant", "Уплотнитель", NumSqlTableItem),
                               SQLTableController.SQLTableColumn("shlegel", "Шлегель", NumSqlTableItem),
                               SQLTableController.SQLTableColumn("is_open", "Открытый?", BoolSqlTableItem),
                               SQLTableController.SQLTableColumn("v_width", "Ширина В.", NumSqlTableItem),
                               SQLTableController.SQLTableColumn("v_depth", "Грубина В.", NumSqlTableItem),
                               SQLTableController.SQLTableColumn("h_top_width", "Высота Г.В.", NumSqlTableItem),
                               SQLTableController.SQLTableColumn("h_bot_width", "Высота Г.Н.", NumSqlTableItem),
                               SQLTableController.SQLTableColumn("h_top_depth", "Глубина Г.В.", NumSqlTableItem),
                               SQLTableController.SQLTableColumn("h_bot_depth", "Глубина Г.Н.", NumSqlTableItem),
                               SQLTableController.SQLTableColumn("name", "Название", StrSqlTableItem),
                               )
        ))
        self._ui.btn_rigel.clicked.connect(self.open_rigel_menu)
        self._ui.btn_material.clicked.connect(lambda: self.update_table(
            SQLTableController(self._ui.table,
                               "Материал",
                               MaterialData,
                               MaterialData.id,
                               SQLTableController.SQLTableColumn("is_have_sealant", "Уплотнитель?", BoolSqlTableItem),
                               SQLTableController.SQLTableColumn("name", "Название", StrSqlTableItem),)
        ))
        self._ui.btn_color.clicked.connect(lambda: self.update_table(
            SQLTableController(self._ui.table,
                               "Цвет",
                               ColorData,
                               ColorData.id,
                               SQLTableController.SQLTableColumn("name", "Наименование", StrSqlTableItem),)
        ))
        self._ui.btn_customer.clicked.connect(lambda: self.update_table(
            SQLTableController(self._ui.table,
                               "Клиент",
                               CustomerModel,
                               CustomerModel.id,
                               SQLTableController.SQLTableColumn("name", "Имя клиента", StrSqlTableItem),)
        ))

        self._ui.btn_save.clicked.connect(self.save)
        self._ui.table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self._ui.table.customContextMenuRequested.connect(self.show_table_context_menu)

        self._ui.lst_rigel_names.itemClicked.connect(self.open_rigel_instance)
        self._ui.lst_rigel_colors.itemChanged.connect(self.rigel_color_select)

    def update_table(self, controller: SQLTableController):
        self._ui.tabWidget.setCurrentIndex(2)
        self.cur_controller = controller
        self.db_session.close()
        self.db_session = Database.Session()

        if self._ui.r_actual.isChecked():
            filters = [controller.model.on_delete == False]
        elif self._ui.r_deleted.isChecked():
            filters = [controller.model.on_delete == True]
        else:
            filters = []

        controller.enable((self.db_session.query(controller.model)), *filters)

    def open_rigel_menu(self):
        self.cur_controller = None
        self.db_session.close()
        self.db_session = Database.Session()
        self._ui.tabWidget.setCurrentIndex(1)

        self._ui.lst_rigel_names.clear()
        self._ui.tbl_rigel_params.clear()
        self._ui.tbl_rigel_params.setRowCount(2)
        self._ui.lst_rigel_colors.clear()
        self._ui.tbl_rigel_1c.clear()
        self._ui.tbl_rigel_1c.setRowCount(1)

        for (id_, name) in self.db_session.query(RigelData.id, RigelData.name).order_by(RigelData.id.desc()).all():
            self._ui.lst_rigel_names.addItem(SearchListItem((id_, name)))

        for color_data in self.db_session.query(ColorData).order_by(ColorData.id.desc()).all():
            # noinspection PyTypeChecker
            self._ui.lst_rigel_colors.addItem(
                item := InstanceListItem(color_data, f"<{color_data.id}> {color_data.name}")
            )
            item.setCheckState(Qt.CheckState.Unchecked)

    def open_rigel_instance(self, rigel_item: SearchListItem):
        self._ui.lst_rigel_colors.setCurrentItem(None)
        self._ui.tbl_rigel_1c.clear()

        for i in range(self._ui.lst_rigel_colors.count()):
            self._ui.lst_rigel_colors.item(i).setCheckState(Qt.CheckState.Unchecked)

        i = 0
        for color_id, in (
                self.db_session.query(RigelColorModel.color_id)
                .filter(RigelColorModel.rigel_id == rigel_item.id)
                .order_by(RigelColorModel.color_id.desc())
                .all()
        ):
            while self._ui.lst_rigel_colors.item(i).instance.id > color_id:
                i += 1

            color_item: SearchListItem = self._ui.lst_rigel_colors.item(i)
            color_item.setCheckState(Qt.CheckState.Checked)
            i += 1

        # noinspection PyTypeChecker
        instance: RigelData = self.db_session.query(RigelData).filter(RigelData.id == rigel_item.id).one()
        params = [
            (NoEditTableItem('Середина'), NumSqlTableItem(instance, 'center_width')),
            (NoEditTableItem('Глубина'), NumSqlTableItem(instance, 'depth')),
        ]
        for i, row in enumerate(params):
            for j, item in enumerate(row):
                self._ui.tbl_rigel_params.setItem(i, j, item)

    def rigel_color_select(self, item: InstanceListItem):
        if (cur_item := self._ui.lst_rigel_names.currentItem()) is None:
            return

        instance = self.db_session.query(RigelData).filter(RigelData.id == cur_item.id).one()
        if item.checkState() == Qt.CheckState.Checked:
            self.db_session.merge(RigelColorModel(rigel_id=instance.id, color_id=item.instance.id))
        else:
            self.db_session.delete(RigelColorModel(rigel_id=instance.id, color_id=item.instance.id))

    def open_rigel_color_instance(self, color_item: InstanceListItem):
        if (cur_item := self._ui.lst_rigel_names.currentItem()) is None:
            return

        rigel = self.db_session.query(RigelData).filter(RigelData.id == cur_item.id).one()

        # noinspection PyTypeChecker
        if (instance := (
            self.db_session.query(RigelColor1cModel)
            .filter(
                RigelColor1cModel.rigel_id == rigel.id,
            ).one()
        )) is None:
            self.db_session.add(instance := RigelColor1cModel(rigel_id=rigel.id, color_id=color_item.instance.id))

        params = [
            (NoEditTableItem('Ригель'), NumSqlTableItem(instance, 'center_width')),
        ]
        for i, row in enumerate(params):
            for j, item in enumerate(row):
                self._ui.tbl_rigel_params.setItem(i, j, item)

    def add_row(self):
        self.db_session.add(self.cur_controller.model())
        self.cur_controller.enable()

    def show_table_context_menu(self, pos):
        menu = QMenu(self._widget)
        instance = self._ui.table.selectedItems()[0].instance
        (menu.addAction("Восстановить" if instance.on_delete else "На удаление")).triggered.connect(
            lambda *, i=instance: self.delete_or_restore(i)
        )
        menu.exec(self._ui.table.mapToGlobal(pos))

    @response_decorator
    def save(self):
        try:
            self.db_session.flush()
        except Exception as e:
            error_box(str(e))
            self.db_session.rollback()
        self.db_session.commit()

    def __del__(self):
        self.db_session.close()

    def delete_or_restore(self, i):
        i.on_delete = not i.on_delete
        self.save()
        self.cur_controller.enable()
