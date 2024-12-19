from PySide6.QtWidgets import QWidget

from app.ui import Ui_door


class DoorController:
    def __init__(self, door):
        from app.controller import DoorFragmentController
        self._widget: QWidget = QWidget()
        self._ui: Ui_door = Ui_door()
        self._door = door
        self._fragments = [DoorFragmentController(fragment) for fragment in door.fragments]
        self._ui.setupUi(self._widget)

    def update(self):
        self._ui.width.setText(str(self._door.visible_width))

    @property
    def fragments(self):
        return self._fragments

    @property
    def widget(self):
        return self._widget

    @property
    def door(self):
        return self._door

    @property
    def ui(self):
        return self._ui

    def delete(self):
        self._widget.deleteLater()
        for fragment in self._fragments:
            fragment.delete()
