# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminWairnz.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_admin(object):
    def setupUi(self, admin):
        if not admin.objectName():
            admin.setObjectName(u"admin")
        admin.resize(742, 567)
        admin.setStyleSheet(u"#top_widget {\n"
"background-color: rgb(54, 71, 79);\n"
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
        self.centralwidget = QWidget(admin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.top_widget = QWidget(self.centralwidget)
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

        self.btn_add = QPushButton(self.top_widget)
        self.btn_add.setObjectName(u"btn_add")
        icon1 = QIcon()
        icon1.addFile(u"icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_add)


        self.gridLayout.addWidget(self.top_widget, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 614, 529))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lines = QVBoxLayout()
        self.lines.setSpacing(6)
        self.lines.setObjectName(u"lines")
        self.lines.setContentsMargins(9, 9, 9, 9)

        self.verticalLayout_2.addLayout(self.lines)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.rigth_widget = QWidget(self.centralwidget)
        self.rigth_widget.setObjectName(u"rigth_widget")
        self.verticalLayout = QVBoxLayout(self.rigth_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.rigth_widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.btn_profile = QPushButton(self.rigth_widget)
        self.btn_profile.setObjectName(u"btn_profile")

        self.verticalLayout.addWidget(self.btn_profile)

        self.btn_rigel = QPushButton(self.rigth_widget)
        self.btn_rigel.setObjectName(u"btn_rigel")

        self.verticalLayout.addWidget(self.btn_rigel)

        self.btn_user = QPushButton(self.rigth_widget)
        self.btn_user.setObjectName(u"btn_user")

        self.verticalLayout.addWidget(self.btn_user)

        self.label_2 = QLabel(self.rigth_widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.btn_manager = QPushButton(self.rigth_widget)
        self.btn_manager.setObjectName(u"btn_manager")

        self.verticalLayout.addWidget(self.btn_manager)

        self.btn_admin = QPushButton(self.rigth_widget)
        self.btn_admin.setObjectName(u"btn_admin")

        self.verticalLayout.addWidget(self.btn_admin)

        self.btn_postgres_manager = QPushButton(self.rigth_widget)
        self.btn_postgres_manager.setObjectName(u"btn_postgres_manager")

        self.verticalLayout.addWidget(self.btn_postgres_manager)

        self.btn_postgres_admin = QPushButton(self.rigth_widget)
        self.btn_postgres_admin.setObjectName(u"btn_postgres_admin")

        self.verticalLayout.addWidget(self.btn_postgres_admin)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.rigth_widget, 0, 1, 3, 1)

        admin.setCentralWidget(self.centralwidget)

        self.retranslateUi(admin)

        QMetaObject.connectSlotsByName(admin)
    # setupUi

    def retranslateUi(self, admin):
        admin.setWindowTitle(QCoreApplication.translate("admin", u"MainWindow", None))
        self.btn_save.setText(QCoreApplication.translate("admin", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_add.setText(QCoreApplication.translate("admin", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("admin", u"\u0422\u0410\u0411\u041b\u0418\u0426\u042b", None))
        self.btn_profile.setText(QCoreApplication.translate("admin", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.btn_rigel.setText(QCoreApplication.translate("admin", u"\u0420\u0438\u0433\u0435\u043b\u044c", None))
        self.btn_user.setText(QCoreApplication.translate("admin", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.label_2.setText(QCoreApplication.translate("admin", u"\u041f\u0410\u0420\u041e\u041b\u0418", None))
        self.btn_manager.setText(QCoreApplication.translate("admin", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 App", None))
        self.btn_admin.setText(QCoreApplication.translate("admin", u"\u0410\u0434\u043c\u0438\u043d App", None))
        self.btn_postgres_manager.setText(QCoreApplication.translate("admin", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 DB", None))
        self.btn_postgres_admin.setText(QCoreApplication.translate("admin", u"\u0410\u0434\u043c\u0438\u043d DB", None))
    # retranslateUi

