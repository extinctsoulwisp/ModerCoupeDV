from PySide6.QtWidgets import QTreeWidgetItem


class OneCSearchTreeItem(QTreeWidgetItem):
    def __init__(self, search_preview: tuple, is_category=False):
        self.id: int | None = search_preview[0]
        self.data_tuple = search_preview
        self.is_category = is_category

        title = f"{search_preview[1]}" if is_category else f"<{search_preview[0]}> {search_preview[1]}"
        super().__init__([title])

