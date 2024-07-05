# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_lineuGYzSs.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1166, 60)
        Form.setStyleSheet(u".QLabel  {\n"
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
        self.create_date = QLabel(Form)
        self.create_date.setObjectName(u"create_date")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_date.sizePolicy().hasHeightForWidth())
        self.create_date.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.create_date)

        self.customer = QLabel(Form)
        self.customer.setObjectName(u"customer")
        sizePolicy.setHeightForWidth(self.customer.sizePolicy().hasHeightForWidth())
        self.customer.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.customer)

        self.description = QLabel(Form)
        self.description.setObjectName(u"description")
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.description)

        self.number = QLabel(Form)
        self.number.setObjectName(u"number")
        sizePolicy.setHeightForWidth(self.number.sizePolicy().hasHeightForWidth())
        self.number.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.number)

        self.profile = QLabel(Form)
        self.profile.setObjectName(u"profile")
        sizePolicy.setHeightForWidth(self.profile.sizePolicy().hasHeightForWidth())
        self.profile.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.profile)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.create_date.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.customer.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.description.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.number.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.profile.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

