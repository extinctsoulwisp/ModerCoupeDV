from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget


class Tab:
    def __init__(self, icon_path: str, name: str, app, ui_app, _id: int):
        from ..list_items import TabListItem
        from .. import AppController

        self._icon: QIcon = QIcon(icon_path)
        self._name: str = name
        self._widget: QWidget = QWidget()
        self._app = app
        self._ui_app: AppController = ui_app
        self._list_item: TabListItem = TabListItem(self)
        self._id = _id

    @property
    def list_item(self):
        return self._list_item

    @property
    def icon(self):
        return self._icon

    @property
    def name(self):
        return self._name

    @property
    def widget(self):
        return self._widget

    @property
    def id(self):
        return self._id
