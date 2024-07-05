# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rigel_linePHyTuY.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QHBoxLayout,
    QLineEdit, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1166, 60)
        Form.setStyleSheet(u".QSpinBox, .QDateEdit, .QLineEdit, .QTextEdit, .QRadioButton, .QPushButton, .QCheckBox, \n"
".QDoubleSpinBox  {\n"
"background-color: transparent;\n"
"border: 1px solid rgb(200, 200, 200);\n"
"padding: 20%;\n"
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
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.i_name.sizePolicy().hasHeightForWidth())
        self.i_name.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.i_name)

        self.i_center = QDoubleSpinBox(Form)
        self.i_center.setObjectName(u"i_center")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.i_center.sizePolicy().hasHeightForWidth())
        self.i_center.setSizePolicy(sizePolicy1)
        self.i_center.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.i_center.setDecimals(1)

        self.horizontalLayout_2.addWidget(self.i_center)

        self.i_depth = QDoubleSpinBox(Form)
        self.i_depth.setObjectName(u"i_depth")
        sizePolicy1.setHeightForWidth(self.i_depth.sizePolicy().hasHeightForWidth())
        self.i_depth.setSizePolicy(sizePolicy1)
        self.i_depth.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.i_depth.setDecimals(1)

        self.horizontalLayout_2.addWidget(self.i_depth)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

