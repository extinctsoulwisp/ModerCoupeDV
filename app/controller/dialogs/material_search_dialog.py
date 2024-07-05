from PySide6.QtWidgets import QCheckBox

from app.ui.ui_search_dialog import Ui_Dialog
from . import SearchDialog
from ..list_items import SearchListItem
from ..list_items.material_list_item import MaterialListItem
from ...model import App, Material


class MaterialSearchDialog(SearchDialog):
    def __init__(self, app: App):
        super().__init__(app)
        self._ui: Ui_Dialog = Ui_Dialog()
        self._app: App = app

        self._setup()

    @property
    def selected_id(self):
        return self._ui.search_list.selectedItems()[0].id

    def _setup(self):
        self._ui.setupUi(self._dialog)
        self._ui.btn_add_to_db.setVisible(False)

        self._ui.inp_search.textChanged.connect(self._update_list)
        self._ui.search_list.doubleClicked.connect(self._dialog.accept)

    def _update_list(self):
        material_name = self._ui.inp_search.text()
        self._ui.search_list.clear()
        for material_preview in self._app.search_materials(material_name):
            self._ui.search_list.addItem(MaterialListItem(material_preview))
