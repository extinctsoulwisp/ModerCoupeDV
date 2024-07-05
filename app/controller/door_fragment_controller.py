from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from app.model import DoorFragment


class DoorFragmentController:
    def __init__(self, door_fragment: DoorFragment):
        self._widget: QLabel = QLabel()
        self._door_fragment: DoorFragment = door_fragment
        self._is_selected: bool = False

    def update(self):
        print(self._widget.isVisible(), 123)
        self._widget.setVisible(not self._door_fragment.fragment_container)
        self._widget.setText(self.text)
        self._widget.setToolTip(self.text)
        self._widget.setStyleSheet(f"background-color: {self._color}; border: 1px solid black;")
        # pixmap = QPixmap("m.webp")
        # self._widget.setPixmap(pixmap)
        # self._widget.setScaledContents(True)

    def delete(self):
        self._widget.deleteLater()
        del self

    @property
    def widget(self):
        return self._widget

    @property
    def text(self):
        return (f"№{self._door_fragment.number_in_scheme} {self._door_fragment.material_name}\n"
                f"{self._door_fragment.visible_height}\nx\n{self._door_fragment.visible_width}")

    @property
    def _color(self):
        if self._is_selected:
            return 'rgb(38, 165, 154)'
        elif self._door_fragment.material is None:
            return '#f1f4f9'
        elif self._door_fragment.is_have_sealant:
            return 'rgb(175,238,238)'
        else:
            return 'rgb(250, 150, 70)'

    @property
    def door_fragment(self):
        return self._door_fragment

    @property
    def is_selected(self):
        return self._is_selected

    @is_selected.setter
    def is_selected(self, value: int):
        self._is_selected = value

    @property
    def x(self):
        return self._door_fragment.x

    @property
    def y(self):
        return self._door_fragment.y
