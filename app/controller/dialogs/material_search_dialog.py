from PySide6.QtWidgets import QCheckBox

from app.ui.ui_search_dialog import Ui_Dialog
from . import SearchDialog
from .. import confirm_box
from ..list_items import SearchListItem
from ..list_items.material_list_item import MaterialListItem
from ...model.orm import Database, MaterialData


class MaterialSearchDialog(SearchDialog):
    def __init__(self, app):
        super().__init__(app)
        self._ui: Ui_Dialog = Ui_Dialog()
        self._app = app

        self._setup()

    @property
    def selected_id(self):
        return self._ui.search_list.selectedItems()[0].id

    def _setup(self):
        self._ui.setupUi(self._dialog)
        self._ui.btn_add_to_db.setEnabled(False)
        self._dialog.geometry().setWidth(1000)

        self._ui.inp_search.textChanged.connect(self._update_list)
        self._ui.search_list.doubleClicked.connect(self._dialog.accept)
        self._ui.btn_add_to_db.clicked.connect(self.add_to_db)

    def add_to_db(self):
        material_name = self._ui.inp_search.text()
        need_sealant = confirm_box('Нужен уплотнитель?')
        if confirm_box(
                f'Внести в базу материал "{material_name}" {"с уплотнителем" if need_sealant else "без уплотнителя"}?'
        ):
            from app.model import Material
            Material.add_to_db(material_name, need_sealant)
            self._update_list()

    def _update_list(self):
        material_name = self._ui.inp_search.text()
        self._ui.search_list.clear()

        for material_preview in self._app.search_materials(material_name):
            self._ui.search_list.addItem(MaterialListItem(material_preview))

        with Database.Session() as session:
            if material_name and session.query(MaterialData.name).filter(
                    MaterialData.name.ilike(material_name)).first() is None:
                self._ui.btn_add_to_db.setEnabled(True)
            else:
                self._ui.btn_add_to_db.setEnabled(False)
