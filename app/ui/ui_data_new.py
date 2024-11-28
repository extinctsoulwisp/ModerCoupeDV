# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_newhuembm.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_tables_tab(object):
    def setupUi(self, tables_tab):
        if not tables_tab.objectName():
            tables_tab.setObjectName(u"tables_tab")
        tables_tab.resize(1099, 657)
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
".QTableWidget, .QListWidget {\n"
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
"	font: 700 9pt \"Segoe UI\";\n"
"	padding: 10%;\n"
"}\n"
"\n"
".QTableWidget > .QHeaderView::section {\n"
"    background-color: rgb(239, 243, 246);\n"
"	color: rgb(86, 96, 113);\n"
"border: 0;\n"
"border-bottom: 1px solid rgb(203, 206, 208);\n"
"}\n"
".QTableWidget > .QTableCornerButton::section{ \n"
"    background-color: transparent;\n"
"\n"
"}\n"
".QTableWidget {\n"
"outline: 0;\n"
"}\n"
".QTableWidget::item:selected {\n"
"	background-color: rgb(184, 236, 230);\n"
"color:"
                        " black;\n"
"}\n"
"\n"
".QListWidget {\n"
"outline: 0;\n"
"}\n"
".QListWidget::item {\n"
"padding: 5%;\n"
"border-bottom: 1px solid rgb(203, 206, 208);\n"
"}\n"
"\n"
".QListWidget::item:selected {\n"
"	background-color: rgb(184, 236, 230);\n"
"	color: black;\n"
"}\n"
"\n"
"\n"
"\n"
".QRadioButton, .QPushButton {\n"
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
".QRadioButton:hover, .QPushButton:hover{\n"
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
".QSpinBox, .QDateEdit, "
                        ".QLineEdit, .QTextEdit {\n"
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
"QMenu::i"
                        "temQComboBox QAbstractItemView{\n"
