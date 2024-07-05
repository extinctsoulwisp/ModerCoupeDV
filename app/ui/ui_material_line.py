# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'material_lineooDJuY.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLineEdit,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1166, 60)
        Form.setStyleSheet(u".QSpinBox, .QDateEdit, .QLineEdit, .QTextEdit, .QRadioButton, .QPushButton, .QCheckBox, \n"
".QDoubleSpinBox  {\n"
"background-color: transparent;\n"
"padding: 20%;\n"
"border: 0;\n"
"border-bottom: 1px solid rgb(200, 200, 200);\n"
"color: black;\n"
"}\n"
"\n"
".QCheckBox::indicator{\n"
"width: 0;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.i_name = QLineEdit(Form)
        self.i_name.setObjectName(u"i_name")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.i_name.sizePolicy().hasHeightForWidth())
        self.i_name.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.i_name)

        self.ch_need_sealant = QCheckBox(Form)
        self.ch_need_sealant.setObjectName(u"ch_need_sealant")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ch_need_sealant.sizePolicy().hasHeightForWidth())
        self.ch_need_sealant.setSizePolicy(sizePolicy1)
        self.ch_need_sealant.setChecked(True)

        self.horizontalLayout_2.addWidget(self.ch_need_sealant)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ch_need_sealant.setText(QCoreApplication.translate("Form", u"\u0411\u0435\u0437 \u0443\u043f\u043b\u043e\u0442\u043d\u0438\u0442\u0435\u043b\u044f", None))
    # retranslateUi

