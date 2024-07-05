from PySide6.QtWidgets import QDialog


class Dialog:
    def __init__(self):
        self._dialog: QDialog = QDialog()

    def exec(self):
        return self._dialog.exec()