"color: white;\n"
"            padding: 5px 20px;\n"
"            background-color: rgb(39, 50, 56);\n"
"            }\n"
"QComboBox QAbstractItemView:selected {\n"
"             background-color: rgb(69, 75, 84);\n"
"            }\n"
"\n"
"\n"
"#bg {\n"
"	background-color: rgb(241, 244, 249);\n"
"\n"
"}\n"
".QTabWidget > .QTabBar::tab {\n"
"    height: 0;\n"
"}\n"
"\n"
".QTabWidget {\n"
"    outline: 0;\n"
"}\n"
"\n"
"#profile_tab, #rigel_tab {\n"
"background-color: rgb(241, 244, 249);\n"
"}\n"
"\n"
"#ch_is_open, #tabWidget .QPushButton {\n"
"	color: black;\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")
        self.gridLayout = QGridLayout(tables_tab)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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

        self.btn_load_from_1c = QPushButton(self.top_widget)
        self.btn_load_from_1c.setObjectName(u"btn_load_from_1c")
        sizePolicy1.setHeightForWidth(self.btn_load_from_1c.sizePolicy().hasHeightForWidth())
        self.btn_load_from_1c.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u"icons/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_load_from_1c.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_load_from_1c)


        self.gridLayout.addWidget(self.top_widget, 0, 0, 1, 1)

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

        self.label_14 = QLabel(self.rigth_widget)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

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

        self.tabWidget = QTabWidget(tables_tab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setDocumentMode(True)
        self.profile_tab = QWidget()
        self.profile_tab.setObjectName(u"profile_tab")
        self.gridLayout_2 = QGridLayout(self.profile_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(30)
        self.gridLayout_2.setContentsMargins(30, 30, 30, 30)
        self.label_3 = QLabel(self.profile_tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.tbl_profile_params = QTableWidget(self.profile_tab)
        if (self.tbl_profile_params.columnCount() < 2):
            self.tbl_profile_params.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_profile_params.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_profile_params.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tbl_profile_params.rowCount() < 11):
            self.tbl_profile_params.setRowCount(11)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_profile_params.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_profile_params.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_profile_params.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_profile_params.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_profile_params.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_profile_params.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_profile_params.setVerticalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbl_profile_params.setVerticalHeaderItem(8, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbl_profile_params.setVerticalHeaderItem(9, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbl_profile_params.setVerticalHeaderItem(10, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbl_profile_params.setItem(0, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbl_profile_params.setItem(1, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbl_profile_params.setItem(2, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tbl_profile_params.setItem(3, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tbl_profile_params.setItem(4, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tbl_profile_params.setItem(5, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tbl_profile_params.setItem(6, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tbl_profile_params.setItem(7, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tbl_profile_params.setItem(8, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tbl_profile_params.setItem(9, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tbl_profile_params.setItem(10, 0, __qtablewidgetitem22)
        self.tbl_profile_params.setObjectName(u"tbl_profile_params")
        self.tbl_profile_params.setSelectionMode(QAbstractItemView.NoSelection)
        self.tbl_profile_params.setShowGrid(True)
        self.tbl_profile_params.horizontalHeader().setVisible(False)
        self.tbl_profile_params.horizontalHeader().setStretchLastSection(True)
        self.tbl_profile_params.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.tbl_profile_params, 1, 1, 1, 1)

        self.lst_profile_names = QListWidget(self.profile_tab)
        self.lst_profile_names.setObjectName(u"lst_profile_names")
        self.lst_profile_names.setContextMenuPolicy(Qt.CustomContextMenu)

        self.gridLayout_2.addWidget(self.lst_profile_names, 1, 0, 1, 1)

        self.label_6 = QLabel(self.profile_tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)

        self.tbl_profile_1c = QTableWidget(self.profile_tab)
        if (self.tbl_profile_1c.columnCount() < 2):
            self.tbl_profile_1c.setColumnCount(2)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tbl_profile_1c.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tbl_profile_1c.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        if (self.tbl_profile_1c.rowCount() < 13):
            self.tbl_profile_1c.setRowCount(13)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tbl_profile_1c.setVerticalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tbl_profile_1c.setVerticalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tbl_profile_1c.setVerticalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tbl_profile_1c.setVerticalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tbl_profile_1c.setVerticalHeaderItem(4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tbl_profile_1c.setVerticalHeaderItem(5, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tbl_profile_1c.setVerticalHeaderItem(6, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tbl_profile_1c.setVerticalHeaderItem(7, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tbl_profile_1c.setVerticalHeaderItem(8, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tbl_profile_1c.setVerticalHeaderItem(9, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tbl_profile_1c.setVerticalHeaderItem(10, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tbl_profile_1c.setVerticalHeaderItem(11, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tbl_profile_1c.setItem(0, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tbl_profile_1c.setItem(1, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tbl_profile_1c.setItem(2, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tbl_profile_1c.setItem(3, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tbl_profile_1c.setItem(4, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tbl_profile_1c.setItem(5, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tbl_profile_1c.setItem(6, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tbl_profile_1c.setItem(7, 0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tbl_profile_1c.setItem(8, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tbl_profile_1c.setItem(9, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tbl_profile_1c.setItem(10, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tbl_profile_1c.setItem(11, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tbl_profile_1c.setItem(12, 0, __qtablewidgetitem49)
        self.tbl_profile_1c.setObjectName(u"tbl_profile_1c")
        self.tbl_profile_1c.setSelectionMode(QAbstractItemView.NoSelection)
        self.tbl_profile_1c.setShowGrid(True)
        self.tbl_profile_1c.horizontalHeader().setVisible(False)
        self.tbl_profile_1c.horizontalHeader().setStretchLastSection(True)
        self.tbl_profile_1c.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.tbl_profile_1c, 1, 3, 1, 1)

        self.label_4 = QLabel(self.profile_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_5 = QLabel(self.profile_tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)

        self.lst_profile_colors = QListWidget(self.profile_tab)
        self.lst_profile_colors.setObjectName(u"lst_profile_colors")

        self.gridLayout_2.addWidget(self.lst_profile_colors, 1, 2, 1, 1)

        self.tabWidget.addTab(self.profile_tab, "")
        self.rigel_tab = QWidget()
        self.rigel_tab.setObjectName(u"rigel_tab")
        self.rigel_tab.setContextMenuPolicy(Qt.CustomContextMenu)
        self.gridLayout_3 = QGridLayout(self.rigel_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(30)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(30, 30, 30, 30)
        self.label_10 = QLabel(self.rigel_tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_7 = QLabel(self.rigel_tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)

        self.label_9 = QLabel(self.rigel_tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_9, 0, 2, 1, 1)

        self.label_8 = QLabel(self.rigel_tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_8, 0, 3, 1, 1)

        self.lst_rigel_names = QListWidget(self.rigel_tab)
        QListWidgetItem(self.lst_rigel_names)
        QListWidgetItem(self.lst_rigel_names)
        QListWidgetItem(self.lst_rigel_names)
        QListWidgetItem(self.lst_rigel_names)
        self.lst_rigel_names.setObjectName(u"lst_rigel_names")
        self.lst_rigel_names.setContextMenuPolicy(Qt.CustomContextMenu)

        self.gridLayout_3.addWidget(self.lst_rigel_names, 1, 0, 1, 1)

        self.tbl_rigel_params = QTableWidget(self.rigel_tab)
        if (self.tbl_rigel_params.columnCount() < 2):
            self.tbl_rigel_params.setColumnCount(2)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tbl_rigel_params.setHorizontalHeaderItem(0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tbl_rigel_params.setHorizontalHeaderItem(1, __qtablewidgetitem51)
        if (self.tbl_rigel_params.rowCount() < 2):
            self.tbl_rigel_params.setRowCount(2)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tbl_rigel_params.setVerticalHeaderItem(0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tbl_rigel_params.setItem(0, 0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tbl_rigel_params.setItem(1, 0, __qtablewidgetitem54)
        self.tbl_rigel_params.setObjectName(u"tbl_rigel_params")
        self.tbl_rigel_params.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_rigel_params.setShowGrid(True)
        self.tbl_rigel_params.horizontalHeader().setVisible(False)
        self.tbl_rigel_params.horizontalHeader().setStretchLastSection(True)
        self.tbl_rigel_params.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.tbl_rigel_params, 1, 1, 1, 1)

        self.lst_rigel_colors = QListWidget(self.rigel_tab)
        __qlistwidgetitem = QListWidgetItem(self.lst_rigel_colors)
        __qlistwidgetitem.setCheckState(Qt.Checked);
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        QListWidgetItem(self.lst_rigel_colors)
        self.lst_rigel_colors.setObjectName(u"lst_rigel_colors")

        self.gridLayout_3.addWidget(self.lst_rigel_colors, 1, 2, 1, 1)

        self.tbl_rigel_1c = QTableWidget(self.rigel_tab)
        if (self.tbl_rigel_1c.columnCount() < 2):
            self.tbl_rigel_1c.setColumnCount(2)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tbl_rigel_1c.setHorizontalHeaderItem(0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tbl_rigel_1c.setHorizontalHeaderItem(1, __qtablewidgetitem56)
        if (self.tbl_rigel_1c.rowCount() < 1):
            self.tbl_rigel_1c.setRowCount(1)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tbl_rigel_1c.setItem(0, 0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tbl_rigel_1c.setItem(0, 1, __qtablewidgetitem58)
        self.tbl_rigel_1c.setObjectName(u"tbl_rigel_1c")
        self.tbl_rigel_1c.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_rigel_1c.setShowGrid(True)
        self.tbl_rigel_1c.horizontalHeader().setVisible(False)
        self.tbl_rigel_1c.horizontalHeader().setStretchLastSection(True)
        self.tbl_rigel_1c.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.tbl_rigel_1c, 1, 3, 1, 1)

        self.tabWidget.addTab(self.rigel_tab, "")
        self.table_tab = QWidget()
        self.table_tab.setObjectName(u"table_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.table_tab)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.table = QTableWidget(self.table_tab)
        self.table.setObjectName(u"table")
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)

        self.horizontalLayout_4.addWidget(self.table)

        self.tabWidget.addTab(self.table_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)


        self.retranslateUi(tables_tab)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(tables_tab)
    # setupUi

    def retranslateUi(self, tables_tab):
        tables_tab.setWindowTitle(QCoreApplication.translate("tables_tab", u"Form", None))
        self.btn_save.setText(QCoreApplication.translate("tables_tab", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_load_from_1c.setText(QCoreApplication.translate("tables_tab", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437 1\u0421", None))
        self.label.setText(QCoreApplication.translate("tables_tab", u"\u0421\u0418\u0421\u0422\u0415\u041c\u042b", None))
        self.btn_profile.setText(QCoreApplication.translate("tables_tab", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.btn_rigel.setText(QCoreApplication.translate("tables_tab", u"\u0420\u0438\u0433\u0435\u043b\u044c", None))
        self.label_14.setText(QCoreApplication.translate("tables_tab", u"\u0422\u0410\u0411\u041b\u0418\u0426\u042b", None))
        self.btn_user.setText(QCoreApplication.translate("tables_tab", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.btn_material.setText(QCoreApplication.translate("tables_tab", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b", None))
        self.btn_color.setText(QCoreApplication.translate("tables_tab", u"\u0426\u0432\u0435\u0442", None))
        self.btn_customer.setText(QCoreApplication.translate("tables_tab", u"\u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.label_2.setText(QCoreApplication.translate("tables_tab", u"\u041f\u041e\u041a\u0410\u0417\u0410\u0422\u042c", None))
        self.groupBox.setTitle("")
        self.r_actual.setText(QCoreApplication.translate("tables_tab", u"\u0410\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0435", None))
        self.r_deleted.setText(QCoreApplication.translate("tables_tab", u"\u0423\u0434\u0430\u043b\u0435\u043d\u043d\u044b\u0435", None))
        self.r_all.setText(QCoreApplication.translate("tables_tab", u"\u0412\u0441\u0435", None))
        self.label_3.setText(QCoreApplication.translate("tables_tab", u"\u041f\u0420\u041e\u0424\u0418\u041b\u042c", None))
        ___qtablewidgetitem = self.tbl_profile_params.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem1 = self.tbl_profile_params.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem2 = self.tbl_profile_params.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem3 = self.tbl_profile_params.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem4 = self.tbl_profile_params.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem5 = self.tbl_profile_params.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem6 = self.tbl_profile_params.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem7 = self.tbl_profile_params.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem8 = self.tbl_profile_params.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem9 = self.tbl_profile_params.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem10 = self.tbl_profile_params.verticalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem11 = self.tbl_profile_params.verticalHeaderItem(10)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));

        __sortingEnabled = self.tbl_profile_params.isSortingEnabled()
        self.tbl_profile_params.setSortingEnabled(False)
        ___qtablewidgetitem12 = self.tbl_profile_params.item(0, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("tables_tab", u"\u041f\u0435\u0440\u0435\u0445\u043b\u0435\u0441\u0442", None));
        ___qtablewidgetitem13 = self.tbl_profile_params.item(1, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("tables_tab", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u044f\u044e\u0449\u0430\u044f", None));
        ___qtablewidgetitem14 = self.tbl_profile_params.item(2, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("tables_tab", u"\u0423\u043f\u043b\u043e\u0442\u043d\u0438\u0442\u0435\u043b\u044c", None));
        ___qtablewidgetitem15 = self.tbl_profile_params.item(3, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("tables_tab", u"\u0428\u043b\u0435\u0433\u0435\u043b\u044c", None));
        ___qtablewidgetitem16 = self.tbl_profile_params.item(4, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("tables_tab", u"\u0422\u0438\u043f", None));
        ___qtablewidgetitem17 = self.tbl_profile_params.item(5, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("tables_tab", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u0412.", None));
        ___qtablewidgetitem18 = self.tbl_profile_params.item(6, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("tables_tab", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430 \u0412.", None));
        ___qtablewidgetitem19 = self.tbl_profile_params.item(7, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("tables_tab", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0413.\u0412.", None));
        ___qtablewidgetitem20 = self.tbl_profile_params.item(8, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("tables_tab", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0413.\u041d.", None));
        ___qtablewidgetitem21 = self.tbl_profile_params.item(9, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("tables_tab", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430 \u0413.\u0412.", None));
        ___qtablewidgetitem22 = self.tbl_profile_params.item(10, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("tables_tab", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430 \u0413.\u041d.", None));
        self.tbl_profile_params.setSortingEnabled(__sortingEnabled)

        self.label_6.setText(QCoreApplication.translate("tables_tab", u"\u0421\u0412\u042f\u0417\u042c \u0421 1\u0421", None))
        ___qtablewidgetitem23 = self.tbl_profile_1c.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem24 = self.tbl_profile_1c.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem25 = self.tbl_profile_1c.verticalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem26 = self.tbl_profile_1c.verticalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem27 = self.tbl_profile_1c.verticalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem28 = self.tbl_profile_1c.verticalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem29 = self.tbl_profile_1c.verticalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem30 = self.tbl_profile_1c.verticalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem31 = self.tbl_profile_1c.verticalHeaderItem(6)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem32 = self.tbl_profile_1c.verticalHeaderItem(7)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem33 = self.tbl_profile_1c.verticalHeaderItem(8)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem34 = self.tbl_profile_1c.verticalHeaderItem(9)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem35 = self.tbl_profile_1c.verticalHeaderItem(10)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem36 = self.tbl_profile_1c.verticalHeaderItem(11)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));

        __sortingEnabled1 = self.tbl_profile_1c.isSortingEnabled()
        self.tbl_profile_1c.setSortingEnabled(False)
        ___qtablewidgetitem37 = self.tbl_profile_1c.item(0, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("tables_tab", u"\u0412\u0435\u0440\u0445\u043d\u044f\u044f \u041d. 2\u041f", None));
        ___qtablewidgetitem38 = self.tbl_profile_1c.item(1, 0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("tables_tab", u"\u041d\u0438\u0436\u043d\u044f\u044f \u041d. 2\u041f", None));
        ___qtablewidgetitem39 = self.tbl_profile_1c.item(2, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("tables_tab", u"\u0412\u0435\u0440\u0445\u043d\u044f\u044f \u041d. 1\u041f", None));
        ___qtablewidgetitem40 = self.tbl_profile_1c.item(3, 0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("tables_tab", u"\u041d\u0438\u0436\u043d\u044f\u044f \u041d. 1\u041f", None));
        ___qtablewidgetitem41 = self.tbl_profile_1c.item(4, 0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("tables_tab", u"\u0425\u043e\u0434\u043e\u0432\u043e\u0439", None));
        ___qtablewidgetitem42 = self.tbl_profile_1c.item(5, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("tables_tab", u"\u041d\u0430\u043a\u043b\u0430\u0434\u043a\u0430", None));
        ___qtablewidgetitem43 = self.tbl_profile_1c.item(6, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("tables_tab", u"\u0417\u0430\u0433\u043b\u0443\u0448\u043a\u0430", None));
        ___qtablewidgetitem44 = self.tbl_profile_1c.item(7, 0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("tables_tab", u"\u0412\u0435\u0440\u0445\u043d\u0438\u0439 \u0413.", None));
        ___qtablewidgetitem45 = self.tbl_profile_1c.item(8, 0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("tables_tab", u"\u041d\u0438\u0436\u043d\u0438\u0439 \u0413.", None));
        ___qtablewidgetitem46 = self.tbl_profile_1c.item(9, 0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("tables_tab", u"\u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439", None));
        ___qtablewidgetitem47 = self.tbl_profile_1c.item(10, 0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("tables_tab", u"\u0423\u043f\u043b\u043e\u0442\u043d\u0438\u0442\u0435\u043b\u044c", None));
        ___qtablewidgetitem48 = self.tbl_profile_1c.item(11, 0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("tables_tab", u"\u0428\u043b\u0435\u0433\u0435\u043b\u044c", None));
        ___qtablewidgetitem49 = self.tbl_profile_1c.item(12, 0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("tables_tab", u"\u0420\u043e\u043b\u0438\u043a\u0438", None));
        self.tbl_profile_1c.setSortingEnabled(__sortingEnabled1)

        self.label_4.setText(QCoreApplication.translate("tables_tab", u"\u041f\u0410\u0420\u0410\u041c\u0415\u0422\u0420\u042b", None))
        self.label_5.setText(QCoreApplication.translate("tables_tab", u"\u0426\u0412\u0415\u0422", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profile_tab), QCoreApplication.translate("tables_tab", u"Tab 1", None))
        self.label_10.setText(QCoreApplication.translate("tables_tab", u"\u0420\u0418\u0413\u0415\u041b\u042c", None))
        self.label_7.setText(QCoreApplication.translate("tables_tab", u"\u041f\u0410\u0420\u0410\u041c\u0415\u0422\u0420\u042b", None))
        self.label_9.setText(QCoreApplication.translate("tables_tab", u"\u0426\u0412\u0415\u0422", None))
        self.label_8.setText(QCoreApplication.translate("tables_tab", u"\u0421\u0412\u042f\u0417\u042c \u0421 1\u0421", None))

        __sortingEnabled2 = self.lst_rigel_names.isSortingEnabled()
        self.lst_rigel_names.setSortingEnabled(False)
        ___qlistwidgetitem = self.lst_rigel_names.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem1 = self.lst_rigel_names.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem2 = self.lst_rigel_names.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem3 = self.lst_rigel_names.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        self.lst_rigel_names.setSortingEnabled(__sortingEnabled2)

        ___qtablewidgetitem50 = self.tbl_rigel_params.horizontalHeaderItem(0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem51 = self.tbl_rigel_params.horizontalHeaderItem(1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem52 = self.tbl_rigel_params.verticalHeaderItem(0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));

        __sortingEnabled3 = self.tbl_rigel_params.isSortingEnabled()
        self.tbl_rigel_params.setSortingEnabled(False)
        ___qtablewidgetitem53 = self.tbl_rigel_params.item(0, 0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("tables_tab", u"\u0421\u0435\u0440\u0435\u0434\u0438\u043d\u0430", None));
        ___qtablewidgetitem54 = self.tbl_rigel_params.item(1, 0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("tables_tab", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430", None));
        self.tbl_rigel_params.setSortingEnabled(__sortingEnabled3)


        __sortingEnabled4 = self.lst_rigel_colors.isSortingEnabled()
        self.lst_rigel_colors.setSortingEnabled(False)
        ___qlistwidgetitem4 = self.lst_rigel_colors.item(0)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem5 = self.lst_rigel_colors.item(1)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem6 = self.lst_rigel_colors.item(2)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem7 = self.lst_rigel_colors.item(3)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem8 = self.lst_rigel_colors.item(4)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem9 = self.lst_rigel_colors.item(5)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem10 = self.lst_rigel_colors.item(6)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem11 = self.lst_rigel_colors.item(7)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem12 = self.lst_rigel_colors.item(8)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem13 = self.lst_rigel_colors.item(9)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem14 = self.lst_rigel_colors.item(10)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem15 = self.lst_rigel_colors.item(11)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem16 = self.lst_rigel_colors.item(12)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem17 = self.lst_rigel_colors.item(13)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem18 = self.lst_rigel_colors.item(14)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem19 = self.lst_rigel_colors.item(15)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem20 = self.lst_rigel_colors.item(16)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem21 = self.lst_rigel_colors.item(17)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        self.lst_rigel_colors.setSortingEnabled(__sortingEnabled4)

        ___qtablewidgetitem55 = self.tbl_rigel_1c.horizontalHeaderItem(0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem56 = self.tbl_rigel_1c.horizontalHeaderItem(1)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("tables_tab", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));

        __sortingEnabled5 = self.tbl_rigel_1c.isSortingEnabled()
        self.tbl_rigel_1c.setSortingEnabled(False)
        ___qtablewidgetitem57 = self.tbl_rigel_1c.item(0, 0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("tables_tab", u"\u0420\u0438\u0433\u0435\u043b\u044c", None));
        self.tbl_rigel_1c.setSortingEnabled(__sortingEnabled5)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rigel_tab), QCoreApplication.translate("tables_tab", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.table_tab), QCoreApplication.translate("tables_tab", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
    # retranslateUi

