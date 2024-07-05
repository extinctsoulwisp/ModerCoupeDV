from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QSizePolicy, QMenu

from app.controller import response_decorator, clear_layout, error_box
from app.controller.sql_table_controller import SQLTableController, NumSqlTableItem, StrSqlTableItem, BoolSqlTableItem
from app.controller.tabs import Tab
from app.model import AdminApp
from app.model.orm import UserData, ProfileData, RigelData, MaterialData, Database, ColorData, CustomerModel
from app.ui.ui_admin_tables import Ui_tables_tab


class DataTab(Tab):
    _app: AdminApp

    def __init__(self, app: AdminApp, ui_app):
        super().__init__("icons/edit.svg", "Данные", app, ui_app, -1)

        self._ui = Ui_tables_tab()
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
        self._ui.btn_rigel.clicked.connect(lambda: self.update_table(
            SQLTableController(self._ui.table,
                               "Ригель",
                               RigelData,
                               RigelData.id,
                               SQLTableController.SQLTableColumn("center_width", "Середина", NumSqlTableItem),
                               SQLTableController.SQLTableColumn("depth", "Глубина", NumSqlTableItem),
                               SQLTableController.SQLTableColumn("name", "Название", StrSqlTableItem),
                               )
        ))
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

        self._ui.btn_add.clicked.connect(self.add_row)
        self._ui.btn_save.clicked.connect(self.save)
        self._ui.table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self._ui.table.customContextMenuRequested.connect(self.show_table_context_menu)

    def update_table(self, controller: SQLTableController):
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
