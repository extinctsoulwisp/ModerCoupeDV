from app.ui.ui_search_dialog import Ui_Dialog
from . import SearchDialog
from .. import confirm_decorator
from ..list_items import SearchListItem
from ...model import App, Color
from ...model.orm import Database, ColorData


class ColorSearchDialog(SearchDialog):
    def __init__(self, app: App):
        super().__init__(app)
        self._ui: Ui_Dialog = Ui_Dialog()
        self._app: App = app

        self._ui.setupUi(self._dialog)
        self._connect_triggers()

    @property
    def selected_id(self):
        return self._ui.search_list.selectedItems()[0].id

    def _connect_triggers(self):
        self._ui.inp_search.textChanged.connect(self._update_list)
        self._ui.btn_add_to_db.clicked.connect(self._add_to_db)
        self._ui.search_list.doubleClicked.connect(self._dialog.accept)

    def _update_list(self):
        color = self._ui.inp_search.text()
        with Database.Session() as session:
            if color and session.query(ColorData).filter(ColorData.name.ilike(color)).first() is None:
                self._ui.btn_add_to_db.setEnabled(True)
            else:
                self._ui.btn_add_to_db.setEnabled(False)
        self._ui.search_list.clear()
        for color_preview in self._app.search_colors(color):
            self._ui.search_list.addItem(SearchListItem(color_preview))

    @confirm_decorator("Уверены, что хотите внести новый цвет?")
    def _add_to_db(self):
        color_name = self._ui.inp_search.text()
        Color.add_to_db(color_name)
        self._update_list()
