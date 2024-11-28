# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_newtSXASi.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_OrderTab(object):
    def setupUi(self, OrderTab):
        if not OrderTab.objectName():
            OrderTab.setObjectName(u"OrderTab")
        OrderTab.resize(1118, 708)
        OrderTab.setStyleSheet(u"#rigth_widget {\n"
"	background-color: rgb(39, 50, 56);\n"
"}\n"
"\n"
"#top_widget {\n"
"background-color: rgb(54, 71, 79);\n"
"}\n"
"\n"
"#bottom_widget {\n"
"background-color: rgb(54, 71, 79);\n"
"}\n"
"\n"
"#scheme_widget {\n"
"	background-color: rgb(241, 244, 249);\n"
"}\n"
"\n"
".QGroupBox {\n"
"border: null;\n"
"}\n"
"\n"
".QRadioButton, .QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border: null;\n"
"	padding: 10%;\n"
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
".QRadioButton::indicator{\n"
"width: 0;\n"
"}\n"
"\n"
"#doors_height {\n"
"color: black;\n"
"}\n"
"\n"
"#nomenclatures_widget, #nomenclatures_widget  QWidget {\n"
"background-color: rgb(136, 139, 145);\n"
"}\n"
"\n"
".QTabWidget > .QTabBar::tab {\n"
"    height: 0;\n"
"}\n"
"\n"
".QTabWidget {\n"
"    outline: 0;\n"
"}")
        self.horizontalLayout = QHBoxLayout(OrderTab)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_widget = QWidget(OrderTab)
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
        self.btn_exit = QPushButton(self.top_widget)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u"icons/cross.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_exit)

        self.horizontalSpacer = QSpacerItem(18, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_save = QPushButton(self.top_widget)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy1.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u"icons/disk.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_save)

        self.btn_save_2 = QPushButton(self.top_widget)
        self.btn_save_2.setObjectName(u"btn_save_2")
        sizePolicy1.setHeightForWidth(self.btn_save_2.sizePolicy().hasHeightForWidth())
        self.btn_save_2.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u"icons/export.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_2.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_save_2)

        self.btn_document = QPushButton(self.top_widget)
        self.btn_document.setObjectName(u"btn_document")
        sizePolicy1.setHeightForWidth(self.btn_document.sizePolicy().hasHeightForWidth())
        self.btn_document.setSizePolicy(sizePolicy1)
        icon3 = QIcon()
        icon3.addFile(u"icons/document.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_document.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_document)

        self.btn_update = QPushButton(self.top_widget)
        self.btn_update.setObjectName(u"btn_update")
        sizePolicy1.setHeightForWidth(self.btn_update.sizePolicy().hasHeightForWidth())
        self.btn_update.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u"icons/refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.btn_update)

        self.horizontalSpacer_2 = QSpacerItem(19, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_add_door = QPushButton(self.top_widget)
        self.btn_add_door.setObjectName(u"btn_add_door")
        sizePolicy1.setHeightForWidth(self.btn_add_door.sizePolicy().hasHeightForWidth())
        self.btn_add_door.setSizePolicy(sizePolicy1)
        icon5 = QIcon()
        icon5.addFile(u"icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_door.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.btn_add_door)

        self.btn_menu = QPushButton(self.top_widget)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy1.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy1)
        icon6 = QIcon()
        icon6.addFile(u"icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.btn_menu)


        self.verticalLayout.addWidget(self.top_widget)

        self.scrollArea = QScrollArea(OrderTab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 790, 632))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scheme_widget = QWidget(self.scrollAreaWidgetContents)
        self.scheme_widget.setObjectName(u"scheme_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.scheme_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.doors_height = QLabel(self.scheme_widget)
        self.doors_height.setObjectName(u"doors_height")

        self.horizontalLayout_5.addWidget(self.doors_height)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.horizontalLayout_6.addWidget(self.scheme_widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.bottom_widget = QWidget(OrderTab)
        self.bottom_widget.setObjectName(u"bottom_widget")
        sizePolicy.setHeightForWidth(self.bottom_widget.sizePolicy().hasHeightForWidth())
        self.bottom_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(56, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.r_merge = QRadioButton(self.bottom_widget)
        self.r_merge.setObjectName(u"r_merge")
        sizePolicy1.setHeightForWidth(self.r_merge.sizePolicy().hasHeightForWidth())
        self.r_merge.setSizePolicy(sizePolicy1)
        icon7 = QIcon()
        icon7.addFile(u"icons/apps.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.r_merge.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.r_merge)

        self.r_unmerge = QRadioButton(self.bottom_widget)
        self.r_unmerge.setObjectName(u"r_unmerge")
        sizePolicy1.setHeightForWidth(self.r_unmerge.sizePolicy().hasHeightForWidth())
        self.r_unmerge.setSizePolicy(sizePolicy1)
        icon8 = QIcon()
        icon8.addFile(u"icons/arrows.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.r_unmerge.setIcon(icon8)

        self.horizontalLayout_3.addWidget(self.r_unmerge)

        self.r_material = QRadioButton(self.bottom_widget)
        self.r_material.setObjectName(u"r_material")
        sizePolicy1.setHeightForWidth(self.r_material.sizePolicy().hasHeightForWidth())
        self.r_material.setSizePolicy(sizePolicy1)
        icon9 = QIcon()
        icon9.addFile(u"icons/palette.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.r_material.setIcon(icon9)

        self.horizontalLayout_3.addWidget(self.r_material)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.r_delete_door = QRadioButton(self.bottom_widget)
        self.r_delete_door.setObjectName(u"r_delete_door")
        sizePolicy1.setHeightForWidth(self.r_delete_door.sizePolicy().hasHeightForWidth())
        self.r_delete_door.setSizePolicy(sizePolicy1)
        icon10 = QIcon()
        icon10.addFile(u"icons/trash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.r_delete_door.setIcon(icon10)

        self.horizontalLayout_3.addWidget(self.r_delete_door)

        self.r_edit_door = QRadioButton(self.bottom_widget)
        self.r_edit_door.setObjectName(u"r_edit_door")
        sizePolicy1.setHeightForWidth(self.r_edit_door.sizePolicy().hasHeightForWidth())
        self.r_edit_door.setSizePolicy(sizePolicy1)
        icon11 = QIcon()
        icon11.addFile(u"icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.r_edit_door.setIcon(icon11)

        self.horizontalLayout_3.addWidget(self.r_edit_door)

        self.r_double = QRadioButton(self.bottom_widget)
        self.r_double.setObjectName(u"r_double")
        sizePolicy1.setHeightForWidth(self.r_double.sizePolicy().hasHeightForWidth())
        self.r_double.setSizePolicy(sizePolicy1)
        icon12 = QIcon()
        icon12.addFile(u"icons/layers.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.r_double.setIcon(icon12)

        self.horizontalLayout_3.addWidget(self.r_double)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.bottom_widget)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.rigth_widget = QWidget(OrderTab)
        self.rigth_widget.setObjectName(u"rigth_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.rigth_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget = QTabWidget(self.rigth_widget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_9 = QHBoxLayout(self.tab)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.right_pannel = QScrollArea(self.tab)
        self.right_pannel.setObjectName(u"right_pannel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.right_pannel.sizePolicy().hasHeightForWidth())
        self.right_pannel.setSizePolicy(sizePolicy3)
        self.right_pannel.setMinimumSize(QSize(300, 0))
        self.right_pannel.setMaximumSize(QSize(300, 16777215))
        self.right_pannel.setStyleSheet(u"#right_pannel {\n"
"	border: null;\n"
"}\n"
"\n"
"#right_pannel_content {\n"
"	background-color: rgb(39, 50, 56);\n"
"}\n"
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
".QSpinBox, .QDateEdit, .QLineEdit, .QTextEdit,  .QCheckBox, #c_guide, #c_guide_decor{\n"
"background-color: rgb(54, 71, 79);\n"
"border: null;\n"
"padding: 5%;"
                        "\n"
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
"QMenu::itemQComboBox QAbstractItemView{\n"
"color: white;\n"
"            padding: 5px 20px;\n"
"         "
                        "   background-color: rgb(39, 50, 56);\n"
"            }\n"
"QComboBox QAbstractItemView:selected {\n"
"             background-color: rgb(69, 75, 84);\n"
"            }")
        self.right_pannel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.right_pannel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_pannel.setWidgetResizable(True)
        self.right_pannel_content = QWidget()
        self.right_pannel_content.setObjectName(u"right_pannel_content")
        self.right_pannel_content.setGeometry(QRect(0, 0, 290, 1082))
        self.verticalLayout_4 = QVBoxLayout(self.right_pannel_content)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 6, 6, -1)
        self.height = QLabel(self.right_pannel_content)
        self.height.setObjectName(u"height")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.height)

        self.inp_height = QSpinBox(self.right_pannel_content)
        self.inp_height.setObjectName(u"inp_height")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.inp_height.sizePolicy().hasHeightForWidth())
        self.inp_height.setSizePolicy(sizePolicy4)
        self.inp_height.setFocusPolicy(Qt.ClickFocus)
        self.inp_height.setWrapping(False)
        self.inp_height.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.inp_height.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.inp_height.setKeyboardTracking(True)
        self.inp_height.setProperty("showGroupSeparator", False)
        self.inp_height.setMinimum(500)
        self.inp_height.setMaximum(9999)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.inp_height)

        self.long_2 = QLabel(self.right_pannel_content)
        self.long_2.setObjectName(u"long_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.long_2)

        self.inp_width = QSpinBox(self.right_pannel_content)
        self.inp_width.setObjectName(u"inp_width")
        sizePolicy4.setHeightForWidth(self.inp_width.sizePolicy().hasHeightForWidth())
        self.inp_width.setSizePolicy(sizePolicy4)
        self.inp_width.setFocusPolicy(Qt.ClickFocus)
        self.inp_width.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.inp_width.setMinimum(500)
        self.inp_width.setMaximum(9999)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inp_width)

        self.longL2 = QLabel(self.right_pannel_content)
        self.longL2.setObjectName(u"longL2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.longL2)

        self.inp_quide_long = QLineEdit(self.right_pannel_content)
        self.inp_quide_long.setObjectName(u"inp_quide_long")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.inp_quide_long.sizePolicy().hasHeightForWidth())
        self.inp_quide_long.setSizePolicy(sizePolicy5)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.inp_quide_long)

        self.date = QLabel(self.right_pannel_content)
        self.date.setObjectName(u"date")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.date)

        self.inp_date = QDateEdit(self.right_pannel_content)
        self.inp_date.setObjectName(u"inp_date")
        sizePolicy5.setHeightForWidth(self.inp_date.sizePolicy().hasHeightForWidth())
        self.inp_date.setSizePolicy(sizePolicy5)
        self.inp_date.setFocusPolicy(Qt.ClickFocus)
        self.inp_date.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.inp_date)

        self.norder = QLabel(self.right_pannel_content)
        self.norder.setObjectName(u"norder")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.norder)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.inp_responsibility = QLineEdit(self.right_pannel_content)
        self.inp_responsibility.setObjectName(u"inp_responsibility")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.inp_responsibility.sizePolicy().hasHeightForWidth())
        self.inp_responsibility.setSizePolicy(sizePolicy6)
        self.inp_responsibility.setMaximumSize(QSize(50, 16777215))
        self.inp_responsibility.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.inp_responsibility)

        self.inp_order_number = QSpinBox(self.right_pannel_content)
        self.inp_order_number.setObjectName(u"inp_order_number")
        sizePolicy5.setHeightForWidth(self.inp_order_number.sizePolicy().hasHeightForWidth())
        self.inp_order_number.setSizePolicy(sizePolicy5)
        self.inp_order_number.setFocusPolicy(Qt.ClickFocus)
        self.inp_order_number.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.inp_order_number.setMinimum(0)
        self.inp_order_number.setMaximum(999)
        self.inp_order_number.setStepType(QAbstractSpinBox.DefaultStepType)
        self.inp_order_number.setValue(0)

        self.horizontalLayout_8.addWidget(self.inp_order_number)

        self.norder_2 = QLabel(self.right_pannel_content)
        self.norder_2.setObjectName(u"norder_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.norder_2.sizePolicy().hasHeightForWidth())
        self.norder_2.setSizePolicy(sizePolicy7)
        self.norder_2.setScaledContents(False)
        self.norder_2.setIndent(0)

        self.horizontalLayout_8.addWidget(self.norder_2)

        self.inp_order_number_part = QSpinBox(self.right_pannel_content)
        self.inp_order_number_part.setObjectName(u"inp_order_number_part")
        sizePolicy5.setHeightForWidth(self.inp_order_number_part.sizePolicy().hasHeightForWidth())
        self.inp_order_number_part.setSizePolicy(sizePolicy5)
        self.inp_order_number_part.setFocusPolicy(Qt.ClickFocus)
        self.inp_order_number_part.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.inp_order_number_part.setMinimum(0)
        self.inp_order_number_part.setMaximum(999)
        self.inp_order_number_part.setStepType(QAbstractSpinBox.DefaultStepType)
        self.inp_order_number_part.setValue(0)

        self.horizontalLayout_8.addWidget(self.inp_order_number_part)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_8)

        self.dateout = QLabel(self.right_pannel_content)
        self.dateout.setObjectName(u"dateout")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.dateout)

        self.inp_date_uot = QDateEdit(self.right_pannel_content)
        self.inp_date_uot.setObjectName(u"inp_date_uot")
        sizePolicy5.setHeightForWidth(self.inp_date_uot.sizePolicy().hasHeightForWidth())
        self.inp_date_uot.setSizePolicy(sizePolicy5)
        self.inp_date_uot.setFocusPolicy(Qt.ClickFocus)
        self.inp_date_uot.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.inp_date_uot)

        self.discription_10 = QLabel(self.right_pannel_content)
        self.discription_10.setObjectName(u"discription_10")
        self.discription_10.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.discription_10)

        self.inp_overlap_count = QLineEdit(self.right_pannel_content)
        self.inp_overlap_count.setObjectName(u"inp_overlap_count")
        sizePolicy5.setHeightForWidth(self.inp_overlap_count.sizePolicy().hasHeightForWidth())
        self.inp_overlap_count.setSizePolicy(sizePolicy5)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.inp_overlap_count)

        self.discription_6 = QLabel(self.right_pannel_content)
        self.discription_6.setObjectName(u"discription_6")
        self.discription_6.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.discription_6)

        self.ch_need_shlegel = QCheckBox(self.right_pannel_content)
        self.ch_need_shlegel.setObjectName(u"ch_need_shlegel")
        self.ch_need_shlegel.setChecked(True)
        self.ch_need_shlegel.setTristate(False)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.ch_need_shlegel)

        self.discription_11 = QLabel(self.right_pannel_content)
        self.discription_11.setObjectName(u"discription_11")
        self.discription_11.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.discription_11)

        self.c_bot_system = QCheckBox(self.right_pannel_content)
        self.c_bot_system.setObjectName(u"c_bot_system")
        self.c_bot_system.setChecked(False)
        self.c_bot_system.setTristate(False)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.c_bot_system)

        self.discription_12 = QLabel(self.right_pannel_content)
        self.discription_12.setObjectName(u"discription_12")
        self.discription_12.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.discription_12)

        self.c_guide = QComboBox(self.right_pannel_content)
        self.c_guide.addItem("")
        self.c_guide.addItem("")
        self.c_guide.addItem("")
        self.c_guide.setObjectName(u"c_guide")
        self.c_guide.setFocusPolicy(Qt.NoFocus)
        self.c_guide.setInsertPolicy(QComboBox.InsertAtBottom)
        self.c_guide.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.c_guide.setDuplicatesEnabled(False)
        self.c_guide.setFrame(False)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.c_guide)

        self.lbl_guide_decor = QLabel(self.right_pannel_content)
        self.lbl_guide_decor.setObjectName(u"lbl_guide_decor")
        self.lbl_guide_decor.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.lbl_guide_decor)

        self.c_guide_decor = QSpinBox(self.right_pannel_content)
        self.c_guide_decor.setObjectName(u"c_guide_decor")
        sizePolicy4.setHeightForWidth(self.c_guide_decor.sizePolicy().hasHeightForWidth())
        self.c_guide_decor.setSizePolicy(sizePolicy4)
        self.c_guide_decor.setFocusPolicy(Qt.ClickFocus)
        self.c_guide_decor.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.c_guide_decor.setMinimum(0)
        self.c_guide_decor.setMaximum(10)
        self.c_guide_decor.setValue(2)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.c_guide_decor)


        self.verticalLayout_4.addLayout(self.formLayout)

        self.discription = QLabel(self.right_pannel_content)
        self.discription.setObjectName(u"discription")
        self.discription.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.discription)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.inp_description = QTextEdit(self.right_pannel_content)
        self.inp_description.setObjectName(u"inp_description")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.inp_description.sizePolicy().hasHeightForWidth())
        self.inp_description.setSizePolicy(sizePolicy8)

        self.verticalLayout_3.addWidget(self.inp_description)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(-1, 16, -1, 0)
        self.color_2 = QLabel(self.right_pannel_content)
        self.color_2.setObjectName(u"color_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.color_2)

        self.btn_color = QPushButton(self.right_pannel_content)
        self.btn_color.setObjectName(u"btn_color")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.btn_color)

        self.discription_2 = QLabel(self.right_pannel_content)
        self.discription_2.setObjectName(u"discription_2")
        self.discription_2.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.discription_2)

        self.btn_customer = QPushButton(self.right_pannel_content)
        self.btn_customer.setObjectName(u"btn_customer")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.btn_customer)

        self.discription_4 = QLabel(self.right_pannel_content)
        self.discription_4.setObjectName(u"discription_4")
        self.discription_4.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.discription_4)

        self.btn_profile = QPushButton(self.right_pannel_content)
        self.btn_profile.setObjectName(u"btn_profile")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.btn_profile)

        self.discription_3 = QLabel(self.right_pannel_content)
        self.discription_3.setObjectName(u"discription_3")
        self.discription_3.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.discription_3)

        self.btn_rigel = QPushButton(self.right_pannel_content)
        self.btn_rigel.setObjectName(u"btn_rigel")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.btn_rigel)


        self.verticalLayout_4.addLayout(self.formLayout_2)

        self.groupBox_8 = QGroupBox(self.right_pannel_content)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_4 = QGridLayout(self.groupBox_8)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.groupBox_8)

        self.discription_9 = QLabel(self.right_pannel_content)
        self.discription_9.setObjectName(u"discription_9")
        self.discription_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.discription_9)

        self.c_delivery_config = QComboBox(self.right_pannel_content)
        self.c_delivery_config.addItem("")
        self.c_delivery_config.addItem("")
        self.c_delivery_config.setObjectName(u"c_delivery_config")
        self.c_delivery_config.setFocusPolicy(Qt.NoFocus)
        self.c_delivery_config.setInsertPolicy(QComboBox.InsertAtBottom)
        self.c_delivery_config.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.c_delivery_config.setDuplicatesEnabled(False)
        self.c_delivery_config.setFrame(False)

        self.verticalLayout_4.addWidget(self.c_delivery_config)

        self.c_pack_config = QComboBox(self.right_pannel_content)
        self.c_pack_config.addItem("")
        self.c_pack_config.addItem("")
        self.c_pack_config.addItem("")
        self.c_pack_config.addItem("")
        self.c_pack_config.setObjectName(u"c_pack_config")
        self.c_pack_config.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_4.addWidget(self.c_pack_config)

        self.c_set_config = QComboBox(self.right_pannel_content)
        self.c_set_config.addItem("")
        self.c_set_config.addItem("")
        self.c_set_config.addItem("")
        self.c_set_config.setObjectName(u"c_set_config")
        self.c_set_config.setEnabled(True)
        self.c_set_config.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_4.addWidget(self.c_set_config)

        self.discription_8 = QLabel(self.right_pannel_content)
        self.discription_8.setObjectName(u"discription_8")
        self.discription_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.discription_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.inp_additional_materials = QTextEdit(self.right_pannel_content)
        self.inp_additional_materials.setObjectName(u"inp_additional_materials")
        sizePolicy8.setHeightForWidth(self.inp_additional_materials.sizePolicy().hasHeightForWidth())
        self.inp_additional_materials.setSizePolicy(sizePolicy8)

        self.verticalLayout_7.addWidget(self.inp_additional_materials)


        self.verticalLayout_4.addLayout(self.verticalLayout_7)

        self.right_pannel.setWidget(self.right_pannel_content)

        self.horizontalLayout_9.addWidget(self.right_pannel)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"#scrollArea_2 {\n"
