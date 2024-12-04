from PySide6.QtWidgets import QListWidgetItem


class SearchListItem(QListWidgetItem):
    def __init__(self, search_preview: tuple):
        self.id: int = search_preview[0]
        self.data_tuple = search_preview
        super().__init__(f"<{search_preview[0]}> {search_preview[1]}")
