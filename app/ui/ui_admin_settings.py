# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_settingsrSzurY.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_settings_tab(object):
    def setupUi(self, settings_tab):
        if not settings_tab.objectName():
            settings_tab.setObjectName(u"settings_tab")
        settings_tab.resize(866, 673)
        settings_tab.setStyleSheet(u"#top_widget {\n"
"background-color: rgb(54, 71, 79);\n"
"}\n"
"#header {\n"
"background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
".QRadioButton, .QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border: null;\n"
"	padding: 10%;\n"
"}\n"
"\n"
"#table {\n"
"background-color: rgb(241, 244, 249);\n"
"}\n"
"\n"
".QRadioButton:hover, .QPushButton:hover{\n"
"background-color: rgb(69, 75, 84);\n"
"}\n"
"\n"
"#rigth_widget {\n"
"	background-color: rgb(39, 50, 56);\n"
"}\n"
"\n"
".QLabel {\n"
"	color: rgb(136, 139, 145);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	padding: 10%;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents {\n"
"background-color: rgb(241, 244, 249);\n"
"}")
        self.gridLayout = QGridLayout(settings_tab)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.top_widget = QWidget(settings_tab)
        self.top_widget.setObjectName(u"top_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_widget.sizePolicy().hasHeightForWidth())
        self.top_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.top_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_save = QPushButton(self.top_widget)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u"icons/disk.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_save)

        self.horizontalSpacer_3 = QSpacerItem(19, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.gridLayout.addWidget(self.top_widget, 0, 0, 1, 1)

        self.rigth_widget = QWidget(settings_tab)
        self.rigth_widget.setObjectName(u"rigth_widget")
        self.verticalLayout = QVBoxLayout(self.rigth_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.rigth_widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.btn_manager = QPushButton(self.rigth_widget)
        self.btn_manager.setObjectName(u"btn_manager")

        self.verticalLayout.addWidget(self.btn_manager)

        self.btn_postgres_manager = QPushButton(self.rigth_widget)
        self.btn_postgres_manager.setObjectName(u"btn_postgres_manager")

        self.verticalLayout.addWidget(self.btn_postgres_manager)

        self.btn_admin = QPushButton(self.rigth_widget)
        self.btn_admin.setObjectName(u"btn_admin")

        self.verticalLayout.addWidget(self.btn_admin)

        self.btn_postgres_admin = QPushButton(self.rigth_widget)
        self.btn_postgres_admin.setObjectName(u"btn_postgres_admin")

        self.verticalLayout.addWidget(self.btn_postgres_admin)

        self.label_3 = QLabel(self.rigth_widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.btn_archive = QPushButton(self.rigth_widget)
        self.btn_archive.setObjectName(u"btn_archive")

        self.verticalLayout.addWidget(self.btn_archive)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.rigth_widget, 0, 1, 2, 1)

        self.scrollArea = QScrollArea(settings_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(0, 0, 711, 635))
        self.formLayout = QFormLayout(self.settings)
        self.formLayout.setObjectName(u"formLayout")
        self.scrollArea.setWidget(self.settings)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.retranslateUi(settings_tab)

        QMetaObject.connectSlotsByName(settings_tab)
    # setupUi

    def retranslateUi(self, settings_tab):
        settings_tab.setWindowTitle(QCoreApplication.translate("settings_tab", u"Form", None))
        self.btn_save.setText(QCoreApplication.translate("settings_tab", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("settings_tab", u"\u0421\u041c\u0415\u041d\u0418\u0422\u042c \u041f\u0410\u0420\u041e\u041b\u042c", None))
        self.btn_manager.setText(QCoreApplication.translate("settings_tab", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 App", None))
        self.btn_postgres_manager.setText(QCoreApplication.translate("settings_tab", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 DB", None))
        self.btn_admin.setText(QCoreApplication.translate("settings_tab", u"\u0410\u0434\u043c\u0438\u043d App", None))
        self.btn_postgres_admin.setText(QCoreApplication.translate("settings_tab", u"\u0410\u0434\u043c\u0438\u043d DB", None))
        self.label_3.setText(QCoreApplication.translate("settings_tab", u"\u0411\u0410\u0417\u0410 \u0414\u0410\u041d\u041d\u042b\u0425", None))
        self.btn_archive.setText(QCoreApplication.translate("settings_tab", u"\u0410\u0440\u0445\u0438\u0432\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

