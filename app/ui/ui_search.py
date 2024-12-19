# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchduvNKl.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_SearchTab(object):
    def setupUi(self, SearchTab):
        if not SearchTab.objectName():
            SearchTab.setObjectName(u"SearchTab")
        SearchTab.resize(669, 486)
        SearchTab.setStyleSheet(u"#right_widget {\n"
"background-color: rgb(39, 50, 56);\n"
"}\n"
"\n"
"#table {\n"
"background-color: #f1f4f9;\n"
"}\n"
"\n"
"#top_widget {\n"
"background-color: rgb(54, 71, 79);\n"
"}\n"
"\n"
"#orders_list {\n"
"background-color: rgb(241, 244, 249);\n"
"border: null;\n"
"}\n"
"\n"
"#orders_list:item {\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	margin: 10%;\n"
"}\n"
"\n"
"#orders_list:item:!enabled {\n"
"    color: gray;\n"
"}\n"
"\n"
".QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	padding: 10;\n"
"	border: null;\n"
"}\n"
"\n"
".QGroupBox {\n"
"border: null;\n"
"}\n"
"\n"
"#btn_search {\n"
"border-radius: 10%;\n"
"}\n"
"\n"
".QLabel {\n"
"	color: rgb(136, 139, 145);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	padding: 10%;\n"
"}\n"
"\n"
"QRadioButton{\n"
"		padding: 5%;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 0;\n"
"}\n"
"\n"
"QRadioButton:checked{\n"
"background-color: rgb(38, 165, 154);\n"
""
                        "}\n"
"\n"
"QRadioButton:hover{\n"
"background-color: rgb(69, 75, 84);\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"	background-color: rgb(69, 75, 84);\n"
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
"#header {\n"
"background-color: rgb(200, 200, 200);\n"
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
"\n"
"")
        self.horizontalLayout = QHBoxLayout(SearchTab)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_widget = QWidget(SearchTab)
        self.top_widget.setObjectName(u"top_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.top_widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btn_update = QPushButton(self.top_widget)
        self.btn_update.setObjectName(u"btn_update")
        icon = QIcon()
        icon.addFile(u"icons/refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btn_update)

        self.btn_create = QPushButton(self.top_widget)
        self.btn_create.setObjectName(u"btn_create")
        icon1 = QIcon()
        icon1.addFile(u"icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_create.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.btn_create)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.top_widget)

        self.table = QTableWidget(SearchTab)
        if (self.table.columnCount() < 9):
            self.table.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table.setObjectName(u"table")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setShowGrid(True)
        self.table.setColumnCount(9)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.right_widget = QWidget(SearchTab)
        self.right_widget.setObjectName(u"right_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_widget.sizePolicy().hasHeightForWidth())
        self.right_widget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.right_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, -1, -1, -1)
        self.btn_search = QPushButton(self.right_widget)
        self.btn_search.setObjectName(u"btn_search")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u"icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_search)

        self.inp_search = QLineEdit(self.right_widget)
        self.inp_search.setObjectName(u"inp_search")
        self.inp_search.setStyleSheet(u"#inp_search {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.inp_search.setFrame(False)

        self.horizontalLayout_2.addWidget(self.inp_search)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label = QLabel(self.right_widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.groupBox = QGroupBox(self.right_widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.r_by_customer = QRadioButton(self.groupBox)
        self.r_by_customer.setObjectName(u"r_by_customer")
        self.r_by_customer.setChecked(True)

        self.verticalLayout_3.addWidget(self.r_by_customer)

        self.r_by_number = QRadioButton(self.groupBox)
        self.r_by_number.setObjectName(u"r_by_number")

        self.verticalLayout_3.addWidget(self.r_by_number)

        self.r_by_date = QRadioButton(self.groupBox)
        self.r_by_date.setObjectName(u"r_by_date")

        self.verticalLayout_3.addWidget(self.r_by_date)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.label_2 = QLabel(self.right_widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.groupBox_2 = QGroupBox(self.right_widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.r_desc = QRadioButton(self.groupBox_2)
        self.r_desc.setObjectName(u"r_desc")
        self.r_desc.setChecked(False)

        self.verticalLayout_4.addWidget(self.r_desc)

        self.r_asc = QRadioButton(self.groupBox_2)
        self.r_asc.setObjectName(u"r_asc")
        self.r_asc.setChecked(True)

        self.verticalLayout_4.addWidget(self.r_asc)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.label_3 = QLabel(self.right_widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.inp_limit = QSpinBox(self.right_widget)
        self.inp_limit.setObjectName(u"inp_limit")
        self.inp_limit.setStyleSheet(u"\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.inp_limit.setFrame(False)
        self.inp_limit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.inp_limit.setKeyboardTracking(False)
        self.inp_limit.setMinimum(100)
        self.inp_limit.setMaximum(5000)
        self.inp_limit.setSingleStep(10)

        self.horizontalLayout_3.addWidget(self.inp_limit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.right_widget)


        self.retranslateUi(SearchTab)

        QMetaObject.connectSlotsByName(SearchTab)
    # setupUi

    def retranslateUi(self, SearchTab):
        SearchTab.setWindowTitle(QCoreApplication.translate("SearchTab", u"Form", None))
        self.btn_update.setText(QCoreApplication.translate("SearchTab", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.btn_create.setText(QCoreApplication.translate("SearchTab", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SearchTab", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SearchTab", u"\u041a\u043b\u0438\u0435\u043d\u0442", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SearchTab", u"\u041d\u043e\u043c\u0435\u0440", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SearchTab", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SearchTab", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None));
        self.btn_search.setText("")
        self.inp_search.setInputMask("")
        self.inp_search.setPlaceholderText(QCoreApplication.translate("SearchTab", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label.setText(QCoreApplication.translate("SearchTab", u"\u041f\u041e\u0418\u0421\u041a \u041f\u041e", None))
        self.groupBox.setTitle("")
        self.r_by_customer.setText(QCoreApplication.translate("SearchTab", u"\u041a\u043b\u0438\u0435\u043d\u0442\u0443", None))
        self.r_by_number.setText(QCoreApplication.translate("SearchTab", u"\u041d\u043e\u043c\u0435\u0440\u0443", None))
        self.r_by_date.setText(QCoreApplication.translate("SearchTab", u"\u0414\u0430\u0442\u0435", None))
        self.label_2.setText(QCoreApplication.translate("SearchTab", u"\u0421\u041e\u0420\u0422\u0418\u0420\u041e\u0412\u041a\u0410", None))
        self.groupBox_2.setTitle("")
        self.r_desc.setText(QCoreApplication.translate("SearchTab", u"\u0421\u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u0442\u0430\u0440\u044b\u0435", None))
        self.r_asc.setText(QCoreApplication.translate("SearchTab", u"\u0421\u043d\u0430\u0447\u0430\u043b\u0430 \u043d\u043e\u0432\u044b\u0435", None))
        self.label_3.setText(QCoreApplication.translate("SearchTab", u"\u041b\u0418\u041c\u0418\u0422", None))
    # retranslateUi

