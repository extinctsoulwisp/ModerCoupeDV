# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_linesuLOJt.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDoubleSpinBox,
    QHBoxLayout, QLineEdit, QSizePolicy, QSpinBox,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1166, 68)
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
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.i_name.sizePolicy().hasHeightForWidth())
        self.i_name.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.i_name)

        self.is_open = QCheckBox(Form)
        self.is_open.setObjectName(u"is_open")
        sizePolicy.setHeightForWidth(self.is_open.sizePolicy().hasHeightForWidth())
        self.is_open.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.is_open)

        self.overlap = QSpinBox(Form)
        self.overlap.setObjectName(u"overlap")
        sizePolicy.setHeightForWidth(self.overlap.sizePolicy().hasHeightForWidth())
        self.overlap.setSizePolicy(sizePolicy)
        self.overlap.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_2.addWidget(self.overlap)

        self.guide = QDoubleSpinBox(Form)
        self.guide.setObjectName(u"guide")
        sizePolicy.setHeightForWidth(self.guide.sizePolicy().hasHeightForWidth())
        self.guide.setSizePolicy(sizePolicy)
        self.guide.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.guide.setDecimals(1)

        self.horizontalLayout_2.addWidget(self.guide)

        self.sealant = QDoubleSpinBox(Form)
        self.sealant.setObjectName(u"sealant")
        sizePolicy.setHeightForWidth(self.sealant.sizePolicy().hasHeightForWidth())
        self.sealant.setSizePolicy(sizePolicy)
        self.sealant.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sealant.setDecimals(1)

        self.horizontalLayout_2.addWidget(self.sealant)

        self.shlegel = QDoubleSpinBox(Form)
        self.shlegel.setObjectName(u"shlegel")
        sizePolicy.setHeightForWidth(self.shlegel.sizePolicy().hasHeightForWidth())
        self.shlegel.setSizePolicy(sizePolicy)
        self.shlegel.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.shlegel.setDecimals(1)

        self.horizontalLayout_2.addWidget(self.shlegel)

        self.v_width = QDoubleSpinBox(Form)
        self.v_width.setObjectName(u"v_width")
        sizePolicy.setHeightForWidth(self.v_width.sizePolicy().hasHeightForWidth())
        self.v_width.setSizePolicy(sizePolicy)
        self.v_width.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.v_width.setDecimals(1)

        self.horizontalLayout_2.addWidget(self.v_width)

        self.v_depth = QDoubleSpinBox(Form)
        self.v_depth.setObjectName(u"v_depth")
        sizePolicy.setHeightForWidth(self.v_depth.sizePolicy().hasHeightForWidth())
        self.v_depth.setSizePolicy(sizePolicy)
        self.v_depth.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.v_depth.setDecimals(1)

        self.horizontalLayout_2.addWidget(self.v_depth)

        self.h_top_width = QDoubleSpinBox(Form)
        self.h_top_width.setObjectName(u"h_top_width")
        sizePolicy.setHeightForWidth(self.h_top_width.sizePolicy().hasHeightForWidth())
        self.h_top_width.setSizePolicy(sizePolicy)
        self.h_top_width.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.h_top_width.setDecimals(1)

        self.horizontalLayout_2.addWidget(self.h_top_width)

        self.h_bot_width = QDoubleSpinBox(Form)
        self.h_bot_width.setObjectName(u"h_bot_width")
        sizePolicy.setHeightForWidth(self.h_bot_width.sizePolicy().hasHeightForWidth())
        self.h_bot_width.setSizePolicy(sizePolicy)
        self.h_bot_width.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.h_bot_width.setDecimals(1)

        self.horizontalLayout_2.addWidget(self.h_bot_width)

        self.h_top_depth = QDoubleSpinBox(Form)
        self.h_top_depth.setObjectName(u"h_top_depth")
        sizePolicy.setHeightForWidth(self.h_top_depth.sizePolicy().hasHeightForWidth())
        self.h_top_depth.setSizePolicy(sizePolicy)
        self.h_top_depth.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.h_top_depth.setDecimals(1)

        self.horizontalLayout_2.addWidget(self.h_top_depth)

        self.h_bot_depth = QDoubleSpinBox(Form)
        self.h_bot_depth.setObjectName(u"h_bot_depth")
        sizePolicy.setHeightForWidth(self.h_bot_depth.sizePolicy().hasHeightForWidth())
        self.h_bot_depth.setSizePolicy(sizePolicy)
        self.h_bot_depth.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.h_bot_depth.setDecimals(1)

        self.horizontalLayout_2.addWidget(self.h_bot_depth)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.is_open.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044b\u0439", None))
    # retranslateUi

