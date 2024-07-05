from datetime import datetime
from enum import Enum
from typing import Optional, Callable

from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QColor
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMenu
from sqlalchemy import Column, func, String

from app.controller import error_box, input_box
from app.model.decryptor import password_decrypt, password_encrypt
from app.model.orm import Database


class SqlTableItem(QTableWidgetItem):
    def __init__(self, instance: Database.Base, attr: str, type_in: Callable = str):
        super().__init__(type_in(instance[attr]))
        self.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
        self.instance = instance
        self.attr = attr

        if instance.on_delete:
            self.setBackground(QColor(231, 99, 68, 100))

    def item_double_clicked(self):
        pass


NoEditSqlTableItem = SqlTableItem


class DateSqlTableItem(SqlTableItem):
    def __init__(self, instance: Database.Base, attr: str):
        super().__init__(instance, attr, type_in=lambda i: i.strftime("%d.%m.%Y"))
        self.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable)

    def setData(self, role, value):
        if role == Qt.EditRole:
            try:
                self.instance[self.attr] = datetime.strptime(value, "%d.%m.%Y")
            except Exception as e:
                error_box(str(e))
        super().setData(role, value)


class StrSqlTableItem(SqlTableItem):
    def __init__(self, instance: Database.Base, attr: str):
        super().__init__(instance, attr)
        self.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable)

    def setData(self, role, value):
        if role == Qt.EditRole:
            try:
                self.instance[self.attr] = str(value)
            except Exception as e:
                error_box(str(e))
        super().setData(role, value)


class NumSqlTableItem(SqlTableItem):
    def __init__(self, instance: Database.Base, attr: str):
        super().__init__(instance, attr)
        self.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable)

    def setData(self, role, value):
        if role == Qt.EditRole:
            try:
                value = float(value)
                if value.is_integer():
                    value = int(value)
                self.instance[self.attr] = value
            except Exception as e:
                error_box(str(e))
        super().setData(role, value)


class NoEditIterableSqlTableItem(SqlTableItem):
    def __init__(self, instance: Database.Base, attr: str):
        super().__init__(instance, attr, type_in=lambda value: ', '.join(str(v.name) for v in value))


class NoEditWaybillSqlTableItem(SqlTableItem):
    def __init__(self, instance: Database.Base, attr: str):
        super().__init__(instance, attr, type_in=lambda value: f"{instance.id} от {value:%d.%m.%Y %H:%M}")


class EmptySqlTableItem(SqlTableItem):
    def __init__(self, instance: Database.Base, *_):
        super().__init__(instance, 'id', type_in=lambda value: "")


class NoEditBoolSqlTableItem(SqlTableItem):
    def __init__(self, instance: Database.Base, attr: str):
        super().__init__(instance, attr, type_in=lambda value: 'Да' if value else 'Нет')


class BoolSqlTableItem(NoEditBoolSqlTableItem):
    def setData(self, role, value):
        if role == Qt.EditRole:
            try:
                self.instance[self.attr] = value
            except Exception as e:
                error_box(str(e))
        super().setData(role, "Да" if value else "Нет")

    def item_double_clicked(self):
        menu = QMenu()
        (menu.addAction("Да")).triggered.connect(lambda *_, v=True: self.setData(Qt.EditRole, v))
        (menu.addAction("Нет")).triggered.connect(lambda *_, v=False: self.setData(Qt.EditRole, v))
        menu.exec(QCursor().pos())


class EnumSqlTaleItem(SqlTableItem):
    def __init__(self, instance: Database.Base, attr: str):
        super().__init__(instance, attr, type_in=lambda i: i.value)
        self.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)

    def setData(self, role, value):
        if role == Qt.EditRole:
            try:
                self.instance[self.attr] = value
            except Exception as e:
                error_box(str(e))
        super().setData(role, value.value)

    def item_double_clicked(self):
        menu = QMenu()
        for enum in type(self.instance[self.attr]):
            (menu.addAction(enum.value)).triggered.connect(lambda *_, v=enum: self.setData(Qt.EditRole, v))
        menu.exec(QCursor().pos())


