import sys
from typing import List

from PySide6.QtWidgets import QApplication, QMainWindow

from app.ui import Ui_MainWindow
from . import clear_layout, confirm_decorator
from .tabs import Tab, SearchTab


class AppController:
    def __init__(self, app, ui_app: QApplication):
        self._app = app
        self._ui_app = ui_app
        self._window = QMainWindow()
        self._ui = Ui_MainWindow()

        self._tabs: List[Tab] = []

        self._setup()

    def start(self):
        self._window.showMaximized()
        self._ui.user.setText(self._app.user_name)
        search_tab = SearchTab(self._app, self)
        self.add_tab(search_tab)
        self.open_tab(search_tab)
        sys.exit(self._ui_app.exec())

    def add_tab(self, tab: Tab):
        for _tab in self._tabs:
            if _tab.id == tab.id:
                self.open_tab(_tab)
                return False
        self._tabs.append(tab)
        self._ui.tabs.addItem(tab.list_item)
        self._ui.central_widget.layout().addWidget(tab.widget)
        tab.widget.setVisible(False)
        return True

    def open_tab(self, cur_tab: Tab):
        for tab in self._tabs:
            if tab is not cur_tab:
                tab.widget.setVisible(False)

        cur_tab.widget.setVisible(True)
        self._ui.tabs.setCurrentItem(cur_tab.list_item)

        from app.controller.tabs import OrderTab
        if isinstance(cur_tab, SearchTab):
            cur_tab.update_orders_list()

        elif isinstance(cur_tab, OrderTab):
            cur_tab.list_item.setText(str(cur_tab.order.visible_number))

    @confirm_decorator("Закрыть вкладку? Несохраненные изменения будут утеряны.")
    def close_tab(self, cur_tab: Tab):
        self._ui.tabs.takeItem(self._ui.tabs.row(cur_tab.list_item))
        self.open_tab(self._tabs[0])
        clear_layout(cur_tab.widget.layout())
        cur_tab.widget.deleteLater()
        self._tabs.remove(cur_tab)

    def refresh_order(self, order):
        from app.controller.tabs import OrderTab
        order: OrderTab
        order_id = order.order.id
        self.close_tab(order, confirm=False)
        order_tab = OrderTab(self._app, self, self._app.get_order_by_id(order_id))
        self.add_tab(order_tab)
        self.open_tab(order_tab)

    def _setup(self):
        self._ui.setupUi(self._window)
        self._ui.tabs.itemClicked.connect(lambda li: self.open_tab(li.tab))
