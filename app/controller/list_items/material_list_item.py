from PySide6.QtWidgets import QListWidgetItem


class MaterialListItem(QListWidgetItem):
    def __init__(self, search_preview: tuple):
        self.id: int = search_preview[0]
        super().__init__(f"{'□' if search_preview[2] else '  '} <{search_preview[0]}> {search_preview[1]}")
