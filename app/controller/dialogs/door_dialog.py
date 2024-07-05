from PySide6 import QtWidgets
from PySide6.QtGui import QRegularExpressionValidator

from app.ui import Ui_door_edit_dialog
from . import Dialog
from ...model import Door


class DoorDialog(Dialog):
    def __init__(self, door: Door = None):
        super().__init__()
        self._ui: Ui_door_edit_dialog = Ui_door_edit_dialog()
        self._door = door

        self._setup()

    @property
    def cols_count(self):
        return self._ui.i_cols_count.value()

    @property
    def rows_count(self):
        return self._ui.i_rows_count.value()

    @property
    def rows_sizes(self):
        if self.rows_count < 13:
            for i in range(1, self.rows_count + 1):
                yield int(t) if (t := self._ui.fragments_frame.layout().itemAtPosition(i, 0).widget().text()) else 0

    @property
    def cols_sizes(self):
        if self.cols_count < 13:
            for j in range(1, self.cols_count + 1):
                yield int(t) if (t := self._ui.fragments_frame.layout().itemAtPosition(0, j).widget().text()) else 0

    @property
    def door_width(self):
        return int(t) if (t := self._ui.i_width.text()) else 0

    @property
    def is_h_main_rigel(self):
        return self._ui.ch_h_main_rigel.isChecked()

    def _update(self, cols_count: int = None, rows_count: int = None):
        if cols_count:
            self._ui.i_cols_count.setValue(cols_count)
        if rows_count:
            self._ui.i_rows_count.setValue(rows_count)

        for i in range(1, 13):
            for j in range(1, 13):
                widget: QtWidgets.QWidget = self._ui.fragments_frame.layout().itemAtPosition(i, j).widget()
                if i > self.rows_count or j > self.cols_count:
                    widget.setStyleSheet(f"background-color: {'transparent' if self._door else 'rgb(38, 165, 154)'};")
                else:
                    widget.setStyleSheet("background-color: rgb(241, 244, 249);")

        if self.cols_count > 12:
            for i in range(1, 13):
                for j in range(2, 13):
                    self._ui.fragments_frame.layout().itemAtPosition(i, j).widget().setStyleSheet(
                        'background-color: transparent;')

        if self.rows_count > 12:
            for i in range(2, 13):
                for j in range(1, 13):
                    self._ui.fragments_frame.layout().itemAtPosition(i, j).widget().setStyleSheet(
                        'background-color: transparent;')

    def _setup(self):
        self._ui.setupUi(self._dialog)
        self._ui.i_width.setValidator(QRegularExpressionValidator(r"[0-9]+"))
        self._ui.ch_h_main_rigel.toggled.connect(lambda: self._ui.ch_h_main_rigel.setText(
            "Горизонтальный" if self._ui.ch_h_main_rigel.isChecked() else "Вертикальный"
        ))
        self._ui.i_cols_count.valueChanged.connect(lambda : self._update())
        self._ui.i_rows_count.valueChanged.connect(lambda: self._update())

        if self._door is None:
            for i in range(1, 13):
                for j in range(1, 13):
                    widget: QtWidgets.QWidget = self._ui.fragments_frame.layout().itemAtPosition(j, i).widget()
                    widget.mousePressEvent = lambda *_, cc=i, rc=j: self._update(cc, rc)
        else:
            self._ui.i_cols_count.setValue(self._door.cols_count)
            self._ui.i_rows_count.setValue(self._door.rows_count)
            self._ui.ch_h_main_rigel.setChecked(self._door.is_h_main_rigel)
            for i in range(1, 13):
                line: QtWidgets.QLineEdit = self._ui.fragments_frame.layout().itemAtPosition(0, i).widget()
                line.setValidator(QRegularExpressionValidator(r"[0-9]+"))
                if i > self.cols_count:
                    line.setEnabled(False)
                else:
                    line.setText(str(val) if (val := self._door.custom_cols.get(i - 1)) else "")

            for j in range(1, 13):
                line: QtWidgets.QLineEdit = self._ui.fragments_frame.layout().itemAtPosition(j, 0).widget()
                line.setValidator(QRegularExpressionValidator(r"[0-9]+"))
                if j > self.rows_count:
                    line.setEnabled(False)
                else:
                    line.setText(str(val) if (val := self._door.custom_rows.get(j - 1)) else "")

            self._ui.i_cols_count.setEnabled(False)
            self._ui.i_rows_count.setEnabled(False)
            if self._door.custom_width:
                self._ui.i_width.setText(str(self._door.custom_width))
        self._update()
