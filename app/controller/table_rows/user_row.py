from PySide6.QtWidgets import QSpinBox

from app.controller.funcs import setup_ui
from app.controller.table_rows.table_row import TableRow
from app.model.orm import UserData
from app.ui.ui_user_line import Ui_Form


class UserRow(TableRow):
    @classmethod
    def header_text(cls) -> ():
        return "Имя", "Номер (Уникальный)", "Пароль (Уникальный)"

    _model: UserData
    model_type = UserData

    def __init__(self, model: UserData):
        self._ui = Ui_Form()
        super().__init__(model)

    def _setup_ui(self):
        super()._setup_ui()
        self._ui.setupUi(self)

        if self._model.id:
            self._ui.i_name.setText(self._model.name)
            self._ui.i_password.setText(self._model.password)
            self._ui.i_number.setValue(self._model.number)

    def _update_model(self):
        self._model.number = self._ui.i_number.value()
        self._model.name = self._ui.i_name.text()
        self._model.password = self._ui.i_password.text()
