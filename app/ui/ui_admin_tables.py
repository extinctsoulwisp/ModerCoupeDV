# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_tablesrgeIqa.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_tables_tab(object):
    def setupUi(self, tables_tab):
        if not tables_tab.objectName():
            tables_tab.setObjectName(u"tables_tab")
        tables_tab.resize(866, 657)
        tables_tab.setStyleSheet(u"#top_widget {\n"
"background-color: rgb(54, 71, 79);\n"
"}\n"
"#header {\n"
"background-color: rgb(200, 200, 200);\n"
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
"#table > .QHeaderView::section {\n"
"    background-color: rgb(239, 243, 246);\n"
"	color: rgb(86, 96, 113);\n"
"border: 0;\n"
"border-bottom: 1px solid rgb(203, 206, 208);\n"
"}\n"
"#table > .QTableCornerButton::section{ \n"
"    background-color: transparent;\n"
"\n"
"}\n"
"#table::item:selected {\n"
"	background-color: rgb(184, 236, 230);\n"
"color: black;\n"
"}\n"
".QRadioButton, .QPushButton, .QChe"
                        "ckBox {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	padding: 10%;\n"
"	border: null;\n"
"}\n"
"\n"
".QComboBox {\n"
"	background-color: #36474f;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	padding: 10%;\n"
"	border: null;\n"
"}\n"
"\n"
".QRadioButton:hover, .QPushButton:hover, .QCheckBox:hover{\n"
"background-color: rgb(69, 75, 84);\n"
"}\n"
"\n"
".QRadioButton:checked{\n"
"background-color: rgb(38, 165, 154);\n"
"}\n"
"\n"
".QRadioButton::indicator, .QCheckBox::indicator{\n"
"width: 0;\n"
"}\n"
"\n"
".QLabel {\n"
"	color: rgb(136, 139, 145);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	padding: 10%;\n"
"}\n"
"\n"
".QSpinBox, .QDateEdit, .QLineEdit, .QTextEdit {\n"
"background-color: rgb(54, 71, 79);\n"
"border: null;\n"
"padding: 5%;\n"
"border-color: rgb(200, 200, 200);\n"
"color: rgb(200, 200, 200);\n"
"}\n"
"    \n"
"    QScrollBar:vertical {\n"
"        background-color: rgb(39, 50, 56);\n"
"        width: 10px;\n"
""
                        "        margin: 0px;\n"
"    }\n"
"    \n"
"    QScrollBar::handle:vertical {\n"
"        background-color: #c0c0c0;\n"
"        min-height: 20px;\n"
"    }\n"
"    \n"
"    QScrollBar::add-line:vertical,\n"
"    QScrollBar::sub-line:vertical {\n"
"        background: none;\n"
"    }\n"
"    \n"
"    QScrollBar::add-page:vertical,\n"
"    QScrollBar::sub-page:vertical {\n"
"        background: none;\n"
"    }\n"
"\n"
"#r_custom_overlap:checked +#i_overlap_count {\n"
"background-color: rgb(38, 165, 154);\n"
"}\n"
"\n"
"\n"
"#r_custom_overlap:hover +#i_overlap_count {\n"
"background-color: rgb(38, 165, 154);\n"
"}\n"
"\n"
".QGroupBox {\n"
"border: null;\n"
"}\n"
"\n"
".QComboBox::drop-down {\n"
"width: 0;\n"
"}\n"
"\n"
"QMenu::itemQComboBox QAbstractItemView{\n"
"color: white;\n"
"            padding: 5px 20px;\n"
"            background-color: rgb(39, 50, 56);\n"
"            }\n"
"QComboBox QAbstractItemView:selected {\n"
"             background-color: rgb(69, 75, 84);\n"
"            }")
        self.gridLayout = QGridLayout(tables_tab)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.rigth_widget = QWidget(tables_tab)
        self.rigth_widget.setObjectName(u"rigth_widget")
        self.verticalLayout = QVBoxLayout(self.rigth_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
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

        self.btn_material = QPushButton(self.rigth_widget)
        self.btn_material.setObjectName(u"btn_material")

        self.verticalLayout.addWidget(self.btn_material)

        self.btn_color = QPushButton(self.rigth_widget)
        self.btn_color.setObjectName(u"btn_color")

        self.verticalLayout.addWidget(self.btn_color)

        self.btn_customer = QPushButton(self.rigth_widget)
        self.btn_customer.setObjectName(u"btn_customer")

        self.verticalLayout.addWidget(self.btn_customer)

        self.label_2 = QLabel(self.rigth_widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.groupBox = QGroupBox(self.rigth_widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.r_actual = QRadioButton(self.groupBox)
        self.r_actual.setObjectName(u"r_actual")
        self.r_actual.setChecked(True)

        self.verticalLayout_2.addWidget(self.r_actual)

        self.r_deleted = QRadioButton(self.groupBox)
        self.r_deleted.setObjectName(u"r_deleted")

        self.verticalLayout_2.addWidget(self.r_deleted)

        self.r_all = QRadioButton(self.groupBox)
        self.r_all.setObjectName(u"r_all")

        self.verticalLayout_2.addWidget(self.r_all)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.rigth_widget, 0, 1, 3, 1)

        self.top_widget = QWidget(tables_tab)
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

        self.table = QTableWidget(tables_tab)
        self.table.setObjectName(u"table")
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.table, 1, 0, 1, 1)


        self.retranslateUi(tables_tab)

        QMetaObject.connectSlotsByName(tables_tab)
    # setupUi

    def retranslateUi(self, tables_tab):
        tables_tab.setWindowTitle(QCoreApplication.translate("tables_tab", u"Form", None))
        self.label.setText(QCoreApplication.translate("tables_tab", u"\u0422\u0410\u0411\u041b\u0418\u0426\u042b", None))
        self.btn_profile.setText(QCoreApplication.translate("tables_tab", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.btn_rigel.setText(QCoreApplication.translate("tables_tab", u"\u0420\u0438\u0433\u0435\u043b\u044c", None))
        self.btn_user.setText(QCoreApplication.translate("tables_tab", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.btn_material.setText(QCoreApplication.translate("tables_tab", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b", None))
        self.btn_color.setText(QCoreApplication.translate("tables_tab", u"\u0426\u0432\u0435\u0442", None))
        self.btn_customer.setText(QCoreApplication.translate("tables_tab", u"\u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.label_2.setText(QCoreApplication.translate("tables_tab", u"\u041f\u041e\u041a\u0410\u0417\u0410\u0422\u042c", None))
        self.groupBox.setTitle("")
        self.r_actual.setText(QCoreApplication.translate("tables_tab", u"\u0410\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0435", None))
        self.r_deleted.setText(QCoreApplication.translate("tables_tab", u"\u0423\u0434\u0430\u043b\u0435\u043d\u043d\u044b\u0435", None))
        self.r_all.setText(QCoreApplication.translate("tables_tab", u"\u0412\u0441\u0435", None))
        self.btn_save.setText(QCoreApplication.translate("tables_tab", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_add.setText(QCoreApplication.translate("tables_tab", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

