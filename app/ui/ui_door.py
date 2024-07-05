# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doorKfXWHe.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_door(object):
    def setupUi(self, door):
        if not door.objectName():
            door.setObjectName(u"door")
        door.resize(320, 524)
        door.setStyleSheet(u".QPushButton {\n"
"border: null;\n"
"	color: white;\n"
"	font: 11pt \"Segoe UI\";\n"
"background-color: rgb(39, 50, 56);\n"
"padding: 7;\n"
"border-radius: 10;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"background-color: rgb(69, 75, 84);\n"
"}\n"
"\n"
".QLabel {\n"
"color: black;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(door)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(17, 431, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.width = QLabel(door)
        self.width.setObjectName(u"width")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.width.sizePolicy().hasHeightForWidth())
        self.width.setSizePolicy(sizePolicy)
        self.width.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.width)

        self.widget = QWidget(door)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.widget)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(door)

        QMetaObject.connectSlotsByName(door)
    # setupUi

    def retranslateUi(self, door):
        door.setWindowTitle(QCoreApplication.translate("door", u"Form", None))
        self.width.setText(QCoreApplication.translate("door", u"TextLabel", None))
    # retranslateUi

