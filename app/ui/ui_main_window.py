# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowlNvZWn.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(752, 355)
        icon = QIcon()
        icon.addFile(u"icons/logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#left_widget {\n"
"	background-color: #20272a;\n"
"}\n"
"\n"
"#central_widget {\n"
"	background-color: rgb(241, 244, 249);\n"
"}\n"
"\n"
".QPushButton {\n"
"background: transparent;\n"
"border: null;\n"
"color: white;\n"
"}\n"
"\n"
".QLabel {\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	color: white;\n"
"}\n"
"\n"
"#tabs {\n"
"	background-color: transparent;\n"
"	border: null;\n"
"	outline: none;\n"
"}\n"
"\n"
"#tabs::item {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 9pt \"Segoe UI\";\n"
"	padding: 10%;\n"
"	border: null;\n"
"}\n"
"\n"
"#tabs::item:hover{\n"
"background-color: rgb(69, 75, 84);\n"
"}\n"
"\n"
"#tabs::item:selected{\n"
"background-color: rgb(38, 165, 154);\n"
"}\n"
"\n"
"#company_name {\n"
"padding-left: 10;\n"
"padding-right: 10;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_widget = QWidget(self.centralwidget)
        self.left_widget.setObjectName(u"left_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_widget.sizePolicy().hasHeightForWidth())
        self.left_widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.left_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.logo = QPushButton(self.left_widget)
        self.logo.setObjectName(u"logo")
        self.logo.setIcon(icon)
        self.logo.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.logo)

        self.company_name = QLabel(self.left_widget)
        self.company_name.setObjectName(u"company_name")
        self.company_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.company_name)

        self.tabs = QListWidget(self.left_widget)
        self.tabs.setObjectName(u"tabs")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy1)
        self.tabs.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tabs.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabs.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.tabs)

        self.user = QPushButton(self.left_widget)
        self.user.setObjectName(u"user")
        icon1 = QIcon()
        icon1.addFile(u"icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.user.setIcon(icon1)

        self.verticalLayout.addWidget(self.user)


        self.horizontalLayout.addWidget(self.left_widget)

        self.central_widget = QWidget(self.centralwidget)
        self.central_widget.setObjectName(u"central_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy2)
        self.horizontalLayout_3 = QHBoxLayout(self.central_widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.central_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u0440\u043d\u041a\u0443\u043f\u0435 - \u0411\u0435\u0442\u0430-\u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.logo.setText("")
        self.company_name.setText(QCoreApplication.translate("MainWindow", u"\u041c\u041e\u0414\u0415\u0420\u041d \u041a\u0423\u041f\u0415", None))
        self.user.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
    # retranslateUi

