from abc import abstractmethod

from PySide6.QtWidgets import QWidget
from sqlalchemy.orm import declarative_base

from app.controller.funcs import setup_ui


class TableRow(QWidget):
    model_type: declarative_base

    def __init__(self, model: declarative_base):
        super().__init__()
        self._model = model
        self._setup_ui()

    def new(self):
        return type(self)(self.model_type())

    @abstractmethod
    def _setup_ui(self):
        pass

    @abstractmethod
    def _update_model(self):
        pass

    @classmethod
    @abstractmethod
    def header_text(cls) -> ():
        pass

    @property
    def model(self):
        self._update_model()
        return self._model
