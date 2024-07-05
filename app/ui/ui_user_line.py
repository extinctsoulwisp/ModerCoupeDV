# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_lineJtUsDr.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QHBoxLayout, QLineEdit,
    QSizePolicy, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1208, 60)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u".QSpinBox, .QDateEdit, .QLineEdit, .QTextEdit, .QRadioButton, .QPushButton, .QCheckBox  {\n"
"background-color: transparent;\n"
"border: 1px solid rgb(200, 200, 200);\n"
"padding: 20%;\n"
"color: black;\n"
"}\n"
"\n"
".QCheckBox::indicator{\n"
"width: 0;\n"
"}\n"
"\n"
".QRadioButton::indicator, .QCheckBox::indicator{\n"
"width: 0;\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.i_name = QLineEdit(Form)
        self.i_name.setObjectName(u"i_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.i_name.sizePolicy().hasHeightForWidth())
        self.i_name.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.i_name)

        self.i_number = QSpinBox(Form)
        self.i_number.setObjectName(u"i_number")
        sizePolicy1.setHeightForWidth(self.i_number.sizePolicy().hasHeightForWidth())
        self.i_number.setSizePolicy(sizePolicy1)
        self.i_number.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.i_number.setMinimum(1)

        self.horizontalLayout.addWidget(self.i_number)

        self.i_password = QLineEdit(Form)
        self.i_password.setObjectName(u"i_password")
        sizePolicy1.setHeightForWidth(self.i_password.sizePolicy().hasHeightForWidth())
        self.i_password.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.i_password)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

