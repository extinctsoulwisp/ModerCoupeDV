from app.controller.funcs import setup_ui
from app.controller.table_rows.table_row import TableRow
from app.model.orm import MaterialData
from app.ui.ui_material_line import Ui_Form


class MaterialRow(TableRow):
    @classmethod
    def header_text(cls) -> ():
        return "Название + уплотнитель",

    _model: MaterialData
    model_type = MaterialData

    def __init__(self, model: MaterialData):
        self._ui = Ui_Form()
        super().__init__(model)

    def _setup_ui(self):
        super()._setup_ui()
        self._ui.setupUi(self)
        setup_ui(self._ui)
        self._ui.ch_need_sealant.toggled.connect(lambda: self._ui.ch_need_sealant.setText(
            "С уплотнителем" if self._ui.ch_need_sealant.isChecked() else "Без уплотнителя"))

        if self._model.id:
            self._ui.i_name.setText(self._model.name)
            self._ui.ch_need_sealant.setChecked(self._model.is_have_sealant)
            self._ui.ch_need_sealant.setText(
                "С уплотнителем" if self._ui.ch_need_sealant.isChecked() else "Без уплотнителя")

    def _update_model(self):
        self._model.name = self._ui.i_name.text()
        self._model.is_have_sealant = self._ui.ch_need_sealant.isChecked()
