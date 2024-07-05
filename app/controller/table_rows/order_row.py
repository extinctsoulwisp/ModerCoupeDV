from app.controller.funcs import setup_ui
from app.controller.table_rows.table_row import TableRow
from app.ui.ui_order_line import Ui_Form


class OrderRow(TableRow):
    def __init__(self, order_tuple: tuple, slot):
        self._ui = Ui_Form()
        self._id = order_tuple[0]
        self._data = order_tuple
        self._slot = slot
        super().__init__(None)

    @classmethod
    def header_text(cls) -> ():
        return "Дата", "Покупатель", "Описание", "Номер", "Профиль"

    def _setup_ui(self):
        self._ui.setupUi(self)
        setup_ui(self._ui)
        self.mouseDoubleClickEvent = self._slot

        self._ui.create_date.setText(str(self._data[1]))
        self._ui.customer.setText(self._data[2])
        self._ui.description.setText(self._data[3])
        self._ui.number.setText(self._data[4])
        self._ui.profile.setText(self._data[5])

    def _update_model(self):
        pass
