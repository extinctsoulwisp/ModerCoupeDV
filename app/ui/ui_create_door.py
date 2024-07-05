# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_doorqeLbBr.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractSpinBox, QApplication, QCheckBox,
    QDialog, QDialogButtonBox, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_door_edit_dialog(object):
    def setupUi(self, door_edit_dialog):
        if not door_edit_dialog.objectName():
            door_edit_dialog.setObjectName(u"door_edit_dialog")
        door_edit_dialog.setWindowModality(Qt.ApplicationModal)
        door_edit_dialog.resize(907, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(door_edit_dialog.sizePolicy().hasHeightForWidth())
        door_edit_dialog.setSizePolicy(sizePolicy)
        door_edit_dialog.setMaximumSize(QSize(16777215, 16777215))
        door_edit_dialog.setStyleSheet(u"#background {\n"
"background-color: rgb(39, 50, 56);\n"
"}\n"
"\n"
".QLabel {\n"
"	color: rgb(136, 139, 145);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	padding: 10%;\n"
"}\n"
"\n"
".QSpinBox, .QLineEdit, .QCheckBox {\n"
"	border: null;\n"
"	color: white;\n"
"background-color: rgb(54, 71, 79);\n"
"padding: 5;\n"
"}\n"
"\n"
".QPushButton {\n"
"	background-color: transparent;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	padding: 10;\n"
"	border: null;\n"
"}\n"
".QPushButton:hover {\n"
"	background-color: rgb(69, 75, 84);\n"
"}\n"
"\n"
".QRadioButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	padding: 10%;\n"
"	border: null;\n"
"}\n"
"\n"
".QRadioButton:hover, .QCheckBox:hover{\n"
"background-color: rgb(69, 75, 84);\n"
"}\n"
"\n"
".QRadioButton:checked{\n"
"background-color: rgb(38, 165, 154);\n"
"}\n"
"\n"
".QRadioButton::indicator, .QCheckBox::indicator{\n"
"width: 0;\n"
"}")
        self.gridLayout_3 = QGridLayout(door_edit_dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.background = QWidget(door_edit_dialog)
        self.background.setObjectName(u"background")
        self.gridLayout = QGridLayout(self.background)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.background)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.i_cols_count = QSpinBox(self.widget)
        self.i_cols_count.setObjectName(u"i_cols_count")
        self.i_cols_count.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.i_cols_count.setMinimum(1)
        self.i_cols_count.setMaximum(50)

        self.verticalLayout.addWidget(self.i_cols_count)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.i_rows_count = QSpinBox(self.widget)
        self.i_rows_count.setObjectName(u"i_rows_count")
        self.i_rows_count.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.i_rows_count.setMinimum(1)
        self.i_rows_count.setMaximum(50)

        self.verticalLayout.addWidget(self.i_rows_count)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.i_width = QLineEdit(self.widget)
        self.i_width.setObjectName(u"i_width")

        self.verticalLayout.addWidget(self.i_width)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.ch_h_main_rigel = QCheckBox(self.widget)
        self.ch_h_main_rigel.setObjectName(u"ch_h_main_rigel")
        self.ch_h_main_rigel.setChecked(True)

        self.verticalLayout.addWidget(self.ch_h_main_rigel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.fragments_frame = QWidget(self.background)
        self.fragments_frame.setObjectName(u"fragments_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fragments_frame.sizePolicy().hasHeightForWidth())
        self.fragments_frame.setSizePolicy(sizePolicy2)
        self.gridLayout_2 = QGridLayout(self.fragments_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_66 = QWidget(self.fragments_frame)
        self.widget_66.setObjectName(u"widget_66")

        self.gridLayout_2.addWidget(self.widget_66, 6, 3, 1, 1)

        self.widget_126 = QWidget(self.fragments_frame)
        self.widget_126.setObjectName(u"widget_126")

        self.gridLayout_2.addWidget(self.widget_126, 10, 10, 1, 1)

        self.widget_139 = QWidget(self.fragments_frame)
        self.widget_139.setObjectName(u"widget_139")

        self.gridLayout_2.addWidget(self.widget_139, 5, 5, 1, 1)

        self.widget_111 = QWidget(self.fragments_frame)
        self.widget_111.setObjectName(u"widget_111")

        self.gridLayout_2.addWidget(self.widget_111, 10, 7, 1, 1)

        self.widget_138 = QWidget(self.fragments_frame)
        self.widget_138.setObjectName(u"widget_138")

        self.gridLayout_2.addWidget(self.widget_138, 12, 12, 1, 1)

        self.widget_146 = QWidget(self.fragments_frame)
        self.widget_146.setObjectName(u"widget_146")

        self.gridLayout_2.addWidget(self.widget_146, 5, 12, 1, 1)

        self.widget_68 = QWidget(self.fragments_frame)
        self.widget_68.setObjectName(u"widget_68")

        self.gridLayout_2.addWidget(self.widget_68, 6, 5, 1, 1)

        self.lineEdit_3 = QLineEdit(self.fragments_frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy3)
        self.lineEdit_3.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 0, 1, 1)

        self.widget_28 = QWidget(self.fragments_frame)
        self.widget_28.setObjectName(u"widget_28")

        self.gridLayout_2.addWidget(self.widget_28, 3, 4, 1, 1)

        self.widget_110 = QWidget(self.fragments_frame)
        self.widget_110.setObjectName(u"widget_110")

        self.gridLayout_2.addWidget(self.widget_110, 2, 4, 1, 1)

        self.widget_49 = QWidget(self.fragments_frame)
        self.widget_49.setObjectName(u"widget_49")

        self.gridLayout_2.addWidget(self.widget_49, 7, 12, 1, 1)

        self.widget_109 = QWidget(self.fragments_frame)
        self.widget_109.setObjectName(u"widget_109")

        self.gridLayout_2.addWidget(self.widget_109, 2, 10, 1, 1)

        self.widget_62 = QWidget(self.fragments_frame)
        self.widget_62.setObjectName(u"widget_62")

        self.gridLayout_2.addWidget(self.widget_62, 7, 10, 1, 1)

        self.widget_72 = QWidget(self.fragments_frame)
        self.widget_72.setObjectName(u"widget_72")

        self.gridLayout_2.addWidget(self.widget_72, 6, 9, 1, 1)

        self.widget_106 = QWidget(self.fragments_frame)
        self.widget_106.setObjectName(u"widget_106")

        self.gridLayout_2.addWidget(self.widget_106, 10, 5, 1, 1)

        self.widget_118 = QWidget(self.fragments_frame)
        self.widget_118.setObjectName(u"widget_118")

        self.gridLayout_2.addWidget(self.widget_118, 11, 4, 1, 1)

        self.widget_127 = QWidget(self.fragments_frame)
        self.widget_127.setObjectName(u"widget_127")

        self.gridLayout_2.addWidget(self.widget_127, 10, 3, 1, 1)

        self.widget_51 = QWidget(self.fragments_frame)
        self.widget_51.setObjectName(u"widget_51")

        self.gridLayout_2.addWidget(self.widget_51, 9, 12, 1, 1)

        self.widget_25 = QWidget(self.fragments_frame)
        self.widget_25.setObjectName(u"widget_25")

        self.gridLayout_2.addWidget(self.widget_25, 3, 1, 1, 1)

        self.widget_44 = QWidget(self.fragments_frame)
        self.widget_44.setObjectName(u"widget_44")

        self.gridLayout_2.addWidget(self.widget_44, 4, 8, 1, 1)

        self.widget_58 = QWidget(self.fragments_frame)
        self.widget_58.setObjectName(u"widget_58")

        self.gridLayout_2.addWidget(self.widget_58, 7, 6, 1, 1)

        self.widget_18 = QWidget(self.fragments_frame)
        self.widget_18.setObjectName(u"widget_18")

        self.gridLayout_2.addWidget(self.widget_18, 12, 1, 1, 1)

        self.lineEdit_16 = QLineEdit(self.fragments_frame)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        sizePolicy3.setHeightForWidth(self.lineEdit_16.sizePolicy().hasHeightForWidth())
        self.lineEdit_16.setSizePolicy(sizePolicy3)
        self.lineEdit_16.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_16, 0, 3, 1, 1)

        self.widget_77 = QWidget(self.fragments_frame)
        self.widget_77.setObjectName(u"widget_77")

        self.gridLayout_2.addWidget(self.widget_77, 5, 2, 1, 1)

        self.widget_7 = QWidget(self.fragments_frame)
        self.widget_7.setObjectName(u"widget_7")

        self.gridLayout_2.addWidget(self.widget_7, 1, 6, 1, 1)

        self.widget_103 = QWidget(self.fragments_frame)
        self.widget_103.setObjectName(u"widget_103")

        self.gridLayout_2.addWidget(self.widget_103, 12, 11, 1, 1)

        self.widget_73 = QWidget(self.fragments_frame)
        self.widget_73.setObjectName(u"widget_73")

        self.gridLayout_2.addWidget(self.widget_73, 6, 10, 1, 1)

        self.widget_64 = QWidget(self.fragments_frame)
        self.widget_64.setObjectName(u"widget_64")

        self.gridLayout_2.addWidget(self.widget_64, 6, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.fragments_frame)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy3.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy3)
        self.lineEdit_10.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_10, 9, 0, 1, 1)

        self.widget_71 = QWidget(self.fragments_frame)
        self.widget_71.setObjectName(u"widget_71")

        self.gridLayout_2.addWidget(self.widget_71, 6, 8, 1, 1)

        self.widget_112 = QWidget(self.fragments_frame)
        self.widget_112.setObjectName(u"widget_112")

        self.gridLayout_2.addWidget(self.widget_112, 12, 4, 1, 1)

        self.widget_11 = QWidget(self.fragments_frame)
        self.widget_11.setObjectName(u"widget_11")

        self.gridLayout_2.addWidget(self.widget_11, 1, 10, 1, 1)

        self.widget_114 = QWidget(self.fragments_frame)
        self.widget_114.setObjectName(u"widget_114")

        self.gridLayout_2.addWidget(self.widget_114, 10, 4, 1, 1)

        self.widget_119 = QWidget(self.fragments_frame)
        self.widget_119.setObjectName(u"widget_119")

        self.gridLayout_2.addWidget(self.widget_119, 11, 6, 1, 1)

        self.widget_4 = QWidget(self.fragments_frame)
        self.widget_4.setObjectName(u"widget_4")

        self.gridLayout_2.addWidget(self.widget_4, 1, 3, 1, 1)

        self.widget_115 = QWidget(self.fragments_frame)
        self.widget_115.setObjectName(u"widget_115")

        self.gridLayout_2.addWidget(self.widget_115, 11, 11, 1, 1)

        self.widget_135 = QWidget(self.fragments_frame)
        self.widget_135.setObjectName(u"widget_135")

        self.gridLayout_2.addWidget(self.widget_135, 10, 2, 1, 1)

        self.widget_91 = QWidget(self.fragments_frame)
        self.widget_91.setObjectName(u"widget_91")

        self.gridLayout_2.addWidget(self.widget_91, 9, 2, 1, 1)

        self.widget_116 = QWidget(self.fragments_frame)
        self.widget_116.setObjectName(u"widget_116")

        self.gridLayout_2.addWidget(self.widget_116, 12, 8, 1, 1)

        self.widget_36 = QWidget(self.fragments_frame)
        self.widget_36.setObjectName(u"widget_36")

        self.gridLayout_2.addWidget(self.widget_36, 3, 12, 1, 1)

        self.widget_95 = QWidget(self.fragments_frame)
        self.widget_95.setObjectName(u"widget_95")

        self.gridLayout_2.addWidget(self.widget_95, 8, 6, 1, 1)

        self.widget_90 = QWidget(self.fragments_frame)
        self.widget_90.setObjectName(u"widget_90")

        self.gridLayout_2.addWidget(self.widget_90, 8, 8, 1, 1)

        self.widget_20 = QWidget(self.fragments_frame)
        self.widget_20.setObjectName(u"widget_20")

        self.gridLayout_2.addWidget(self.widget_20, 10, 1, 1, 1)

        self.widget_145 = QWidget(self.fragments_frame)
        self.widget_145.setObjectName(u"widget_145")

        self.gridLayout_2.addWidget(self.widget_145, 5, 11, 1, 1)

        self.widget_5 = QWidget(self.fragments_frame)
        self.widget_5.setObjectName(u"widget_5")

        self.gridLayout_2.addWidget(self.widget_5, 1, 4, 1, 1)

        self.widget_76 = QWidget(self.fragments_frame)
        self.widget_76.setObjectName(u"widget_76")

        self.gridLayout_2.addWidget(self.widget_76, 5, 1, 1, 1)

        self.widget_19 = QWidget(self.fragments_frame)
        self.widget_19.setObjectName(u"widget_19")

        self.gridLayout_2.addWidget(self.widget_19, 11, 1, 1, 1)

        self.widget_147 = QWidget(self.fragments_frame)
        self.widget_147.setObjectName(u"widget_147")

        self.gridLayout_2.addWidget(self.widget_147, 2, 12, 1, 1)

        self.widget_142 = QWidget(self.fragments_frame)
        self.widget_142.setObjectName(u"widget_142")

        self.gridLayout_2.addWidget(self.widget_142, 5, 8, 1, 1)

        self.lineEdit_5 = QLineEdit(self.fragments_frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy3.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy3)
        self.lineEdit_5.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_5, 4, 0, 1, 1)

        self.widget_22 = QWidget(self.fragments_frame)
        self.widget_22.setObjectName(u"widget_22")

        self.gridLayout_2.addWidget(self.widget_22, 8, 1, 1, 1)

        self.lineEdit_15 = QLineEdit(self.fragments_frame)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        sizePolicy3.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy3)
        self.lineEdit_15.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_15, 0, 2, 1, 1)

        self.widget_143 = QWidget(self.fragments_frame)
        self.widget_143.setObjectName(u"widget_143")

        self.gridLayout_2.addWidget(self.widget_143, 5, 9, 1, 1)

        self.lineEdit_2 = QLineEdit(self.fragments_frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy3.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy3)
        self.lineEdit_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 0, 1, 1)

        self.widget_125 = QWidget(self.fragments_frame)
        self.widget_125.setObjectName(u"widget_125")

        self.gridLayout_2.addWidget(self.widget_125, 10, 9, 1, 1)

        self.widget_40 = QWidget(self.fragments_frame)
        self.widget_40.setObjectName(u"widget_40")

        self.gridLayout_2.addWidget(self.widget_40, 4, 4, 1, 1)

        self.widget_92 = QWidget(self.fragments_frame)
        self.widget_92.setObjectName(u"widget_92")

        self.gridLayout_2.addWidget(self.widget_92, 8, 9, 1, 1)

        self.lineEdit_19 = QLineEdit(self.fragments_frame)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        sizePolicy3.setHeightForWidth(self.lineEdit_19.sizePolicy().hasHeightForWidth())
        self.lineEdit_19.setSizePolicy(sizePolicy3)
        self.lineEdit_19.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_19, 0, 6, 1, 1)

        self.widget_27 = QWidget(self.fragments_frame)
        self.widget_27.setObjectName(u"widget_27")

        self.gridLayout_2.addWidget(self.widget_27, 3, 3, 1, 1)

        self.widget_84 = QWidget(self.fragments_frame)
        self.widget_84.setObjectName(u"widget_84")

        self.gridLayout_2.addWidget(self.widget_84, 8, 7, 1, 1)

        self.widget_80 = QWidget(self.fragments_frame)
        self.widget_80.setObjectName(u"widget_80")

        self.gridLayout_2.addWidget(self.widget_80, 9, 5, 1, 1)

        self.widget_57 = QWidget(self.fragments_frame)
        self.widget_57.setObjectName(u"widget_57")

        self.gridLayout_2.addWidget(self.widget_57, 7, 5, 1, 1)

        self.widget_136 = QWidget(self.fragments_frame)
        self.widget_136.setObjectName(u"widget_136")

        self.gridLayout_2.addWidget(self.widget_136, 12, 9, 1, 1)

        self.widget_74 = QWidget(self.fragments_frame)
        self.widget_74.setObjectName(u"widget_74")

        self.gridLayout_2.addWidget(self.widget_74, 6, 11, 1, 1)

        self.widget_87 = QWidget(self.fragments_frame)
        self.widget_87.setObjectName(u"widget_87")

        self.gridLayout_2.addWidget(self.widget_87, 9, 4, 1, 1)

        self.lineEdit_12 = QLineEdit(self.fragments_frame)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy3.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy3)
        self.lineEdit_12.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_12, 11, 0, 1, 1)

        self.widget_2 = QWidget(self.fragments_frame)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout_2.addWidget(self.widget_2, 1, 1, 1, 1)

        self.lineEdit_17 = QLineEdit(self.fragments_frame)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        sizePolicy3.setHeightForWidth(self.lineEdit_17.sizePolicy().hasHeightForWidth())
        self.lineEdit_17.setSizePolicy(sizePolicy3)
        self.lineEdit_17.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_17, 0, 4, 1, 1)

        self.widget_88 = QWidget(self.fragments_frame)
        self.widget_88.setObjectName(u"widget_88")

        self.gridLayout_2.addWidget(self.widget_88, 9, 6, 1, 1)

        self.widget_101 = QWidget(self.fragments_frame)
        self.widget_101.setObjectName(u"widget_101")

        self.gridLayout_2.addWidget(self.widget_101, 11, 5, 1, 1)

        self.widget_48 = QWidget(self.fragments_frame)
        self.widget_48.setObjectName(u"widget_48")

        self.gridLayout_2.addWidget(self.widget_48, 4, 12, 1, 1)

        self.widget_100 = QWidget(self.fragments_frame)
        self.widget_100.setObjectName(u"widget_100")

        self.gridLayout_2.addWidget(self.widget_100, 11, 10, 1, 1)

        self.widget_140 = QWidget(self.fragments_frame)
        self.widget_140.setObjectName(u"widget_140")

        self.gridLayout_2.addWidget(self.widget_140, 5, 6, 1, 1)

        self.widget_137 = QWidget(self.fragments_frame)
        self.widget_137.setObjectName(u"widget_137")

        self.gridLayout_2.addWidget(self.widget_137, 2, 8, 1, 1)

        self.widget_23 = QWidget(self.fragments_frame)
        self.widget_23.setObjectName(u"widget_23")

        self.gridLayout_2.addWidget(self.widget_23, 7, 1, 1, 1)

        self.widget_104 = QWidget(self.fragments_frame)
        self.widget_104.setObjectName(u"widget_104")

        self.gridLayout_2.addWidget(self.widget_104, 2, 7, 1, 1)

        self.widget_17 = QWidget(self.fragments_frame)
        self.widget_17.setObjectName(u"widget_17")

        self.gridLayout_2.addWidget(self.widget_17, 2, 2, 1, 1)

        self.widget_61 = QWidget(self.fragments_frame)
        self.widget_61.setObjectName(u"widget_61")

        self.gridLayout_2.addWidget(self.widget_61, 7, 9, 1, 1)

        self.widget_96 = QWidget(self.fragments_frame)
        self.widget_96.setObjectName(u"widget_96")

        self.gridLayout_2.addWidget(self.widget_96, 8, 11, 1, 1)

        self.lineEdit_4 = QLineEdit(self.fragments_frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy3.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy3)
        self.lineEdit_4.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.fragments_frame)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy3.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy3)
        self.lineEdit_13.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_13, 12, 0, 1, 1)

        self.widget_99 = QWidget(self.fragments_frame)
        self.widget_99.setObjectName(u"widget_99")

        self.gridLayout_2.addWidget(self.widget_99, 12, 2, 1, 1)

        self.widget_45 = QWidget(self.fragments_frame)
        self.widget_45.setObjectName(u"widget_45")

        self.gridLayout_2.addWidget(self.widget_45, 4, 9, 1, 1)

        self.widget_47 = QWidget(self.fragments_frame)
        self.widget_47.setObjectName(u"widget_47")

        self.gridLayout_2.addWidget(self.widget_47, 4, 11, 1, 1)

        self.widget_132 = QWidget(self.fragments_frame)
        self.widget_132.setObjectName(u"widget_132")

        self.gridLayout_2.addWidget(self.widget_132, 10, 11, 1, 1)

        self.widget_70 = QWidget(self.fragments_frame)
        self.widget_70.setObjectName(u"widget_70")
        self.widget_70.setEnabled(True)

        self.gridLayout_2.addWidget(self.widget_70, 6, 7, 1, 1)

        self.widget_24 = QWidget(self.fragments_frame)
        self.widget_24.setObjectName(u"widget_24")

        self.gridLayout_2.addWidget(self.widget_24, 4, 1, 1, 1)

        self.widget_117 = QWidget(self.fragments_frame)
        self.widget_117.setObjectName(u"widget_117")

        self.gridLayout_2.addWidget(self.widget_117, 12, 3, 1, 1)

        self.widget_35 = QWidget(self.fragments_frame)
        self.widget_35.setObjectName(u"widget_35")

        self.gridLayout_2.addWidget(self.widget_35, 3, 11, 1, 1)

        self.widget_59 = QWidget(self.fragments_frame)
        self.widget_59.setObjectName(u"widget_59")

        self.gridLayout_2.addWidget(self.widget_59, 7, 7, 1, 1)

        self.widget_113 = QWidget(self.fragments_frame)
        self.widget_113.setObjectName(u"widget_113")

        self.gridLayout_2.addWidget(self.widget_113, 11, 3, 1, 1)

        self.widget_134 = QWidget(self.fragments_frame)
        self.widget_134.setObjectName(u"widget_134")

        self.gridLayout_2.addWidget(self.widget_134, 12, 6, 1, 1)

        self.widget_89 = QWidget(self.fragments_frame)
        self.widget_89.setObjectName(u"widget_89")

        self.gridLayout_2.addWidget(self.widget_89, 9, 7, 1, 1)

        self.widget_26 = QWidget(self.fragments_frame)
        self.widget_26.setObjectName(u"widget_26")

        self.gridLayout_2.addWidget(self.widget_26, 3, 2, 1, 1)

        self.widget_13 = QWidget(self.fragments_frame)
        self.widget_13.setObjectName(u"widget_13")

        self.gridLayout_2.addWidget(self.widget_13, 1, 12, 1, 1)

        self.widget_54 = QWidget(self.fragments_frame)
        self.widget_54.setObjectName(u"widget_54")

        self.gridLayout_2.addWidget(self.widget_54, 7, 2, 1, 1)

        self.widget_124 = QWidget(self.fragments_frame)
        self.widget_124.setObjectName(u"widget_124")

        self.gridLayout_2.addWidget(self.widget_124, 11, 2, 1, 1)

        self.widget_120 = QWidget(self.fragments_frame)
        self.widget_120.setObjectName(u"widget_120")

        self.gridLayout_2.addWidget(self.widget_120, 11, 7, 1, 1)

        self.widget_34 = QWidget(self.fragments_frame)
        self.widget_34.setObjectName(u"widget_34")

        self.gridLayout_2.addWidget(self.widget_34, 3, 10, 1, 1)

        self.widget_81 = QWidget(self.fragments_frame)
        self.widget_81.setObjectName(u"widget_81")

        self.gridLayout_2.addWidget(self.widget_81, 9, 8, 1, 1)

        self.widget_131 = QWidget(self.fragments_frame)
        self.widget_131.setObjectName(u"widget_131")

        self.gridLayout_2.addWidget(self.widget_131, 2, 6, 1, 1)

        self.widget_108 = QWidget(self.fragments_frame)
        self.widget_108.setObjectName(u"widget_108")

        self.gridLayout_2.addWidget(self.widget_108, 11, 9, 1, 1)

        self.widget_129 = QWidget(self.fragments_frame)
        self.widget_129.setObjectName(u"widget_129")

        self.gridLayout_2.addWidget(self.widget_129, 5, 4, 1, 1)

        self.widget_50 = QWidget(self.fragments_frame)
        self.widget_50.setObjectName(u"widget_50")

        self.gridLayout_2.addWidget(self.widget_50, 8, 12, 1, 1)

        self.lineEdit_14 = QLineEdit(self.fragments_frame)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        sizePolicy3.setHeightForWidth(self.lineEdit_14.sizePolicy().hasHeightForWidth())
        self.lineEdit_14.setSizePolicy(sizePolicy3)
        self.lineEdit_14.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_14, 0, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.fragments_frame)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy3.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy3)
        self.lineEdit_8.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_8, 7, 0, 1, 1)

        self.widget_21 = QWidget(self.fragments_frame)
        self.widget_21.setObjectName(u"widget_21")

        self.gridLayout_2.addWidget(self.widget_21, 9, 1, 1, 1)

        self.widget_33 = QWidget(self.fragments_frame)
        self.widget_33.setObjectName(u"widget_33")

        self.gridLayout_2.addWidget(self.widget_33, 3, 9, 1, 1)

        self.widget_78 = QWidget(self.fragments_frame)
        self.widget_78.setObjectName(u"widget_78")

        self.gridLayout_2.addWidget(self.widget_78, 9, 11, 1, 1)

        self.widget_130 = QWidget(self.fragments_frame)
        self.widget_130.setObjectName(u"widget_130")

        self.gridLayout_2.addWidget(self.widget_130, 5, 3, 1, 1)

        self.widget_8 = QWidget(self.fragments_frame)
        self.widget_8.setObjectName(u"widget_8")

        self.gridLayout_2.addWidget(self.widget_8, 1, 7, 1, 1)

        self.widget_63 = QWidget(self.fragments_frame)
        self.widget_63.setObjectName(u"widget_63")

        self.gridLayout_2.addWidget(self.widget_63, 7, 11, 1, 1)

        self.widget_83 = QWidget(self.fragments_frame)
        self.widget_83.setObjectName(u"widget_83")

        self.gridLayout_2.addWidget(self.widget_83, 9, 9, 1, 1)

        self.widget_148 = QWidget(self.fragments_frame)
        self.widget_148.setObjectName(u"widget_148")

        self.gridLayout_2.addWidget(self.widget_148, 2, 11, 1, 1)

        self.widget_56 = QWidget(self.fragments_frame)
        self.widget_56.setObjectName(u"widget_56")

        self.gridLayout_2.addWidget(self.widget_56, 7, 4, 1, 1)

        self.widget_41 = QWidget(self.fragments_frame)
        self.widget_41.setObjectName(u"widget_41")

        self.gridLayout_2.addWidget(self.widget_41, 4, 5, 1, 1)

        self.widget_69 = QWidget(self.fragments_frame)
        self.widget_69.setObjectName(u"widget_69")

        self.gridLayout_2.addWidget(self.widget_69, 6, 6, 1, 1)

        self.widget_9 = QWidget(self.fragments_frame)
        self.widget_9.setObjectName(u"widget_9")

        self.gridLayout_2.addWidget(self.widget_9, 1, 8, 1, 1)

        self.widget_133 = QWidget(self.fragments_frame)
        self.widget_133.setObjectName(u"widget_133")

        self.gridLayout_2.addWidget(self.widget_133, 12, 7, 1, 1)

        self.widget_12 = QWidget(self.fragments_frame)
        self.widget_12.setObjectName(u"widget_12")

        self.gridLayout_2.addWidget(self.widget_12, 1, 11, 1, 1)

        self.widget_55 = QWidget(self.fragments_frame)
        self.widget_55.setObjectName(u"widget_55")

        self.gridLayout_2.addWidget(self.widget_55, 7, 3, 1, 1)

        self.widget_30 = QWidget(self.fragments_frame)
        self.widget_30.setObjectName(u"widget_30")

        self.gridLayout_2.addWidget(self.widget_30, 3, 6, 1, 1)

        self.widget_122 = QWidget(self.fragments_frame)
        self.widget_122.setObjectName(u"widget_122")

        self.gridLayout_2.addWidget(self.widget_122, 10, 8, 1, 1)

        self.widget_86 = QWidget(self.fragments_frame)
        self.widget_86.setObjectName(u"widget_86")

        self.gridLayout_2.addWidget(self.widget_86, 8, 4, 1, 1)

        self.widget_43 = QWidget(self.fragments_frame)
        self.widget_43.setObjectName(u"widget_43")

        self.gridLayout_2.addWidget(self.widget_43, 4, 7, 1, 1)

        self.widget_123 = QWidget(self.fragments_frame)
        self.widget_123.setObjectName(u"widget_123")

        self.gridLayout_2.addWidget(self.widget_123, 2, 9, 1, 1)

        self.widget_46 = QWidget(self.fragments_frame)
        self.widget_46.setObjectName(u"widget_46")

        self.gridLayout_2.addWidget(self.widget_46, 4, 10, 1, 1)

        self.lineEdit_6 = QLineEdit(self.fragments_frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy3.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy3)
        self.lineEdit_6.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_6, 5, 0, 1, 1)

        self.widget_60 = QWidget(self.fragments_frame)
        self.widget_60.setObjectName(u"widget_60")

        self.gridLayout_2.addWidget(self.widget_60, 7, 8, 1, 1)

        self.widget_93 = QWidget(self.fragments_frame)
        self.widget_93.setObjectName(u"widget_93")

        self.gridLayout_2.addWidget(self.widget_93, 8, 10, 1, 1)

        self.widget_10 = QWidget(self.fragments_frame)
        self.widget_10.setObjectName(u"widget_10")

        self.gridLayout_2.addWidget(self.widget_10, 1, 9, 1, 1)

        self.widget_121 = QWidget(self.fragments_frame)
        self.widget_121.setObjectName(u"widget_121")

        self.gridLayout_2.addWidget(self.widget_121, 12, 10, 1, 1)

        self.widget_128 = QWidget(self.fragments_frame)
        self.widget_128.setObjectName(u"widget_128")

        self.gridLayout_2.addWidget(self.widget_128, 10, 6, 1, 1)

        self.widget_94 = QWidget(self.fragments_frame)
        self.widget_94.setObjectName(u"widget_94")

        self.gridLayout_2.addWidget(self.widget_94, 8, 3, 1, 1)

        self.widget_105 = QWidget(self.fragments_frame)
        self.widget_105.setObjectName(u"widget_105")

        self.gridLayout_2.addWidget(self.widget_105, 11, 8, 1, 1)

        self.widget_39 = QWidget(self.fragments_frame)
        self.widget_39.setObjectName(u"widget_39")

        self.gridLayout_2.addWidget(self.widget_39, 4, 3, 1, 1)

        self.widget_97 = QWidget(self.fragments_frame)
        self.widget_97.setObjectName(u"widget_97")

        self.gridLayout_2.addWidget(self.widget_97, 8, 2, 1, 1)

        self.widget_79 = QWidget(self.fragments_frame)
        self.widget_79.setObjectName(u"widget_79")

        self.gridLayout_2.addWidget(self.widget_79, 9, 10, 1, 1)

        self.lineEdit_9 = QLineEdit(self.fragments_frame)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy3.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy3)
        self.lineEdit_9.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_9, 8, 0, 1, 1)

        self.widget_107 = QWidget(self.fragments_frame)
        self.widget_107.setObjectName(u"widget_107")

        self.gridLayout_2.addWidget(self.widget_107, 2, 5, 1, 1)

        self.lineEdit_18 = QLineEdit(self.fragments_frame)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        sizePolicy3.setHeightForWidth(self.lineEdit_18.sizePolicy().hasHeightForWidth())
        self.lineEdit_18.setSizePolicy(sizePolicy3)
        self.lineEdit_18.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_18, 0, 5, 1, 1)

        self.lineEdit_11 = QLineEdit(self.fragments_frame)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy3.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy3)
        self.lineEdit_11.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_11, 10, 0, 1, 1)

        self.widget_53 = QWidget(self.fragments_frame)
        self.widget_53.setObjectName(u"widget_53")

        self.gridLayout_2.addWidget(self.widget_53, 11, 12, 1, 1)

        self.widget_75 = QWidget(self.fragments_frame)
        self.widget_75.setObjectName(u"widget_75")

        self.gridLayout_2.addWidget(self.widget_75, 6, 12, 1, 1)

        self.widget_65 = QWidget(self.fragments_frame)
        self.widget_65.setObjectName(u"widget_65")

        self.gridLayout_2.addWidget(self.widget_65, 6, 2, 1, 1)

        self.lineEdit_7 = QLineEdit(self.fragments_frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy3.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy3)
        self.lineEdit_7.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_7, 6, 0, 1, 1)

        self.widget_98 = QWidget(self.fragments_frame)
        self.widget_98.setObjectName(u"widget_98")

        self.gridLayout_2.addWidget(self.widget_98, 2, 3, 1, 1)

        self.widget_102 = QWidget(self.fragments_frame)
        self.widget_102.setObjectName(u"widget_102")

        self.gridLayout_2.addWidget(self.widget_102, 12, 5, 1, 1)

        self.widget_82 = QWidget(self.fragments_frame)
        self.widget_82.setObjectName(u"widget_82")

        self.gridLayout_2.addWidget(self.widget_82, 8, 5, 1, 1)

        self.widget_29 = QWidget(self.fragments_frame)
        self.widget_29.setObjectName(u"widget_29")

        self.gridLayout_2.addWidget(self.widget_29, 3, 5, 1, 1)

        self.widget_85 = QWidget(self.fragments_frame)
        self.widget_85.setObjectName(u"widget_85")

        self.gridLayout_2.addWidget(self.widget_85, 9, 3, 1, 1)

        self.widget_6 = QWidget(self.fragments_frame)
        self.widget_6.setObjectName(u"widget_6")

        self.gridLayout_2.addWidget(self.widget_6, 1, 5, 1, 1)

        self.widget_32 = QWidget(self.fragments_frame)
        self.widget_32.setObjectName(u"widget_32")

        self.gridLayout_2.addWidget(self.widget_32, 3, 8, 1, 1)

        self.widget_37 = QWidget(self.fragments_frame)
        self.widget_37.setObjectName(u"widget_37")

        self.gridLayout_2.addWidget(self.widget_37, 2, 1, 1, 1)

        self.widget_38 = QWidget(self.fragments_frame)
        self.widget_38.setObjectName(u"widget_38")

        self.gridLayout_2.addWidget(self.widget_38, 4, 2, 1, 1)

        self.lineEdit_20 = QLineEdit(self.fragments_frame)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        sizePolicy3.setHeightForWidth(self.lineEdit_20.sizePolicy().hasHeightForWidth())
        self.lineEdit_20.setSizePolicy(sizePolicy3)
        self.lineEdit_20.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_20, 0, 7, 1, 1)

        self.widget_3 = QWidget(self.fragments_frame)
        self.widget_3.setObjectName(u"widget_3")

        self.gridLayout_2.addWidget(self.widget_3, 1, 2, 1, 1)

        self.widget_42 = QWidget(self.fragments_frame)
        self.widget_42.setObjectName(u"widget_42")

        self.gridLayout_2.addWidget(self.widget_42, 4, 6, 1, 1)

        self.widget_141 = QWidget(self.fragments_frame)
        self.widget_141.setObjectName(u"widget_141")

        self.gridLayout_2.addWidget(self.widget_141, 5, 7, 1, 1)

        self.widget_52 = QWidget(self.fragments_frame)
        self.widget_52.setObjectName(u"widget_52")

        self.gridLayout_2.addWidget(self.widget_52, 10, 12, 1, 1)

        self.widget_31 = QWidget(self.fragments_frame)
        self.widget_31.setObjectName(u"widget_31")

        self.gridLayout_2.addWidget(self.widget_31, 3, 7, 1, 1)

        self.widget_67 = QWidget(self.fragments_frame)
        self.widget_67.setObjectName(u"widget_67")

        self.gridLayout_2.addWidget(self.widget_67, 6, 4, 1, 1)

        self.widget_144 = QWidget(self.fragments_frame)
        self.widget_144.setObjectName(u"widget_144")

        self.gridLayout_2.addWidget(self.widget_144, 5, 10, 1, 1)

        self.lineEdit_40 = QLineEdit(self.fragments_frame)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        sizePolicy3.setHeightForWidth(self.lineEdit_40.sizePolicy().hasHeightForWidth())
        self.lineEdit_40.setSizePolicy(sizePolicy3)
        self.lineEdit_40.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_40, 0, 8, 1, 1)

        self.lineEdit_41 = QLineEdit(self.fragments_frame)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        sizePolicy3.setHeightForWidth(self.lineEdit_41.sizePolicy().hasHeightForWidth())
        self.lineEdit_41.setSizePolicy(sizePolicy3)
        self.lineEdit_41.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_41, 0, 9, 1, 1)

        self.lineEdit_42 = QLineEdit(self.fragments_frame)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        sizePolicy3.setHeightForWidth(self.lineEdit_42.sizePolicy().hasHeightForWidth())
        self.lineEdit_42.setSizePolicy(sizePolicy3)
        self.lineEdit_42.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_42, 0, 10, 1, 1)

        self.lineEdit_43 = QLineEdit(self.fragments_frame)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        sizePolicy3.setHeightForWidth(self.lineEdit_43.sizePolicy().hasHeightForWidth())
        self.lineEdit_43.setSizePolicy(sizePolicy3)
        self.lineEdit_43.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_43, 0, 11, 1, 1)

        self.lineEdit_44 = QLineEdit(self.fragments_frame)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        sizePolicy3.setHeightForWidth(self.lineEdit_44.sizePolicy().hasHeightForWidth())
        self.lineEdit_44.setSizePolicy(sizePolicy3)
        self.lineEdit_44.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_44, 0, 12, 1, 1)


        self.gridLayout.addWidget(self.fragments_frame, 0, 1, 2, 1)

        self.buttonBox = QDialogButtonBox(self.background)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy4)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.background, 0, 0, 1, 1)


        self.retranslateUi(door_edit_dialog)
        self.buttonBox.accepted.connect(door_edit_dialog.accept)
        self.buttonBox.rejected.connect(door_edit_dialog.reject)

        QMetaObject.connectSlotsByName(door_edit_dialog)
    # setupUi

    def retranslateUi(self, door_edit_dialog):
        door_edit_dialog.setWindowTitle(QCoreApplication.translate("door_edit_dialog", u"\u0414\u0432\u0435\u0440\u044c", None))
        self.label.setText(QCoreApplication.translate("door_edit_dialog", u"\u041a\u043e\u043b-\u0432\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432", None))
        self.label_2.setText(QCoreApplication.translate("door_edit_dialog", u"\u041a\u043e\u043b-\u0432\u043e \u0441\u0442\u0440\u043e\u043a", None))
        self.label_3.setText(QCoreApplication.translate("door_edit_dialog", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.i_width.setPlaceholderText(QCoreApplication.translate("door_edit_dialog", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("door_edit_dialog", u"\u0413\u043b\u0430\u0432\u043d\u044b\u0439 \u0440\u0438\u0433\u0435\u043b\u044c", None))
        self.ch_h_main_rigel.setText(QCoreApplication.translate("door_edit_dialog", u"\u0413\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u044b\u0439", None))
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_16.setPlaceholderText("")
        self.lineEdit_10.setPlaceholderText("")
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_15.setPlaceholderText("")
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_19.setPlaceholderText("")
        self.lineEdit_12.setPlaceholderText("")
        self.lineEdit_17.setPlaceholderText("")
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_13.setPlaceholderText("")
        self.lineEdit_14.setPlaceholderText("")
        self.lineEdit_8.setPlaceholderText("")
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_9.setPlaceholderText("")
        self.lineEdit_18.setPlaceholderText("")
        self.lineEdit_11.setPlaceholderText("")
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_20.setPlaceholderText("")
        self.lineEdit_40.setPlaceholderText("")
        self.lineEdit_41.setPlaceholderText("")
        self.lineEdit_42.setPlaceholderText("")
        self.lineEdit_43.setPlaceholderText("")
        self.lineEdit_44.setPlaceholderText("")
    # retranslateUi