class EncryptedSqlTableItem(SqlTableItem):
    def __init__(self, instance: Database.Base, attr: str):
        super().__init__(instance, attr, type_in=lambda i: "*" * 8)
        self.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)

    def setData(self, role, value):
        if role == Qt.EditRole:
            try:
                self.instance[self.attr] = value
            except Exception as e:
                error_box(str(e))
        super().setData(role, "*" * 8)

    def item_double_clicked(self):
        if result := input_box("Старый пароль", "Новый пароль", password_type=True):
            old_password, new_password = result
        else:
            return
        decrypted_old = password_decrypt(self.instance[self.attr], old_password.encode())
        encrypted_new = password_encrypt(decrypted_old, new_password.encode())
        self.setData(Qt.EditRole, encrypted_new)


class SQLTableController:
    class SQLTableColumn:
        def __init__(self, attr: str, header: str, item: type[SqlTableItem] = NoEditSqlTableItem,
                     column: Column = None):
            self.attr = attr
            self.header = header
            self._column = column
            self.item = item

        def get_item(self, instance: Database.Base):
            return self.item(instance, self.attr)

        def get_column(self, model: type[Database.Base]):
            return self._column if self._column else getattr(model, self.attr)

    def __init__(self,
                 table: QTableWidget,
                 name: str,
                 model: type[Database.Base],
                 id_column: Column,
                 *columns: SQLTableColumn,
                 query_func=None):
        self.name = name
        self._id_column = id_column
        self._model = model
        self.columns: tuple["SQLTableController.SQLTableColumn"] = tuple(columns)
        self._query_func = query_func

        self._last_rowid: int = 0
        self._table = table
        self._search_by: Optional[Column] = None
        self._search_text: str = ""
        self._limit = 0

    @classmethod
    def from_model(cls,
                   table_widget: QTableWidget,
                   model: type[Database.Base]
                   ):
        cols = []
        for col in model.__table__.columns:
            col: Column
            if col.name == 'id':
                continue
            elif col.type.python_type in (int, float, bool):
                cols.append(cls.SQLTableColumn(col.name, col.name, NumSqlTableItem))
            elif col.type.python_type is datetime.date:
                cols.append(cls.SQLTableColumn(col.name, col.name, DateSqlTableItem))
            elif col.type.python_type is str:
                cols.append(cls.SQLTableColumn(col.name, col.name, StrSqlTableItem))
            elif issubclass(col.type.python_type, Enum):
                cols.append(cls.SQLTableColumn(col.name, col.name, EnumSqlTaleItem))
            else:
                cols.append(cls.SQLTableColumn(col.name, col.name))
        return cls(table_widget, model.__tablename__, model, model.id, *cols)

    def enable(self, query_func=None, *filters):
        self._last_rowid: int = 0
        if query_func is not None:
            self._query_func = query_func

        self._table.clear()
        self._table.setRowCount(0)
        self._table.setColumnCount(len(self.columns))
        self._table.setHorizontalHeaderLabels([c.header for c in self.columns])
        self._table.resizeColumnsToContents()

        rows = []
        for row in (self._query_func.filter(self._model.id > self._last_rowid, *filters).order_by(self._model.id.desc()).all()
        ):
            if row.id > self._last_rowid:
                self._last_rowid = row.id
            rows.append(row)

        for row in sorted(rows, key=lambda instance: instance.id):
            self._table.insertRow(0)
            self._table.setVerticalHeaderItem(0, QTableWidgetItem(str(row.id)))

            for i, column in enumerate(self.columns):
                self._table.setItem(0, i, column.get_item(row))

        self.resize_columns()

    def resize_columns(self):
        for i, col in enumerate(self.columns):
            if col.item is not NoEditIterableSqlTableItem:
                self._table.resizeColumnToContents(i)

    def update(self, with_query):
        for row in with_query:
            self._table.insertRow(0)
            self._table.setVerticalHeaderItem(0, QTableWidgetItem(str(row.id)))
            self._last_rowid = row.id

            for i, column in enumerate(self.columns):
                self._table.setItem(0, i, column.get_item(row))

        self.resize_columns()

    @property
    def model(self):
        return self._model
