from PySide6.QtWidgets import QListWidgetItem


class TabListItem(QListWidgetItem):
    def __init__(self, tab):
        from ..tabs import Tab
        super().__init__(tab.icon, tab.name)
        self._tab: Tab = tab

    @property
    def tab(self):
        return self._tab
