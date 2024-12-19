from PySide6.QtWidgets import QTableWidgetItem

from app.ui import Ui_SearchTab
from . import Tab, OrderTab
from ..list_items import OrderTableItem
from ...model.orm.order_preview import OrderPreview


def num_to_str(num: int | float | None):
    if num is None:
        return ""
    num = float(num)
    if num.is_integer():
        num = int(num)
    else:
        num = round(num, 2)
    return "" if num is None else f"{num:_}".replace('.', ',').replace('_', ' ')


class SearchTab(Tab):
    def __init__(self, app, ui_app):
        super().__init__("icons/search.svg", "Поиск", app, ui_app, 0)
        self._ui: Ui_SearchTab = Ui_SearchTab()

        self._setup()

    def _setup(self):
        self._ui.setupUi(self._widget)
        self._ui.btn_search.clicked.connect(self.update_orders_list)
        self._ui.btn_update.clicked.connect(self.update_orders_list)
        self._ui.btn_create.clicked.connect(self._create_order)
        self._ui.table.itemDoubleClicked.connect(self._open_order)
        self.update_orders_list()

    def _create_order(self):
        self._app.create_order()
        self.update_orders_list()

    def update_orders_list(self):
        self._ui.table.clear()
        self._ui.table.setRowCount(0)
        self._ui.table.setHorizontalHeaderLabels(
            ("Номер", "Дата", "Клиент", "Двери", "Профиль", "Цвет", "Система", "Стоимость", "Описание")
        )

        if self._ui.r_by_date.isChecked():
            search_by = 'date'
        elif self._ui.r_by_number.isChecked():
            search_by = 'number'
        else:
            search_by = 'customer'

        for order in reversed(self._app.search_orders(
                text=self._ui.inp_search.text(),
                search_by=search_by,
                _asc=not self._ui.r_asc.isChecked(),
                limit=self._ui.inp_limit.value()
        )):
            order: OrderPreview
            self._ui.table.insertRow(0)
            self._ui.table.setItem(0, 0, OrderTableItem(order.number, order.id))
            self._ui.table.setItem(0, 1, OrderTableItem(str(order.date), order.id))
            self._ui.table.setItem(0, 2, OrderTableItem(order.customer, order.id))
            self._ui.table.setItem(0, 3, OrderTableItem(str(order.door_count), order.id))
            self._ui.table.setItem(0, 4, OrderTableItem(order.profile, order.id))
            self._ui.table.setItem(0, 5, OrderTableItem(order.color, order.id))
            self._ui.table.setItem(0, 6, OrderTableItem(order.system_, order.id))
            self._ui.table.setItem(0, 7, OrderTableItem(num_to_str(order.price), order.id))
            self._ui.table.setItem(0, 8, OrderTableItem(order.description, order.id))

        for i in range(9):
            self._ui.table.resizeColumnToContents(i)

    def _open_order(self, order_item: OrderTableItem):
        order_tab = OrderTab(self._app, self._ui_app, self._app.get_order_by_id(order_item.id))
        self._ui_app.add_tab(order_tab) and self._ui_app.open_tab(order_tab)
