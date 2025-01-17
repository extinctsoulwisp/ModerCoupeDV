from abc import abstractmethod

from . import Dialog
from ...model import App
from ...ui.ui_search_dialog import Ui_Dialog


class SearchDialog(Dialog):
    def __init__(self, app: App):
        super().__init__()
        self._ui: Ui_Dialog = Ui_Dialog()
        self._app: App = app

    @property
    def selected_id(self):
        return self._ui.search_list.selectedItems()[0].id

    def exec(self):
        self._update_list()
        return super().exec()

    @abstractmethod
    def _update_list(self): ...