"	border: null;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents_2 {\n"
"	background-color: rgb(39, 50, 56);\n"
"}\n"
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
".QSpinBox,.QDoubleSpinBox, .QDateEdit, .QLineEdit, .QTextEdit,  .QCheckBox, #c_guide, #c_guide_decor{\n"
"background-color: rgb(54, 71, 79);\n"
"border: "
                        "null;\n"
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
"QMenu::itemQComboBox QAbstractItemView{\n"
"color: white;\n"
"            padding: 5"
                        "px 20px;\n"
"            background-color: rgb(39, 50, 56);\n"
"            }\n"
"QComboBox QAbstractItemView:selected {\n"
"             background-color: rgb(69, 75, 84);\n"
"            }")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.scrollArea_2 = QScrollArea(self.tab_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -351, 296, 1032))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.color_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_4.setObjectName(u"color_4")

        self.gridLayout.addWidget(self.color_4, 1, 0, 1, 2)

        self.pushButton_6 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 7, 2, 1, 1)

        self.color_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_3.setObjectName(u"color_3")
        self.color_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.color_3, 0, 0, 1, 4)

        self.materials_nomenclature_widget = QWidget(self.scrollAreaWidgetContents_2)
        self.materials_nomenclature_widget.setObjectName(u"materials_nomenclature_widget")
        self.gridLayout_2 = QGridLayout(self.materials_nomenclature_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.materials_nomenclature_widget, 19, 0, 1, 4)

        self.color_25 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_25.setObjectName(u"color_25")
        self.color_25.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.color_25, 20, 0, 1, 4)

        self.color_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_22.setObjectName(u"color_22")
        self.color_22.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.color_22, 17, 0, 1, 4)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_3.setDecimals(1)

        self.gridLayout.addWidget(self.doubleSpinBox_3, 3, 3, 1, 1)

        self.color_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_15.setObjectName(u"color_15")

        self.gridLayout.addWidget(self.color_15, 14, 0, 1, 2)

        self.color_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_6.setObjectName(u"color_6")

        self.gridLayout.addWidget(self.color_6, 3, 0, 1, 2)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_4.setDecimals(1)

        self.gridLayout.addWidget(self.doubleSpinBox_4, 4, 3, 1, 1)

        self.pushButton_9 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 10, 2, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox.setDecimals(1)

        self.gridLayout.addWidget(self.doubleSpinBox, 1, 3, 1, 1)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_6.setDecimals(1)

        self.gridLayout.addWidget(self.doubleSpinBox_6, 7, 3, 1, 1)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_5.setDecimals(1)

        self.gridLayout.addWidget(self.doubleSpinBox_5, 5, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 4, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 5, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout.addWidget(self.pushButton_12, 16, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 8, 2, 1, 1)

        self.color_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_10.setObjectName(u"color_10")

        self.gridLayout.addWidget(self.color_10, 7, 0, 1, 2)

        self.spinBox_15 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_15.setObjectName(u"spinBox_15")
        self.spinBox_15.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.spinBox_15, 22, 3, 1, 1)

        self.color_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_7.setObjectName(u"color_7")

        self.gridLayout.addWidget(self.color_7, 4, 0, 1, 2)

        self.color_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_23.setObjectName(u"color_23")
        self.color_23.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.color_23, 18, 0, 1, 4)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")
        self.doubleSpinBox_9.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_9.setDecimals(1)

        self.gridLayout.addWidget(self.doubleSpinBox_9, 10, 3, 1, 1)

        self.color_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_18.setObjectName(u"color_18")

        self.gridLayout.addWidget(self.color_18, 15, 0, 1, 2)

        self.spinBox_11 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.spinBox_11, 14, 3, 1, 1)

        self.spinBox_14 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_14.setObjectName(u"spinBox_14")
        self.spinBox_14.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.spinBox_14, 21, 3, 1, 1)

        self.color_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_19.setObjectName(u"color_19")

        self.gridLayout.addWidget(self.color_19, 21, 0, 1, 2)

        self.pushButton_15 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout.addWidget(self.pushButton_15, 22, 2, 1, 1)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)

        self.pushButton_16 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        icon13 = QIcon()
        icon13.addFile(u"icons/sircle-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon13)

        self.gridLayout.addWidget(self.pushButton_16, 27, 0, 1, 4)

        self.color_24 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_24.setObjectName(u"color_24")
        self.color_24.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.color_24, 24, 0, 1, 4)

        self.color_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_16.setObjectName(u"color_16")

        self.gridLayout.addWidget(self.color_16, 16, 0, 1, 2)

        self.color_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_13.setObjectName(u"color_13")

        self.gridLayout.addWidget(self.color_13, 10, 0, 1, 2)

        self.color_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_9.setObjectName(u"color_9")
        self.color_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.color_9, 6, 0, 1, 4)

        self.color_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_11.setObjectName(u"color_11")

        self.gridLayout.addWidget(self.color_11, 8, 0, 1, 2)

        self.color_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_8.setObjectName(u"color_8")

        self.gridLayout.addWidget(self.color_8, 5, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)

        self.additional_nomenclature_widget_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.additional_nomenclature_widget_2.setObjectName(u"additional_nomenclature_widget_2")
        self.gridLayout_3 = QGridLayout(self.additional_nomenclature_widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.additional_nomenclature_widget_2, 26, 0, 1, 4)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_7.setDecimals(1)

        self.gridLayout.addWidget(self.doubleSpinBox_7, 8, 3, 1, 1)

        self.color_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_17.setObjectName(u"color_17")
        self.color_17.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.color_17, 13, 0, 1, 4)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 9, 2, 1, 1)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")
        self.doubleSpinBox_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_8.setDecimals(1)

        self.gridLayout.addWidget(self.doubleSpinBox_8, 9, 3, 1, 1)

        self.color_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_12.setObjectName(u"color_12")

        self.gridLayout.addWidget(self.color_12, 9, 0, 1, 2)

        self.pushButton_11 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout.addWidget(self.pushButton_11, 14, 2, 1, 1)

        self.color_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_20.setObjectName(u"color_20")

        self.gridLayout.addWidget(self.color_20, 22, 0, 1, 2)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_2.setDecimals(1)

        self.gridLayout.addWidget(self.doubleSpinBox_2, 2, 3, 1, 1)

        self.pushButton_13 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout.addWidget(self.pushButton_13, 15, 2, 1, 1)

        self.color_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_5.setObjectName(u"color_5")

        self.gridLayout.addWidget(self.color_5, 2, 0, 1, 2)

        self.spinBox_12 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_12.setObjectName(u"spinBox_12")
        self.spinBox_12.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.spinBox_12, 16, 3, 1, 1)

        self.color_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_21.setObjectName(u"color_21")
        self.color_21.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.color_21, 23, 0, 1, 4)

        self.spinBox_13 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.spinBox_13, 15, 3, 1, 1)

        self.pushButton_14 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout.addWidget(self.pushButton_14, 21, 2, 1, 1)

        self.color_26 = QLabel(self.scrollAreaWidgetContents_2)
        self.color_26.setObjectName(u"color_26")
        self.color_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.color_26, 28, 0, 1, 4)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.rigth_widget)


        self.retranslateUi(OrderTab)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(OrderTab)
    # setupUi

    def retranslateUi(self, OrderTab):
        OrderTab.setWindowTitle(QCoreApplication.translate("OrderTab", u"Form", None))
        self.btn_exit.setText("")
        self.btn_save.setText(QCoreApplication.translate("OrderTab", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_save_2.setText(QCoreApplication.translate("OrderTab", u"\u041f\u0435\u0440\u0435\u043d\u0435\u0441\u0442\u0438 \u0432 1\u0421", None))
        self.btn_document.setText(QCoreApplication.translate("OrderTab", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.btn_update.setText(QCoreApplication.translate("OrderTab", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.btn_add_door.setText(QCoreApplication.translate("OrderTab", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0432\u0435\u0440\u044c", None))
        self.btn_menu.setText("")
        self.doors_height.setText(QCoreApplication.translate("OrderTab", u"0", None))
        self.r_merge.setText(QCoreApplication.translate("OrderTab", u"\u041e\u0431\u044a\u0435\u0434\u0435\u043d\u0438\u0442\u044c", None))
        self.r_unmerge.setText(QCoreApplication.translate("OrderTab", u"\u0420\u0430\u0437\u044a\u0435\u0434\u0435\u043d\u0438\u0442\u044c", None))
        self.r_material.setText(QCoreApplication.translate("OrderTab", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b", None))
        self.r_delete_door.setText(QCoreApplication.translate("OrderTab", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.r_edit_door.setText(QCoreApplication.translate("OrderTab", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.r_double.setText(QCoreApplication.translate("OrderTab", u"\u0414\u0443\u0431\u043b\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.height.setText(QCoreApplication.translate("OrderTab", u"\u0412\u042b\u0421\u041e\u0422\u0410", None))
        self.long_2.setText(QCoreApplication.translate("OrderTab", u"\u0428\u0418\u0420\u0418\u041d\u0410", None))
        self.longL2.setText(QCoreApplication.translate("OrderTab", u"\u0414\u041b\u0418\u041d\u0410 \u041d", None))
        self.inp_quide_long.setPlaceholderText(QCoreApplication.translate("OrderTab", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438", None))
        self.date.setText(QCoreApplication.translate("OrderTab", u"\u0414\u0410\u0422\u0410", None))
        self.norder.setText(QCoreApplication.translate("OrderTab", u"\u2116 \u0417\u0410\u041a\u0410\u0417\u0410", None))
        self.inp_order_number.setSuffix("")
        self.inp_order_number.setPrefix("")
        self.norder_2.setText(QCoreApplication.translate("OrderTab", u"/", None))
        self.inp_order_number_part.setSuffix("")
        self.inp_order_number_part.setPrefix("")
        self.dateout.setText(QCoreApplication.translate("OrderTab", u"\u0414\u0410\u0422\u0410 \u0413\u041e\u0422.", None))
        self.discription_10.setText(QCoreApplication.translate("OrderTab", u"\u041f\u0415\u0420\u0415\u0425\u041b\u0415\u0421\u0422", None))
        self.inp_overlap_count.setPlaceholderText(QCoreApplication.translate("OrderTab", u"\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u044b\u0439", None))
        self.discription_6.setText(QCoreApplication.translate("OrderTab", u"\u0428\u041b\u0415\u0413\u0415\u041b\u042c", None))
        self.ch_need_shlegel.setText(QCoreApplication.translate("OrderTab", u"\u041d\u0443\u0436\u0435\u043d", None))
        self.discription_11.setText(QCoreApplication.translate("OrderTab", u"\u0421\u0418\u0421\u0422\u0415\u041c\u0410", None))
        self.c_bot_system.setText(QCoreApplication.translate("OrderTab", u"\u0412\u0435\u0440\u0445\u043d\u044f\u044f \u043f\u043e\u0434\u0432\u0435\u0441\u043d\u0430\u044f", None))
        self.discription_12.setText(QCoreApplication.translate("OrderTab", u"\u041d\u0410\u041f\u0420\u0410\u0412\u041b.", None))
        self.c_guide.setItemText(0, QCoreApplication.translate("OrderTab", u"2 \u043f\u043e\u043b\u043e\u0441\u044b", None))
        self.c_guide.setItemText(1, QCoreApplication.translate("OrderTab", u"1 \u043f\u043e\u043b\u043e\u0441\u0430", None))
        self.c_guide.setItemText(2, QCoreApplication.translate("OrderTab", u"\u0411\u0435\u0437 \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u044f\u044e\u0449\u0438\u0445", None))

        self.lbl_guide_decor.setText(QCoreApplication.translate("OrderTab", u"\u041d\u0410\u041a\u041b\u0410\u0414\u041a.", None))
        self.c_guide_decor.setSuffix("")
        self.discription.setText(QCoreApplication.translate("OrderTab", u"\u041e\u041f\u0418\u0421\u0410\u041d\u0418\u0415", None))
        self.color_2.setText(QCoreApplication.translate("OrderTab", u"\u0426\u0412\u0415\u0422", None))
        self.btn_color.setText(QCoreApplication.translate("OrderTab", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435, \u0447\u0442\u043e\u0431\u044b \u0432\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.discription_2.setText(QCoreApplication.translate("OrderTab", u"\u041a\u041b\u0418\u0415\u041d\u0422", None))
        self.btn_customer.setText(QCoreApplication.translate("OrderTab", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435, \u0447\u0442\u043e\u0431\u044b \u0432\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.discription_4.setText(QCoreApplication.translate("OrderTab", u"\u041f\u0420\u041e\u0424\u0418\u041b\u042c", None))
        self.btn_profile.setText(QCoreApplication.translate("OrderTab", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435, \u0447\u0442\u043e\u0431\u044b \u0432\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.discription_3.setText(QCoreApplication.translate("OrderTab", u"\u0420\u0418\u0413\u0415\u041b\u042c", None))
        self.btn_rigel.setText(QCoreApplication.translate("OrderTab", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435, \u0447\u0442\u043e\u0431\u044b \u0432\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.groupBox_8.setTitle("")
        self.discription_9.setText(QCoreApplication.translate("OrderTab", u"\u041a\u041e\u041d\u0424\u0418\u0413\u0423\u0420\u0410\u0426\u0418\u042f", None))
        self.c_delivery_config.setItemText(0, QCoreApplication.translate("OrderTab", u"\u0411\u0435\u0437 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.c_delivery_config.setItemText(1, QCoreApplication.translate("OrderTab", u"\u0421 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u043e\u0439", None))

        self.c_pack_config.setItemText(0, QCoreApplication.translate("OrderTab", u"\u0412 \u043f\u043b\u0435\u043d\u043a\u0443", None))
        self.c_pack_config.setItemText(1, QCoreApplication.translate("OrderTab", u"\u0412 \u0433\u043e\u0444\u0440\u0443", None))
        self.c_pack_config.setItemText(2, QCoreApplication.translate("OrderTab", u"\u0412 \u044f\u0449\u0438\u043a", None))
        self.c_pack_config.setItemText(3, QCoreApplication.translate("OrderTab", u"\u0411\u0435\u0437 \u0443\u043f\u0430\u043a\u043e\u0432\u043a\u0438", None))

        self.c_set_config.setItemText(0, QCoreApplication.translate("OrderTab", u"\u0421\u0431\u043e\u0440\u043a\u0430", None))
        self.c_set_config.setItemText(1, QCoreApplication.translate("OrderTab", u"\u041d\u0430\u0440\u0435\u0437\u043a\u0430", None))
        self.c_set_config.setItemText(2, QCoreApplication.translate("OrderTab", u"\u041d\u0430\u0440\u0435\u0437\u043a\u0430, \u0421\u0432\u0435\u0440\u043b\u043e\u0432\u043a\u0430", None))

        self.discription_8.setText(QCoreApplication.translate("OrderTab", u"\u0414\u041e\u041f. \u041c\u0410\u0422\u0415\u0420\u0418\u0410\u041b\u042b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("OrderTab", u"Tab 1", None))
        self.color_4.setText(QCoreApplication.translate("OrderTab", u"\u0412\u0435\u0440\u0445\u043d\u044f\u044f", None))
        self.pushButton_6.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.color_3.setText(QCoreApplication.translate("OrderTab", u"\u041d\u0410\u041f\u0420\u0410\u0412\u041b\u042f\u042e\u0429\u0410\u042f", None))
        self.color_25.setText(QCoreApplication.translate("OrderTab", u"\u0423\u0421\u041b\u0423\u0413\u0418", None))
        self.color_22.setText(QCoreApplication.translate("OrderTab", u"\u041c\u0410\u0422\u0415\u0420\u0418\u0410\u041b\u042b", None))
        self.color_15.setText(QCoreApplication.translate("OrderTab", u"\u0423\u043f\u043b\u043e\u0442\u043d\u0438\u0442\u0435\u043b\u044c", None))
        self.color_6.setText(QCoreApplication.translate("OrderTab", u"\u0425\u043e\u0434\u043e\u0432\u043e\u0439", None))
        self.pushButton_9.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.pushButton_4.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.pushButton_5.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.pushButton_12.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.pushButton_7.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.color_10.setText(QCoreApplication.translate("OrderTab", u"\u0412\u0435\u0440\u0445\u043d\u0438\u0439", None))
        self.color_7.setText(QCoreApplication.translate("OrderTab", u"\u041d\u0430\u043a\u043b\u0430\u0434\u043a\u0430", None))
        self.color_23.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.color_18.setText(QCoreApplication.translate("OrderTab", u"\u0420\u043e\u043b\u0438\u043a\u0438", None))
        self.color_19.setText(QCoreApplication.translate("OrderTab", u"\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430", None))
        self.pushButton_15.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.pushButton_16.setText(QCoreApplication.translate("OrderTab", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0437\u0438\u0446\u0438\u044e", None))
        self.color_24.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.color_16.setText(QCoreApplication.translate("OrderTab", u"\u0428\u043b\u0435\u0433\u0435\u043b\u044c", None))
        self.color_13.setText(QCoreApplication.translate("OrderTab", u"\u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439", None))
        self.color_9.setText(QCoreApplication.translate("OrderTab", u"\u041f\u0420\u041e\u0424\u0418\u041b\u042c", None))
        self.color_11.setText(QCoreApplication.translate("OrderTab", u"\u041d\u0438\u0436\u043d\u0438\u0439", None))
        self.color_8.setText(QCoreApplication.translate("OrderTab", u"\u0417\u0430\u0433\u043b\u0443\u0448\u043a\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.color_17.setText(QCoreApplication.translate("OrderTab", u"\u0424\u0423\u0420\u041d\u0418\u0422\u0423\u0420\u0410", None))
        self.pushButton_3.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.pushButton_8.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.color_12.setText(QCoreApplication.translate("OrderTab", u"\u0420\u0438\u0433\u0435\u043b\u044c", None))
        self.pushButton_11.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.color_20.setText(QCoreApplication.translate("OrderTab", u"\u0421\u0431\u043e\u0440\u043a\u0430", None))
        self.pushButton_13.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.color_5.setText(QCoreApplication.translate("OrderTab", u"\u041d\u0438\u0436\u043d\u044f\u044f", None))
        self.color_21.setText(QCoreApplication.translate("OrderTab", u"\u0414\u041e\u041f\u041e\u041b\u041d\u0418\u0422\u0415\u041b\u042c\u041d\u041e", None))
        self.pushButton_14.setText(QCoreApplication.translate("OrderTab", u"...", None))
        self.color_26.setText(QCoreApplication.translate("OrderTab", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c: 0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("OrderTab", u"Tab 2", None))
    # retranslateUi

