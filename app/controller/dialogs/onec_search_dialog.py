from abc import abstractmethod

from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QMenu

from app.model.orm import Database, Nomenclature1cData
from . import Dialog
from ..list_items.onec_tree_widget import OneCSearchTreeItem
from ...ui.ui_search_dialog_new import Ui_Dialog


class OneCSearchDialog(Dialog):
    def __init__(self, app, saved_as=""):
        super().__init__()
        self._ui: Ui_Dialog = Ui_Dialog()
        self._app = app
        self._saved_as = saved_as

        self._ui.setupUi(self._dialog)
        self._connect_triggers()

        self._material_id = None
        self._tape_id = None

    def _connect_triggers(self):
        self._ui.inp_search.textChanged.connect(self._update_list)
        self._ui.search_list.itemClicked.connect(self.item_double_clicked)
        self._ui.saved_list.itemClicked.connect(self.item_double_clicked)
        self._ui.search_list.customContextMenuRequested.connect(self.search_menu)

        self._ui.r_material.clicked.connect(self.change_r_view)
        self._ui.r_tape.clicked.connect(self.change_r_view)
        self._ui.r_sealant.clicked.connect(lambda: (
            self._ui.r_sealant.setText("Да" if self._ui.r_sealant.isChecked() else "Нет")
        ))

    def search_menu(self, pos):
        menu = QMenu(self._dialog)
        menu.setStyleSheet(
            "QMenu {"
            "   margin: 0;"
            "   color: white;"
            "}"
            "QMenu::item {"
            "   padding: 5px 20px;"
            "   background-color: rgb(39, 50, 56);"
            "}"
            "QMenu::item:selected {"
            "   background-color: rgb(69, 75, 84);"
            "}"
            "QMenu::separator {"
            "   background-color: rgb(69, 75, 84);"
            "}"
        )

        action = menu.addAction("Добавить в избранное")
        menu.exec(self._ui.search_list.mapToGlobal(pos))

    def item_double_clicked(self, item: OneCSearchTreeItem):
        if item.is_category:
            return

        if self._ui.r_material.isChecked():
            self._material_id = item.id
            self._ui.r_material.setText(item.data_tuple[1])
        else:
            self._tape_id = item.id
            self._ui.r_tape.setText(item.data_tuple[1])

    def change_r_view(self):
        if self._ui.r_material.isChecked():
            self._ui.r_material.setText("Нет")
            self._material_id = None

            font = self._ui.r_material.font()
            font.setUnderline(True)
            self._ui.r_material.setFont(font)

            font = self._ui.r_tape.font()
            font.setUnderline(False)
            self._ui.r_tape.setFont(font)
        else:
            self._tape_id = None
            self._ui.r_tape.setText("Нет")

            font = self._ui.r_material.font()
            font.setUnderline(False)
            self._ui.r_material.setFont(font)

            font = self._ui.r_tape.font()
            font.setUnderline(True)
            self._ui.r_tape.setFont(font)

    def exec(self):
        self._update_list()
        return super().exec()

    @abstractmethod
    def _update_list(self):
        text = self._ui.inp_search.text()
        self._ui.search_list.clear()
        self._ui.saved_list.clear()

        self._ui.search_list.addTopLevelItem(
            non_category_item := OneCSearchTreeItem((None, "БЕЗ КАТЕГОРИИ"), is_category=True)
            )
        self._ui.saved_list.addTopLevelItem(saved_item := OneCSearchTreeItem((None, "Избранное"), is_category=True))
        saved_item.setExpanded(True)

        with Database.Session() as session:
            current_category = None
            current_item = non_category_item

            for (id_, name, category, saved_as) in (
                    session.query(
                        Nomenclature1cData.id,
                        Nomenclature1cData.name,
                        Nomenclature1cData.category,
                        Nomenclature1cData.save_as
                    ).filter(
                        Nomenclature1cData.name.ilike(f'%{text}%'),
                        Nomenclature1cData.on_delete == False
                    ).order_by(Nomenclature1cData.category)
                            .all()
            ):
                if saved_as == self._saved_as:
                    saved_item.addChild(OneCSearchTreeItem((id_, name)))
                    name = "⭐" + name

                if category is None:
                    non_category_item.addChild(OneCSearchTreeItem((id_, name)))
                    continue

                elif category != current_category:
                    current_category = category
                    current_item = OneCSearchTreeItem((None, category), is_category=True)
                    self._ui.search_list.addTopLevelItem(current_item)

                current_item.addChild(OneCSearchTreeItem((id_, name)))
