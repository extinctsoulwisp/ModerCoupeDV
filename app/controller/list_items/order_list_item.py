from PySide6.QtWidgets import QTableWidgetItem


class OrderTableItem(QTableWidgetItem):
    def __init__(self, text, order_id):
        super().__init__(text)
        self.id = order_id
