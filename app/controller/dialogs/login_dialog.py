import sys

from app.controller.dialogs.dialog import Dialog
from app.ui import Ui_LoginDialog


class LoginDialog(Dialog):
    def __init__(self, app, admin_app):
        super().__init__()
        self._ui: Ui_LoginDialog = Ui_LoginDialog()
        self._app = app
        self._admin_app = admin_app

        self._setup()

    @property
    def is_login_as_user(self):
        return self._ui.ch_login_as_user.isChecked()

    def login(self):
        if self.is_login_as_user:
            password = self._ui.inp_password.text()
            user_password = self._ui.inp_user_password.text()
            if error_text := self._app.login(password, user_password):
                self._ui.error_text.setText(error_text)
            else:
                self._dialog.accept()
        else:
            password = self._ui.inp_password.text()
            if error_text := self._admin_app.login(password.encode(), b""):
                self._ui.error_text.setText(error_text)
            else:
                self._dialog.accept()

    def switch_login_as(self):
        if self.is_login_as_user:
            self._ui.ch_login_as_user.setText("Войти как администратор")
            self._ui.inp_password.setPlaceholderText("Пароль")
            self._ui.inp_user_password.setVisible(True)
        else:
            self._ui.ch_login_as_user.setText("Войти как пользователь")
            self._ui.inp_password.setPlaceholderText("Пароль администратора")
            self._ui.inp_user_password.setVisible(False)

    def _setup(self):
        self._ui.setupUi(self._dialog)
        self._ui.btn_login.clicked.connect(self.login)
        self._dialog.rejected.connect(sys.exit)
        self._ui.ch_login_as_user.clicked.connect(self.switch_login_as)
