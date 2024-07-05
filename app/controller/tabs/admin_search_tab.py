from . import SearchTab


class AdminSearchTab(SearchTab):
    def _setup(self):
        super()._setup()
        self._ui.btn_create.deleteLater()

    def _create_order(self):
        pass
