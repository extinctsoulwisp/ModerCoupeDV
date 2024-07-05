# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginVvVEqR.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.setWindowModality(Qt.WindowModal)
        LoginDialog.resize(250, 420)
        LoginDialog.setMinimumSize(QSize(250, 420))
        LoginDialog.setMaximumSize(QSize(250, 420))
        LoginDialog.setStyleSheet(u"#background {\n"
"background-color: rgb(39, 50, 56);\n"
"}\n"
"\n"
"#logo {\n"
"background: transparent;\n"
"border: null;\n"
"}\n"
"\n"
".QLabel {\n"
"	color: white;\n"
"}\n"
"\n"
".QLineEdit {\n"
"	border: null;\n"
"	color: white;\n"
"	font: 11pt \"Segoe UI\";\n"
"background-color: rgb(54, 71, 79);\n"
"padding: 5;\n"
"}\n"
"\n"
"#btn_login {\n"
"border: null;\n"
"	color: white;\n"
"	font: 11pt \"Segoe UI\";\n"
"background-color: rgb(38, 165, 154);\n"
"padding: 5;\n"
"}\n"
"#btn_login:hover, #ch_login_as_user:hover {\n"
"background-color: rgb(69, 75, 84);\n"
"}\n"
"\n"
"#error_text {\n"
"background: transparent;\n"
"border: null;\n"
"color: rgb(54, 71, 79);\n"
"}\n"
"\n"
".QCheckBox{\n"
"border: null;\n"
"background: transparent;\n"
"color: white;\n"
"padding: 3%;\n"
"text-align: center;\n"
"}\n"
".QCheckBox::indicator {\n"
"width: 0;\n"
"}")
        self.horizontalLayout = QHBoxLayout(LoginDialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.background = QWidget(LoginDialog)
        self.background.setObjectName(u"background")
        self.verticalLayout = QVBoxLayout(self.background)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.logo = QPushButton(self.background)
        self.logo.setObjectName(u"logo")
        icon = QIcon()
        icon.addFile(u"icons/logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logo.setIcon(icon)
        self.logo.setIconSize(QSize(64, 64))

        self.verticalLayout.addWidget(self.logo)

        self.company_name = QLabel(self.background)
        self.company_name.setObjectName(u"company_name")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.company_name.sizePolicy().hasHeightForWidth())
        self.company_name.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.company_name.setFont(font)
        self.company_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.company_name)

        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.inp_user_password = QLineEdit(self.background)
        self.inp_user_password.setObjectName(u"inp_user_password")
        self.inp_user_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.inp_user_password)

        self.inp_password = QLineEdit(self.background)
        self.inp_password.setObjectName(u"inp_password")
        self.inp_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.inp_password)

        self.btn_login = QPushButton(self.background)
        self.btn_login.setObjectName(u"btn_login")

        self.verticalLayout.addWidget(self.btn_login)

        self.error_text = QTextEdit(self.background)
        self.error_text.setObjectName(u"error_text")
        self.error_text.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.error_text.sizePolicy().hasHeightForWidth())
        self.error_text.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.error_text)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.ch_login_as_user = QCheckBox(self.background)
        self.ch_login_as_user.setObjectName(u"ch_login_as_user")
        self.ch_login_as_user.setChecked(True)

        self.horizontalLayout_2.addWidget(self.ch_login_as_user)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.background)


        self.retranslateUi(LoginDialog)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"\u0412\u0445\u043e\u0434", None))
        self.logo.setText("")
        self.company_name.setText(QCoreApplication.translate("LoginDialog", u"\u041c\u041e\u0414\u0415\u0420\u041d \u041a\u0423\u041f\u0415", None))
        self.inp_user_password.setText("")
        self.inp_user_password.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440", None))
        self.inp_password.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_login.setText(QCoreApplication.translate("LoginDialog", u"\u0412\u041e\u0419\u0422\u0418", None))
        self.error_text.setHtml(QCoreApplication.translate("LoginDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.ch_login_as_user.setText(QCoreApplication.translate("LoginDialog", u"\u0412\u043e\u0439\u0442\u0438 \u043a\u0430\u043a \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
    # retranslateUi

