from app.ui.ui_search_dialog import Ui_Dialog
from . import SearchDialog
from ..list_items import SearchListItem


class RigelSearchDialog(SearchDialog):
    def __init__(self, app):
        super().__init__(app)
        self._ui: Ui_Dialog = Ui_Dialog()
        self._app = app

        self._ui.setupUi(self._dialog)
        self._ui.btn_add_to_db.setVisible(False)
        self._connect_triggers()

    @property
    def selected_id(self):
        return self._ui.search_list.selectedItems()[0].id

    def _connect_triggers(self):
        self._ui.inp_search.textChanged.connect(self._update_list)
        self._ui.search_list.doubleClicked.connect(self._dialog.accept)

    def _update_list(self):
        rigel_name = self._ui.inp_search.text()
        self._ui.search_list.clear()
        for rigel_preview in self._app.search_rigels(rigel_name):
            self._ui.search_list.addItem(SearchListItem(rigel_preview))
