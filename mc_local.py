from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from app.controller.admin_app_controller import AdminAppController
from app.model import AdminApp
from app.model.orm import Database

Database.init_local()
app = AdminAppController(AdminApp(), QApplication())
app._ui.company_name.setText("ПРЯМОЙ УГОЛ")
app._ui.logo.setIcon(QIcon('icons/logo_pu.png'))
app.start(creatable=True)
