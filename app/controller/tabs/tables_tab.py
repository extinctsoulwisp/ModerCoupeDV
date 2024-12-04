from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QLabel, QSizePolicy, QMenu

from app.controller import response_decorator, clear_layout, error_box
from app.controller.list_items import SearchListItem, InstanceListItem
from app.controller.sql_table_controller import SQLTableController, NumSqlTableItem, StrSqlTableItem, BoolSqlTableItem, \
    NoEditTableItem, OneCSqlTableItem, SqlTableItem
from app.controller.tabs import Tab
from app.model import AdminApp
from app.model.orm import UserData, ProfileData, RigelData, MaterialData, Database, ColorData, CustomerModel, \
    RigelColorModel, RigelColor1cModel, ProfileColorModel
from app.model.orm.one_c_data import ProfileColor1cModel, Customer1cData, Nomenclature1cData, Config1cData
from app.ui import Ui_TablesTabNew


class DataTab(Tab):
    _app: AdminApp

    def __init__(self, app: AdminApp, ui_app):
        super().__init__("icons/edit.svg", "Данные", app, ui_app, -1)

        self._ui = Ui_TablesTabNew()
        self.db_session: Database.Session = Database.Session()
        self.cur_controller: SQLTableController | None = None
        self._setup()

    def clear_tabs(self):
        self._ui.lst_rigel_names.clear()
        self._ui.tbl_rigel_params.clear()
        self._ui.lst_rigel_colors.clear()
        self._ui.tbl_rigel_1c.clear()

        self._ui.lst_profile_names.clear()
        self._ui.tbl_profile_params.clear()
        self._ui.lst_profile_colors.clear()
        self._ui.tbl_profile_1c.clear()

        self._ui.lst_config_names.clear()
        self._ui.lst_config_params.clear()
        self._ui.tbl_config_1c.clear()

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
                               SQLTableController.SQLTableColumn("name", "Имя", StrSqlTableItem), )
        ))
        self._ui.btn_profile.clicked.connect(self.open_profile_menu)
        self._ui.btn_rigel.clicked.connect(self.open_rigel_menu)
        self._ui.btn_config.clicked.connect(self.open_config_menu)
        self._ui.btn_material.clicked.connect(lambda: self.update_table(
            SQLTableController(self._ui.table,
                               "Материал",
                               MaterialData,
                               MaterialData.id,
                               SQLTableController.SQLTableColumn("is_have_sealant", "Уплотнитель?", BoolSqlTableItem),
                               SQLTableController.SQLTableColumn("name", "Название", StrSqlTableItem), )
        ))
        self._ui.btn_color.clicked.connect(lambda: self.update_table(
            SQLTableController(self._ui.table,
                               "Цвет",
                               ColorData,
                               ColorData.id,
                               SQLTableController.SQLTableColumn("name", "Наименование", StrSqlTableItem), )
        ))
        self._ui.btn_customer.clicked.connect(lambda: self.update_table(
            SQLTableController(self._ui.table,
                               "Клиент",
                               CustomerModel,
                               CustomerModel.id,
                               SQLTableController.SQLTableColumn("name", "Имя клиента", StrSqlTableItem), )
        ))
        self._ui.btn_1c_customer.clicked.connect(lambda: self.update_table(
            SQLTableController(self._ui.table,
                               "1C.Клиент",
                               Customer1cData,
                               Customer1cData.one_c_id,
                               SQLTableController.SQLTableColumn("one_c_id", "Код 1С", SqlTableItem),
                               SQLTableController.SQLTableColumn("name", "Имя клиента", StrSqlTableItem), )
        ))
        self._ui.btn_1c_nomenclature.clicked.connect(lambda: self.update_table(
            SQLTableController(self._ui.table,
                               "1C.Номенклатура",
                               Nomenclature1cData,
                               Nomenclature1cData.one_c_id,
                               SQLTableController.SQLTableColumn("one_c_id", "Код 1С", SqlTableItem),
                               SQLTableController.SQLTableColumn("price", "Цена", SqlTableItem),
                               SQLTableController.SQLTableColumn("unit", "Ед. измерения", StrSqlTableItem),
                               SQLTableController.SQLTableColumn("category", "Категория", StrSqlTableItem),
                               SQLTableController.SQLTableColumn("name", "Наименование", SqlTableItem), )
        ))

        self._ui.btn_save.clicked.connect(self.save)
        self._ui.table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self._ui.table.customContextMenuRequested.connect(self.show_table_context_menu)
        self._ui.lst_rigel_names.customContextMenuRequested.connect(self.show_table_context_menu)
        self._ui.lst_profile_names.customContextMenuRequested.connect(self.show_table_context_menu)
        self._ui.tabWidget.currentChanged.connect(self.clear_tabs)

        self._ui.tbl_rigel_params.setRowCount(3)
        self._ui.tbl_rigel_1c.setRowCount(1)
        self._ui.tbl_profile_params.setRowCount(13)
        self._ui.tbl_profile_1c.setRowCount(13)

        self._ui.lst_rigel_names.itemSelectionChanged.connect(
            lambda *_: self.open_rigel_instance(self._ui.lst_rigel_names.currentItem())
        )
        self._ui.lst_rigel_colors.itemChanged.connect(self.rigel_color_select)
        self._ui.lst_rigel_colors.itemSelectionChanged.connect(
            lambda *_: self.open_rigel_color_instance(self._ui.lst_rigel_colors.currentItem())
        )
        self._ui.tbl_rigel_1c.itemDoubleClicked.connect(lambda i: i.item_double_clicked())

        self._ui.lst_profile_names.itemSelectionChanged.connect(
            lambda *_: self.open_profile_instance(self._ui.lst_profile_names.currentItem())
        )
        self._ui.lst_profile_colors.itemChanged.connect(self.profile_color_select)
        self._ui.lst_profile_colors.itemSelectionChanged.connect(
            lambda *_: self.open_profile_color_instance(self._ui.lst_profile_colors.currentItem())
        )
        self._ui.tbl_profile_1c.itemDoubleClicked.connect(lambda i: i.item_double_clicked())

        self._ui.lst_config_names.itemSelectionChanged.connect(
            lambda *_: self.open_config_name(self._ui.lst_config_names.currentItem())
        )
        self._ui.lst_config_params.itemSelectionChanged.connect(
            lambda *_: self.open_config_pare(self._ui.lst_config_params.currentItem())
        )

    def get_filters(self, model):
        if self._ui.r_actual.isChecked():
            return [model.on_delete == False]
        elif self._ui.r_deleted.isChecked():
            return [model.on_delete == True]
        else:
            return []

    def update_table(self, controller: SQLTableController):
        self._ui.tabWidget.setCurrentIndex(2)
        self.cur_controller = controller
        self.db_session.close()
        self.db_session = Database.Session()

        controller.enable((self.db_session.query(controller.model)), *self.get_filters(controller.model))

    def open_rigel_menu(self, *, reopen_session=True):
        if reopen_session:
            self.db_session.close()
            self.db_session = Database.Session()

        self.cur_controller = None
        self._ui.tabWidget.setCurrentIndex(1)
        self.clear_tabs()

        for (id_, name, on_delete) in (
                self.db_session.query(RigelData.id, RigelData.name, RigelData.on_delete)
                        .filter(*self.get_filters(RigelData))
                        .order_by(RigelData.id.desc())
                        .all()

        ):
            self._ui.lst_rigel_names.addItem(item := SearchListItem((id_, name)))
            if on_delete:
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)

        for color_data in (self.db_session.query(ColorData)
                .filter(*self.get_filters(ColorData)).order_by(ColorData.id.desc()).all()):
            # noinspection PyTypeChecker
            self._ui.lst_rigel_colors.addItem(
                item := InstanceListItem(color_data, f"<{color_data.id}> {color_data.name}")
            )
            item.setCheckState(Qt.CheckState.Unchecked)
            if color_data.on_delete:
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)

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
            (NoEditTableItem('Наименование'), StrSqlTableItem(instance, 'name')),
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
                ).first()
        )) is None:
            self.db_session.add(instance := RigelColor1cModel(rigel_id=rigel.id, color_id=color_item.instance.id))

        params = [
            (NoEditTableItem('Ригель'), OneCSqlTableItem(instance, 'one_c_id', 'Номенклатура')),
        ]
        for i, row in enumerate(params):
            for j, item in enumerate(row):
                self._ui.tbl_rigel_1c.setItem(i, j, item)

    def open_profile_menu(self, *, reopen_session=True):
        if reopen_session:
            self.db_session.close()
            self.db_session = Database.Session()

        self.cur_controller = None
        self._ui.tabWidget.setCurrentIndex(0)
        self.clear_tabs()

        for (id_, name, on_delete) in (
                self.db_session.query(ProfileData.id, ProfileData.name, ProfileData.on_delete)
                        .filter(*self.get_filters(ProfileData))
                        .order_by(ProfileData.id.desc())
                        .all()

        ):
            self._ui.lst_profile_names.addItem(item := SearchListItem((id_, name)))
            if on_delete:
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)

        for color_data in (self.db_session.query(ColorData)
                .filter(*self.get_filters(ColorData)).order_by(ColorData.id.desc()).all()):
            # noinspection PyTypeChecker
            self._ui.lst_profile_colors.addItem(
                item := InstanceListItem(color_data, f"<{color_data.id}> {color_data.name}")
            )
            item.setCheckState(Qt.CheckState.Unchecked)
            if color_data.on_delete:
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)

    def open_profile_instance(self, profile_item: SearchListItem):
        self._ui.lst_profile_colors.setCurrentItem(None)
        self._ui.tbl_profile_1c.clear()

        for i in range(self._ui.lst_profile_colors.count()):
            self._ui.lst_profile_colors.item(i).setCheckState(Qt.CheckState.Unchecked)

        i = 0
        for color_id, in (
                self.db_session.query(ProfileColorModel.color_id)
                        .filter(ProfileColorModel.profile_id == profile_item.id)
                        .order_by(ProfileColorModel.color_id.desc())
                        .all()
        ):
            while self._ui.lst_profile_colors.item(i).instance.id > color_id:
                i += 1

            color_item: SearchListItem = self._ui.lst_profile_colors.item(i)
            color_item.setCheckState(Qt.CheckState.Checked)
            i += 1

        # noinspection PyTypeChecker
        instance: ProfileData = self.db_session.query(ProfileData).filter(ProfileData.id == profile_item.id).one()
        params = [
            (NoEditTableItem('Наименование'), StrSqlTableItem(instance, 'name')),
            (NoEditTableItem('Перехлест'), NumSqlTableItem(instance, 'overlap')),
            (NoEditTableItem('Направляющая'), NumSqlTableItem(instance, 'guide')),
            (NoEditTableItem('Уплотнитель'), NumSqlTableItem(instance, 'sealant')),
            (NoEditTableItem('Шлегель'), NumSqlTableItem(instance, 'shlegel')),
            (NoEditTableItem('Открытый?'), NumSqlTableItem(instance, 'is_open')),
            (NoEditTableItem('Ширина В.'), NumSqlTableItem(instance, 'v_width')),
            (NoEditTableItem('Глубина В.'), NumSqlTableItem(instance, 'v_depth')),
            (NoEditTableItem('Высота Г.В.'), NumSqlTableItem(instance, 'h_top_width')),
            (NoEditTableItem('Высота Г.Н.'), NumSqlTableItem(instance, 'h_bot_width')),
            (NoEditTableItem('Глубина Г.В.'), NumSqlTableItem(instance, 'h_top_depth')),
            (NoEditTableItem('Глубина Г.Н.'), NumSqlTableItem(instance, 'h_bot_depth')),
        ]
        for i, row in enumerate(params):
            for j, item in enumerate(row):
                self._ui.tbl_profile_params.setItem(i, j, item)

    def profile_color_select(self, item: InstanceListItem):
        if (cur_item := self._ui.lst_profile_names.currentItem()) is None:
            return

        instance = self.db_session.query(ProfileData).filter(ProfileData.id == cur_item.id).one()
        if item.checkState() == Qt.CheckState.Checked:
            self.db_session.merge(ProfileColorModel(profile_id=instance.id, color_id=item.instance.id))
        else:
            self.db_session.delete(ProfileColorModel(profile_id=instance.id, color_id=item.instance.id))

    def open_profile_color_instance(self, color_item: InstanceListItem):
        if (cur_item := self._ui.lst_profile_names.currentItem()) is None:
            return

        profile = self.db_session.query(ProfileData).filter(ProfileData.id == cur_item.id).one()

        # noinspection PyTypeChecker
        if (instance := (
                self.db_session.query(ProfileColor1cModel)
                        .filter(
                    ProfileColor1cModel.profile_id == profile.id,
                ).first()
        )) is None:
            self.db_session.add(instance := ProfileColor1cModel(profile_id=profile.id, color_id=color_item.instance.id))

        params = [
            (NoEditTableItem('Верхняя Н. 2П'), OneCSqlTableItem(instance, 'top_guide_2', 'Номенклатура')),
            (NoEditTableItem('Нижняя Н. 2П'), OneCSqlTableItem(instance, 'bottom_guide_2', 'Номенклатура')),
            (NoEditTableItem('Верхняя Н. 1П'), OneCSqlTableItem(instance, 'top_guide_1', 'Номенклатура')),
            (NoEditTableItem('Нижняя Н. 1П'), OneCSqlTableItem(instance, 'bottom_guide_1', 'Номенклатура')),
            (NoEditTableItem('Ходовой'), OneCSqlTableItem(instance, 'top_movable_guide', 'Номенклатура')),
            (NoEditTableItem('Накладка'), OneCSqlTableItem(instance, 'decorative_guide', 'Номенклатура')),
            (NoEditTableItem('Заглушка'), OneCSqlTableItem(instance, 'plug', 'Номенклатура')),
            (NoEditTableItem('Верхний Г.'), OneCSqlTableItem(instance, 'top_horizontal', 'Номенклатура')),
            (NoEditTableItem('Нижний Г.'), OneCSqlTableItem(instance, 'bottom_horizontal', 'Номенклатура')),
            (NoEditTableItem('Вертикальный'), OneCSqlTableItem(instance, 'vertical', 'Номенклатура')),
            (NoEditTableItem('Уплотнитель'), OneCSqlTableItem(instance, 'sealant', 'Номенклатура')),
            (NoEditTableItem('Шлегель'), OneCSqlTableItem(instance, 'shlegel', 'Номенклатура')),
            (NoEditTableItem('Ролики'), OneCSqlTableItem(instance, 'wheels', 'Номенклатура')),
        ]
        for i, row in enumerate(params):
            for j, item in enumerate(row):
                self._ui.tbl_profile_1c.setItem(i, j, item)

    def current_model(self):
        if self.cur_controller is not None:
            print("-" * 20, self.cur_controller)
            return self.cur_controller.model()
        else:
            print("-" * 20, self._ui.tabWidget.currentIndex())
            return [ProfileData, RigelData, None][self._ui.tabWidget.currentIndex()]()

    def add_row(self):
        print("-" * 20, self.current_model())
        self.db_session.add(self.current_model())
        self.update()

    def current_instance(self):
        match self._ui.tabWidget.currentIndex():
            case 2:
                return self._ui.table.selectedItems()[0].instance
            case 1:
                return self.db_session.query(RigelData).filter(
                    RigelData.id == self._ui.lst_rigel_names.currentItem().id).one()
            case 0:
                return self.db_session.query(ProfileData).filter(
                    ProfileData.id == self._ui.lst_profile_names.currentItem().id).one()

    def show_table_context_menu(self, _):
        menu = QMenu(self._widget)
        instance = self.current_instance()
        (menu.addAction("Восстановить" if instance.on_delete else "На удаление")).triggered.connect(
            lambda *, i=instance: self.delete_or_restore(i)
        )
        (menu.addAction("Добавить")).triggered.connect(self.add_row)
        menu.exec(QCursor().pos())

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
        self.update()

    def update(self):
        if self.cur_controller is not None:
            self.cur_controller.enable(None, *self.get_filters(self.cur_controller.model))

        elif self._ui.tabWidget.currentIndex() == 1:
            self.open_rigel_menu(reopen_session=False)

        elif self._ui.tabWidget.currentIndex() == 2:
            pass

    def open_config_menu(self, *, reopen_session=True):
        if reopen_session:
            self.db_session.close()
            self.db_session = Database.Session()

        self.cur_controller = None
        self._ui.tabWidget.setCurrentIndex(3)
        self.clear_tabs()

        for config_name, in (
                self.db_session.query(Config1cData.config_name.distinct())
                        .all()

        ):
            self._ui.lst_config_names.addItem(SearchListItem((0, config_name)))

    def open_config_name(self, config_item: SearchListItem):
        self._ui.tbl_config_1c.clear()
        self._ui.lst_config_params.clear()

        for config_value, config_id in (
                self.db_session.query(Config1cData.config_value, Config1cData.config_id)
                        .filter(Config1cData.config_name == config_item.data_tuple[1])
                        .order_by(Config1cData.id.desc())
                        .all()

        ):
            self._ui.lst_config_params.addItem(SearchListItem((config_id, config_value)))

    def open_config_pare(self, config_item: SearchListItem):
        if (cur_item := self._ui.lst_config_names.currentItem()) is None:
            return

        config_name = cur_item.data_tuple[1]
        self._ui.tbl_config_1c.clear()
        self._ui.tbl_config_1c.setRowCount(0)

        # noinspection PyTypeChecker
        for config in (
                self.db_session.query(Config1cData)
                        .filter(
                    Config1cData.config_name == config_name,
                    Config1cData.config_id == config_item.id
                ).all()
        ):
            self._ui.tbl_config_1c.insertRow(0)
            self._ui.tbl_config_1c.setItem(0, 0, SqlTableItem(config, 'one_c_id'))
