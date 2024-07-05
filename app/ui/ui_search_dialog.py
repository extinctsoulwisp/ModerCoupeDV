# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_dialogPsabfF.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(342, 548)
        Dialog.setStyleSheet(u"#background {\n"
"background-color: rgb(39, 50, 56);\n"
"}\n"
"\n"
".QLineEdit {\n"
"	border: null;\n"
"	color: white;\n"
"	font: 11pt \"Segoe UI\";\n"
"background-color: transparent;\n"
"padding: 5;\n"
"}\n"
"\n"
".QPushButton {\n"
"border: null;\n"
"	color: white;\n"
"	font: 11pt \"Segoe UI\";\n"
"background-color: rgb(38, 165, 154);\n"
"padding: 5;\n"
"}\n"
".QCheckBox {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	padding: 10%;\n"
"	border: null;\n"
"}\n"
".QCheckBox::indicator{\n"
"width: 0;\n"
"}\n"
".QPushButton:hover, .QCheckBox:hover {\n"
"background-color: rgb(69, 75, 84);\n"
"}\n"
"\n"
"#search_list {\n"
"background-color: rgb(54, 71, 79);\n"
"font:700 10pt \"Segoe UI\";\n"
"border: null;\n"
"}\n"
"\n"
"#search_list:item {\n"
"	\n"
"	color: white;\n"
"	margin: 10%;\n"
"}\n"
"\n"
"#search_list:item:!enabled {\n"
"    color: gray;\n"
"}\n"
"\n"
".QPushButton::disabled{\n"
"background-color: rgb(69, 75, 84);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.background = QWidget(Dialog)
        self.background.setObjectName(u"background")
        self.verticalLayout_2 = QVBoxLayout(self.background)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.inp_search = QLineEdit(self.background)
        self.inp_search.setObjectName(u"inp_search")

        self.horizontalLayout.addWidget(self.inp_search)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.btn_add_to_db = QPushButton(self.background)
        self.btn_add_to_db.setObjectName(u"btn_add_to_db")
        self.btn_add_to_db.setEnabled(False)

        self.verticalLayout_2.addWidget(self.btn_add_to_db)

        self.search_list = QListWidget(self.background)
        self.search_list.setObjectName(u"search_list")

        self.verticalLayout_2.addWidget(self.search_list)


        self.verticalLayout.addWidget(self.background)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.inp_search.setInputMask("")
        self.inp_search.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.btn_add_to_db.setText(QCoreApplication.translate("Dialog", u"\u0412\u043d\u0435\u0441\u0442\u0438 \u0432 \u0431\u0430\u0437\u0443", None))
    # retranslateUi

