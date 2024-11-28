from PySide6.QtWidgets import QListWidgetItem

from app.model.orm import Database


class InstanceListItem(QListWidgetItem):
    def __init__(self, instance: Database.Base, text: str):
        self.instance: Database.Base = instance
        super().__init__(text)
