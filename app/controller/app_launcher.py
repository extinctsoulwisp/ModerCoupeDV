import sys

from PySide6.QtWidgets import QDialog, QApplication

from app.controller import AppController
from app.controller.admin_app_controller import AdminAppController
from app.controller.dialogs import LoginDialog
from app.model import App, AdminApp, admin_app


class AppLauncher:
    def __init__(self):
        self._ui_app = QApplication(sys.argv)

    def start(self):
        app, admin_app = App(), AdminApp()
        dialog = LoginDialog(app, admin_app)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            if dialog.is_login_as_user:
                AppController(app, self._ui_app).start()
            else:
                AdminAppController(admin_app, self._ui_app).start()

    def start_local(self):
        from app.model.orm import Database
        Database.init_local()
        AdminAppController(AdminApp(), self._ui_app).start(creatable=True)
