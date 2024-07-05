# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orderlTwxmp.ui'
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
    QDateEdit, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_OrderTab(object):
    def setupUi(self, OrderTab):
        if not OrderTab.objectName():
            OrderTab.setObjectName(u"OrderTab")
        OrderTab.resize(1028, 661)
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

        self.btn_document = QPushButton(self.top_widget)
        self.btn_document.setObjectName(u"btn_document")
        sizePolicy1.setHeightForWidth(self.btn_document.sizePolicy().hasHeightForWidth())
        self.btn_document.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u"icons/document.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_document.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_document)

        self.btn_update = QPushButton(self.top_widget)
        self.btn_update.setObjectName(u"btn_update")
        sizePolicy1.setHeightForWidth(self.btn_update.sizePolicy().hasHeightForWidth())
        self.btn_update.setSizePolicy(sizePolicy1)
        icon3 = QIcon()
        icon3.addFile(u"icons/refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_update)

        self.horizontalSpacer_2 = QSpacerItem(19, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_add_door = QPushButton(self.top_widget)
        self.btn_add_door.setObjectName(u"btn_add_door")
        sizePolicy1.setHeightForWidth(self.btn_add_door.sizePolicy().hasHeightForWidth())
        self.btn_add_door.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u"icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_door.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.btn_add_door)


        self.verticalLayout.addWidget(self.top_widget)

        self.scrollArea = QScrollArea(OrderTab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 706, 585))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scheme_widget = QWidget(self.scrollAreaWidgetContents)
        self.scheme_widget.setObjectName(u"scheme_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.scheme_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
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
        icon5 = QIcon()
        icon5.addFile(u"icons/apps.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.r_merge.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.r_merge)

        self.r_unmerge = QRadioButton(self.bottom_widget)
        self.r_unmerge.setObjectName(u"r_unmerge")
        sizePolicy1.setHeightForWidth(self.r_unmerge.sizePolicy().hasHeightForWidth())
        self.r_unmerge.setSizePolicy(sizePolicy1)
        icon6 = QIcon()
        icon6.addFile(u"icons/arrows.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.r_unmerge.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.r_unmerge)

        self.r_material = QRadioButton(self.bottom_widget)
        self.r_material.setObjectName(u"r_material")
        sizePolicy1.setHeightForWidth(self.r_material.sizePolicy().hasHeightForWidth())
        self.r_material.setSizePolicy(sizePolicy1)
        icon7 = QIcon()
        icon7.addFile(u"icons/palette.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.r_material.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.r_material)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.r_delete_door = QRadioButton(self.bottom_widget)
        self.r_delete_door.setObjectName(u"r_delete_door")
        sizePolicy1.setHeightForWidth(self.r_delete_door.sizePolicy().hasHeightForWidth())
        self.r_delete_door.setSizePolicy(sizePolicy1)
        icon8 = QIcon()
        icon8.addFile(u"icons/trash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.r_delete_door.setIcon(icon8)

        self.horizontalLayout_3.addWidget(self.r_delete_door)

        self.r_edit_door = QRadioButton(self.bottom_widget)
        self.r_edit_door.setObjectName(u"r_edit_door")
        sizePolicy1.setHeightForWidth(self.r_edit_door.sizePolicy().hasHeightForWidth())
        self.r_edit_door.setSizePolicy(sizePolicy1)
        icon9 = QIcon()
        icon9.addFile(u"icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.r_edit_door.setIcon(icon9)

        self.horizontalLayout_3.addWidget(self.r_edit_door)

        self.r_double = QRadioButton(self.bottom_widget)
        self.r_double.setObjectName(u"r_double")
        sizePolicy1.setHeightForWidth(self.r_double.sizePolicy().hasHeightForWidth())
        self.r_double.setSizePolicy(sizePolicy1)
        self.r_double.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.r_double)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.bottom_widget)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.rigth_widget = QWidget(OrderTab)
        self.rigth_widget.setObjectName(u"rigth_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.rigth_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.right_pannel = QScrollArea(self.rigth_widget)
        self.right_pannel.setObjectName(u"right_pannel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.right_pannel.sizePolicy().hasHeightForWidth())
        self.right_pannel.setSizePolicy(sizePolicy2)
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
".QSpinBox, .QDateEdit, .QLineEdit, .QTextEdit,  .QCheckBox, #c_guide {\n"
"background-color: rgb(54, 71, 79);\n"
"border: null;\n"
"padding: 5%;\n"
"border-col"
                        "or: rgb(200, 200, 200);\n"
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
"            background-c"
                        "olor: rgb(39, 50, 56);\n"
"            }\n"
"QComboBox QAbstractItemView:selected {\n"
"             background-color: rgb(69, 75, 84);\n"
"            }")
        self.right_pannel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.right_pannel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_pannel.setWidgetResizable(True)
        self.right_pannel_content = QWidget()
        self.right_pannel_content.setObjectName(u"right_pannel_content")
        self.right_pannel_content.setGeometry(QRect(0, 0, 290, 998))
        self.verticalLayout_4 = QVBoxLayout(self.right_pannel_content)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 6, 6, -1)
        self.height = QLabel(self.right_pannel_content)
        self.height.setObjectName(u"height")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.height)

        self.inp_height = QSpinBox(self.right_pannel_content)
        self.inp_height.setObjectName(u"inp_height")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.inp_height.sizePolicy().hasHeightForWidth())
        self.inp_height.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.inp_width.sizePolicy().hasHeightForWidth())
        self.inp_width.setSizePolicy(sizePolicy3)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.inp_quide_long.sizePolicy().hasHeightForWidth())
        self.inp_quide_long.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.inp_quide_long)

        self.date = QLabel(self.right_pannel_content)
        self.date.setObjectName(u"date")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.date)

        self.inp_date = QDateEdit(self.right_pannel_content)
        self.inp_date.setObjectName(u"inp_date")
        sizePolicy4.setHeightForWidth(self.inp_date.sizePolicy().hasHeightForWidth())
        self.inp_date.setSizePolicy(sizePolicy4)
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.inp_responsibility.sizePolicy().hasHeightForWidth())
        self.inp_responsibility.setSizePolicy(sizePolicy5)
        self.inp_responsibility.setMaximumSize(QSize(50, 16777215))
        self.inp_responsibility.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.inp_responsibility)

        self.inp_order_number = QSpinBox(self.right_pannel_content)
        self.inp_order_number.setObjectName(u"inp_order_number")
        sizePolicy4.setHeightForWidth(self.inp_order_number.sizePolicy().hasHeightForWidth())
        self.inp_order_number.setSizePolicy(sizePolicy4)
        self.inp_order_number.setFocusPolicy(Qt.ClickFocus)
        self.inp_order_number.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.inp_order_number.setMinimum(0)
        self.inp_order_number.setMaximum(999)
        self.inp_order_number.setStepType(QAbstractSpinBox.DefaultStepType)
        self.inp_order_number.setValue(0)

        self.horizontalLayout_8.addWidget(self.inp_order_number)

        self.norder_2 = QLabel(self.right_pannel_content)
        self.norder_2.setObjectName(u"norder_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.norder_2.sizePolicy().hasHeightForWidth())
        self.norder_2.setSizePolicy(sizePolicy6)
        self.norder_2.setScaledContents(False)
        self.norder_2.setIndent(0)

        self.horizontalLayout_8.addWidget(self.norder_2)

        self.inp_order_number_part = QSpinBox(self.right_pannel_content)
        self.inp_order_number_part.setObjectName(u"inp_order_number_part")
        sizePolicy4.setHeightForWidth(self.inp_order_number_part.sizePolicy().hasHeightForWidth())
        self.inp_order_number_part.setSizePolicy(sizePolicy4)
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
        sizePolicy4.setHeightForWidth(self.inp_date_uot.sizePolicy().hasHeightForWidth())
        self.inp_date_uot.setSizePolicy(sizePolicy4)
        self.inp_date_uot.setFocusPolicy(Qt.ClickFocus)
        self.inp_date_uot.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.inp_date_uot)

        self.discription_10 = QLabel(self.right_pannel_content)
        self.discription_10.setObjectName(u"discription_10")
        self.discription_10.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.discription_10)

        self.inp_overlap_count = QLineEdit(self.right_pannel_content)
        self.inp_overlap_count.setObjectName(u"inp_overlap_count")
        sizePolicy4.setHeightForWidth(self.inp_overlap_count.sizePolicy().hasHeightForWidth())
        self.inp_overlap_count.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.inp_overlap_count)

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

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.c_guide)

        self.discription_7 = QLabel(self.right_pannel_content)
        self.discription_7.setObjectName(u"discription_7")
        self.discription_7.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.discription_7)

        self.discription_6 = QLabel(self.right_pannel_content)
        self.discription_6.setObjectName(u"discription_6")
        self.discription_6.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.discription_6)

        self.ch_need_shlegel = QCheckBox(self.right_pannel_content)
        self.ch_need_shlegel.setObjectName(u"ch_need_shlegel")
        self.ch_need_shlegel.setChecked(True)
        self.ch_need_shlegel.setTristate(False)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.ch_need_shlegel)


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
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.inp_description.sizePolicy().hasHeightForWidth())
        self.inp_description.setSizePolicy(sizePolicy7)

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
        sizePolicy7.setHeightForWidth(self.inp_additional_materials.sizePolicy().hasHeightForWidth())
        self.inp_additional_materials.setSizePolicy(sizePolicy7)

        self.verticalLayout_7.addWidget(self.inp_additional_materials)


        self.verticalLayout_4.addLayout(self.verticalLayout_7)

        self.right_pannel.setWidget(self.right_pannel_content)

        self.horizontalLayout_4.addWidget(self.right_pannel)


        self.horizontalLayout.addWidget(self.rigth_widget)


        self.retranslateUi(OrderTab)

        QMetaObject.connectSlotsByName(OrderTab)
    # setupUi

    def retranslateUi(self, OrderTab):
        OrderTab.setWindowTitle(QCoreApplication.translate("OrderTab", u"Form", None))
        self.btn_exit.setText("")
        self.btn_save.setText(QCoreApplication.translate("OrderTab", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_document.setText(QCoreApplication.translate("OrderTab", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.btn_update.setText(QCoreApplication.translate("OrderTab", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.btn_add_door.setText(QCoreApplication.translate("OrderTab", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0432\u0435\u0440\u044c", None))
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
        self.c_guide.setItemText(0, QCoreApplication.translate("OrderTab", u"2 \u043f\u043e\u043b\u043e\u0441\u044b", None))
        self.c_guide.setItemText(1, QCoreApplication.translate("OrderTab", u"1 \u043f\u043e\u043b\u043e\u0441\u0430", None))
        self.c_guide.setItemText(2, QCoreApplication.translate("OrderTab", u"\u0411\u0435\u0437 \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u044f\u044e\u0449\u0438\u0445", None))

        self.discription_7.setText(QCoreApplication.translate("OrderTab", u"\u041d\u0410\u041f\u0420\u0410\u0412\u041b.", None))
        self.discription_6.setText(QCoreApplication.translate("OrderTab", u"\u0428\u041b\u0415\u0413\u0415\u041b\u042c", None))
        self.ch_need_shlegel.setText(QCoreApplication.translate("OrderTab", u"\u041d\u0443\u0436\u0435\u043d", None))
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
    # retranslateUi

