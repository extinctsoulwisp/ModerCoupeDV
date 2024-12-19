import sys

from PySide6.QtGui import QIcon

from app.controller import AppController, error_box
from app.controller.tabs import OrderTab, SearchTab
from app.controller.tabs.admin_search_tab import AdminSearchTab
from app.controller.tabs.admin_settings_tab import AdminSettingsTab
from app.controller.tabs.tables_tab import DataTab
from app.model.orm import Database


class AdminAppController(AppController):

    def start(self, creatable=False):
        self._window.showMaximized()
        self._ui.user.setText(self._app.user_name)
        if error := Database.test_connection():
            error_box(error)
        else:
            self.add_tab(SearchTab(self._app, self) if creatable else AdminSearchTab(self._app, self))
            self.add_tab(DataTab(self._app, self))
        self.add_tab(tab := AdminSettingsTab(self._app, self))
        self.open_tab(tab)
        sys.exit(self._ui_app.exec())
