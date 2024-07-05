from app.controller.funcs import setup_ui
from app.controller.table_rows.table_row import TableRow
from app.model.orm import RigelData
from app.ui.ui_rigel_line import Ui_Form


class RigelRow(TableRow):
    @classmethod
    def header_text(cls) -> ():
        return "Название", "Середина", "Глубина"

    _model: RigelData
    model_type = RigelData

    def __init__(self, model: RigelData):
        self._ui = Ui_Form()
        super().__init__(model)

    def _setup_ui(self):
        self._ui.setupUi(self)
        setup_ui(self._ui)

        if self._model.id:
            self._ui.i_name.setText(self._model.name)
            self._ui.i_center.setValue(self._model.center_width)
            self._ui.i_depth.setValue(self._model.depth)

    def _update_model(self):
        self._model.depth = self._ui.i_depth.value()
        self._model.name = self._ui.i_name.text()
        self._model.center_width = self._ui.i_center.value()
