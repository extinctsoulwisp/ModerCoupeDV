from PySide6.QtWidgets import QLabel, QLineEdit, QFormLayout

from app import config
from app.controller import input_box, response_decorator
from app.controller.tabs import Tab
from app.ui.ui_admin_settings import Ui_settings_tab


class AdminSettingsTab(Tab):
    def __init__(self, app, ui_app):
        super().__init__("icons/settings.svg", "Настройки", app, ui_app, -2)
        self._ui = Ui_settings_tab()
        self._settings_dict = {}

        self._setup()

    def _setup(self):
        self._ui.setupUi(self._widget)
        self.update_fields()

        self._ui.btn_save.clicked.connect(self.save_settings)

        self._ui.btn_admin.clicked.connect(self.change_admin_app_password)
        self._ui.btn_manager.clicked.connect(self.change_user_app_password)
        self._ui.btn_postgres_admin.clicked.connect(self.change_admin_db_password)
        self._ui.btn_postgres_manager.clicked.connect(self.change_user_db_password)
        self._ui.btn_archive.clicked.connect(self.archive_db)

    def update_fields(self):
        i = 0
        for section in config.sections():
            self._settings_dict[section] = {}
            self._ui.settings.layout().setWidget(i, QFormLayout.ItemRole.FieldRole, QLabel(section))
            i += 1
            for key, value in config.items(section):
                self._ui.settings.layout().setWidget(i, QFormLayout.ItemRole.LabelRole, QLabel(key))
                self._ui.settings.layout().setWidget(i, QFormLayout.ItemRole.FieldRole, line := QLineEdit(value))
                self._settings_dict[section][key] = line
                i += 1

    @response_decorator
    def save_settings(self):
        for section, content in self._settings_dict.items():
            for name, field in content.items():
                config[section][name] = field.text()
        with open('settings.ini', 'w', encoding='utf-8') as configfile:
            config.write(configfile)

    @response_decorator
    def change_admin_app_password(self):
        if passwords := input_box("Старый пароль", "Новый пароль", password_type=True):
            self._app.change_admin_app_password(*passwords)

    @response_decorator
    def change_user_app_password(self):
        if passwords := input_box("Старый пароль менеджера", "Новый пароль менеджера", password_type=True):
            self._app.change_user_app_password(*passwords)

    @response_decorator
    def change_admin_db_password(self):
        if passwords := input_box("Пароль", "Новый пароль администратора для базы", password_type=True):
            self._app.change_admin_db_password(*passwords)

    @response_decorator
    def change_user_db_password(self):
        if passwords := input_box("Пароль менеджера", "Новый пароль менеджера для базы", password_type=True):
            self._app.change_user_db_password(*passwords)

    @response_decorator
    def archive_db(self):
        self._app.archive_db()
