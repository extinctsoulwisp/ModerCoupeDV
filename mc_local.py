from PySide6.QtWidgets import QApplication
from app.controller.admin_app_controller import AdminAppController
from app.model import AdminApp
from app.model.orm import Database

Database.init_local()
AdminAppController(AdminApp(), QApplication()).start(creatable=True)
