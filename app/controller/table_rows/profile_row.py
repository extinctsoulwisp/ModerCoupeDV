from app.controller.funcs import setup_ui
from app.controller.table_rows.table_row import TableRow
from app.model.orm import UserData, ProfileData
from app.ui.ui_profile_line import Ui_Form


class ProfileRow(TableRow):

    _model: ProfileData
    model_type = ProfileData

    def __init__(self, model: UserData):
        self._ui = Ui_Form()
        super().__init__(model)

    @classmethod
    def header_text(cls) -> ():
        return ("Название", "Тип", "Перехлест", "Направляющая", "Уплотнитель", "Шлегель", "Ширина В.", "Глубина В.",
                "Высота Г.В.", "Высота Г.Н.", "Глубина Г.В.", "Глубина Г.Н.")

    def _setup_ui(self):
        super()._setup_ui()
        self._ui.setupUi(self)
        setup_ui(self._ui)
        self._ui.is_open.toggled.connect(
            lambda: self._ui.is_open.setText("ОТКРЫТЫЙ" if self._ui.is_open.isChecked() else "ЗАКРЫТЫЙ"))

        if self._model.id:
            self._ui.i_name.setText(self._model.name)
            self._ui.is_open.setChecked(self._model.is_open)
            self._ui.is_open.setText("ОТКРЫТЫЙ" if self._ui.is_open.isChecked() else "ЗАКРЫТЫЙ")
            self._ui.overlap.setValue(self._model.overlap)
            self._ui.guide.setValue(self._model.guide)
            self._ui.sealant.setValue(self._model.sealant)
            self._ui.shlegel.setValue(self._model.shlegel)
            self._ui.v_depth.setValue(self._model.v_depth)
            self._ui.h_bot_depth.setValue(self._model.h_bot_depth)
            self._ui.h_top_depth.setValue(self._model.h_top_depth)

            self._ui.v_width.setValue(self._model.v_width)
            self._ui.h_top_width.setValue(self._model.h_top_width)
            self._ui.h_bot_width.setValue(self._model.h_bot_width)

    def _update_model(self):
        self._model.name = self._ui.i_name.text()
        self._model.is_open = self._ui.is_open.isChecked()
        self._model.guide = self._ui.guide.value()
        self._model.overlap = self._ui.overlap.value()
        self._model.sealant = self._ui.sealant.value()
        self._model.shlegel = self._ui.shlegel.value()
        self._model.v_depth = self._ui.v_depth.value()
        self._model.h_top_depth = self._ui.h_top_depth.value()
        self._model.h_bot_depth = self._ui.h_bot_depth.value()

        self._model.v_width = self._ui.v_width.value()
        self._model.h_top_width = self._ui.h_top_width.value()
        self._model.h_bot_width = self._ui.h_bot_width.value()
