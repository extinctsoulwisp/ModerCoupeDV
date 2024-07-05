
from PySide6.QtWidgets import QLayoutItem, QSpinBox, QDateEdit, QDoubleSpinBox


def clear_layout(layout):
    while layout.count():
        item: QLayoutItem = layout.takeAt(0)
        if item.widget():
            item.widget().deleteLater()
        elif item.layout():
            clear_layout(item.layout())


def setup_ui(ui):
    for name, attr in ui.__dict__.items():
        if isinstance(attr, (QSpinBox, QDateEdit, QDoubleSpinBox)):
            attr.wheelEvent = None
