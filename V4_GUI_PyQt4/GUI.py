# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Feutrage(object):
    def setupUi(self, Feutrage):
        Feutrage.setObjectName(_fromUtf8("Feutrage"))
        Feutrage.resize(736, 507)
        self.gridLayout = QtGui.QGridLayout(Feutrage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pb_refreshPorts = QtGui.QPushButton(Feutrage)
        self.pb_refreshPorts.setObjectName(_fromUtf8("pb_refreshPorts"))
        self.gridLayout.addWidget(self.pb_refreshPorts, 2, 0, 1, 1)
        self.pb_openPort = QtGui.QPushButton(Feutrage)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.pb_openPort.setPalette(palette)
        self.pb_openPort.setAutoDefault(False)
        self.pb_openPort.setDefault(False)
        self.pb_openPort.setFlat(False)
        self.pb_openPort.setObjectName(_fromUtf8("pb_openPort"))
        self.gridLayout.addWidget(self.pb_openPort, 2, 3, 1, 1)
        self.cb_ports = QtGui.QComboBox(Feutrage)
        self.cb_ports.setObjectName(_fromUtf8("cb_ports"))
        self.gridLayout.addWidget(self.cb_ports, 2, 2, 1, 1)
        self.lbl_status = QtGui.QLabel(Feutrage)
        self.lbl_status.setObjectName(_fromUtf8("lbl_status"))
        self.gridLayout.addWidget(self.lbl_status, 2, 4, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Feutrage)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.lbl_title = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title.sizePolicy().hasHeightForWidth())
        self.lbl_title.setSizePolicy(sizePolicy)
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.gridLayout_5.addWidget(self.lbl_title, 1, 0, 1, 1)
        self.lbl_purpose = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_purpose.sizePolicy().hasHeightForWidth())
        self.lbl_purpose.setSizePolicy(sizePolicy)
        self.lbl_purpose.setObjectName(_fromUtf8("lbl_purpose"))
        self.gridLayout_5.addWidget(self.lbl_purpose, 2, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 712, 812))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_6 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.lbl_image = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_image.setText(_fromUtf8(""))
        self.lbl_image.setPixmap(QtGui.QPixmap(_fromUtf8("img/cycle.png")))
        self.lbl_image.setObjectName(_fromUtf8("lbl_image"))
        self.gridLayout_6.addWidget(self.lbl_image, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lbl_y = QtGui.QLabel(self.tab_2)
        self.lbl_y.setObjectName(_fromUtf8("lbl_y"))
        self.gridLayout_4.addWidget(self.lbl_y, 0, 0, 1, 1)
        self.sb_y = QtGui.QSpinBox(self.tab_2)
        self.sb_y.setMaximum(300)
        self.sb_y.setProperty("value", 150)
        self.sb_y.setObjectName(_fromUtf8("sb_y"))
        self.gridLayout_4.addWidget(self.sb_y, 0, 1, 1, 1)
        self.lbl_x = QtGui.QLabel(self.tab_2)
        self.lbl_x.setObjectName(_fromUtf8("lbl_x"))
        self.gridLayout_4.addWidget(self.lbl_x, 1, 0, 1, 1)
        self.sb_x = QtGui.QSpinBox(self.tab_2)
        self.sb_x.setMinimum(0)
        self.sb_x.setMaximum(300)
        self.sb_x.setProperty("value", 150)
        self.sb_x.setObjectName(_fromUtf8("sb_x"))
        self.gridLayout_4.addWidget(self.sb_x, 1, 1, 1, 1)
        self.lbl_step = QtGui.QLabel(self.tab_2)
        self.lbl_step.setObjectName(_fromUtf8("lbl_step"))
        self.gridLayout_4.addWidget(self.lbl_step, 2, 0, 1, 1)
        self.sb_step = QtGui.QSpinBox(self.tab_2)
        self.sb_step.setProperty("value", 8)
        self.sb_step.setObjectName(_fromUtf8("sb_step"))
        self.gridLayout_4.addWidget(self.sb_step, 2, 1, 1, 1)
        self.lbl_move_z = QtGui.QLabel(self.tab_2)
        self.lbl_move_z.setObjectName(_fromUtf8("lbl_move_z"))
        self.gridLayout_4.addWidget(self.lbl_move_z, 3, 0, 1, 1)
        self.sb_axis_z = QtGui.QSpinBox(self.tab_2)
        self.sb_axis_z.setProperty("value", 20)
        self.sb_axis_z.setObjectName(_fromUtf8("sb_axis_z"))
        self.gridLayout_4.addWidget(self.sb_axis_z, 3, 1, 1, 1)
        self.lbl_speed_xy = QtGui.QLabel(self.tab_2)
        self.lbl_speed_xy.setObjectName(_fromUtf8("lbl_speed_xy"))
        self.gridLayout_4.addWidget(self.lbl_speed_xy, 5, 0, 1, 1)
        self.sb_speed = QtGui.QSpinBox(self.tab_2)
        self.sb_speed.setMaximum(8)
        self.sb_speed.setProperty("value", 4)
        self.sb_speed.setObjectName(_fromUtf8("sb_speed"))
        self.gridLayout_4.addWidget(self.sb_speed, 5, 1, 1, 1)
        self.lbl_actions = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_actions.sizePolicy().hasHeightForWidth())
        self.lbl_actions.setSizePolicy(sizePolicy)
        self.lbl_actions.setObjectName(_fromUtf8("lbl_actions"))
        self.gridLayout_4.addWidget(self.lbl_actions, 4, 0, 1, 1)
        self.sb_passages = QtGui.QSpinBox(self.tab_2)
        self.sb_passages.setMaximum(20)
        self.sb_passages.setProperty("value", 2)
        self.sb_passages.setObjectName(_fromUtf8("sb_passages"))
        self.gridLayout_4.addWidget(self.sb_passages, 4, 1, 1, 1)
        self.lbl_speed_z = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_speed_z.sizePolicy().hasHeightForWidth())
        self.lbl_speed_z.setSizePolicy(sizePolicy)
        self.lbl_speed_z.setObjectName(_fromUtf8("lbl_speed_z"))
        self.gridLayout_4.addWidget(self.lbl_speed_z, 6, 0, 1, 1)
        self.sb_speed_z = QtGui.QSpinBox(self.tab_2)
        self.sb_speed_z.setMaximum(8)
        self.sb_speed_z.setProperty("value", 6)
        self.sb_speed_z.setObjectName(_fromUtf8("sb_speed_z"))
        self.gridLayout_4.addWidget(self.sb_speed_z, 6, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 7, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pte_displayGCode = QtGui.QPlainTextEdit(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pte_displayGCode.sizePolicy().hasHeightForWidth())
        self.pte_displayGCode.setSizePolicy(sizePolicy)
        self.pte_displayGCode.setUndoRedoEnabled(False)
        self.pte_displayGCode.setObjectName(_fromUtf8("pte_displayGCode"))
        self.gridLayout_3.addWidget(self.pte_displayGCode, 1, 0, 4, 1)
        self.pb_stop = QtGui.QPushButton(self.tab_4)
        self.pb_stop.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pb_stop.setPalette(palette)
        self.pb_stop.setObjectName(_fromUtf8("pb_stop"))
        self.gridLayout_3.addWidget(self.pb_stop, 4, 1, 1, 1)
        self.label = QtGui.QLabel(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 5, 0, 1, 1)
        self.pb_start = QtGui.QPushButton(self.tab_4)
        self.pb_start.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pb_start.setPalette(palette)
        self.pb_start.setObjectName(_fromUtf8("pb_start"))
        self.gridLayout_3.addWidget(self.pb_start, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 5)
        self.cb_bauds = QtGui.QComboBox(Feutrage)
        self.cb_bauds.setObjectName(_fromUtf8("cb_bauds"))
        self.cb_bauds.addItem(_fromUtf8(""))
        self.cb_bauds.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cb_bauds, 2, 1, 1, 1)

        self.retranslateUi(Feutrage)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Feutrage)

    def retranslateUi(self, Feutrage):
        Feutrage.setWindowTitle(_translate("Feutrage", "Form", None))
        self.pb_refreshPorts.setText(_translate("Feutrage", "Mettre à jour les ports", None))
        self.pb_openPort.setText(_translate("Feutrage", "Connection machine", None))
        self.lbl_status.setText(_translate("Feutrage", "Non connecte", None))
        self.lbl_title.setText(_translate("Feutrage", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Feutrage de laine</span></p></body></html>", None))
        self.lbl_purpose.setText(_translate("Feutrage", "<html><head/><body><p><span style=\" font-size:12pt;\">Ce logiciel permet de lancer un cycle de feutrage.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Feutrage", "Presentation", None))
        self.lbl_y.setText(_translate("Feutrage", "Longueur du plateau (mm)", None))
        self.lbl_x.setText(_translate("Feutrage", "Largeur du plateau (mm)", None))
        self.lbl_step.setText(_translate("Feutrage", "Déplacement du porte-aiguilles (mm)", None))
        self.lbl_move_z.setText(_translate("Feutrage", "Déplacement de l\'axe Z (mm)", None))
        self.lbl_speed_xy.setText(_translate("Feutrage", "Vitesse sur l\'axe X et Y", None))
        self.lbl_actions.setText(_translate("Feutrage", "Nombre d\'actions de l\'outil-aiguilles ", None))
        self.lbl_speed_z.setText(_translate("Feutrage", "Vitesse sur l\'axe Z", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Feutrage", "Paramètres", None))
        self.pb_stop.setText(_translate("Feutrage", "Arreter le cycle", None))
        self.label.setText(_translate("Feutrage", "Visualisation du GCode", None))
        self.pb_start.setText(_translate("Feutrage", "Lancer le cycle", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Feutrage", "Lancement du cycle", None))
        self.cb_bauds.setItemText(0, _translate("Feutrage", "115200", None))
        self.cb_bauds.setItemText(1, _translate("Feutrage", "9600", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Feutrage = QtGui.QWidget()
    ui = Ui_Feutrage()
    ui.setupUi(Feutrage)
    Feutrage.show()
    sys.exit(app.exec_())

