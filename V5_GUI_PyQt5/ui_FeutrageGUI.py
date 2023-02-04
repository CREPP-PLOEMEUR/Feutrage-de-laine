# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FeutrageGUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 740)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_2 = QGridLayout(self.tab_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(self.tab_1)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 712, 812))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u"img/cycle.png"))

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 3, 0, 1, 1)

        self.label_5 = QLabel(self.tab_1)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.tab_1)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_11 = QLabel(self.tab_1)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_8 = QGridLayout(self.tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_8.addWidget(self.label_9, 0, 0, 1, 1)

        self.pte_gcodeReturn = QPlainTextEdit(self.tab)
        self.pte_gcodeReturn.setObjectName(u"pte_gcodeReturn")
        self.pte_gcodeReturn.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.gridLayout_8.addWidget(self.pte_gcodeReturn, 1, 0, 1, 3)

        self.pb_clear = QPushButton(self.tab)
        self.pb_clear.setObjectName(u"pb_clear")

        self.gridLayout_8.addWidget(self.pb_clear, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 8)

        self.pb_progressBar = QProgressBar(self.centralwidget)
        self.pb_progressBar.setObjectName(u"pb_progressBar")
        self.pb_progressBar.setValue(0)

        self.gridLayout.addWidget(self.pb_progressBar, 2, 7, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 6, 1, 1)

        self.pb_openPort = QPushButton(self.centralwidget)
        self.pb_openPort.setObjectName(u"pb_openPort")
        palette = QPalette()
        brush = QBrush(QColor(138, 226, 52, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.pb_openPort.setPalette(palette)

        self.gridLayout.addWidget(self.pb_openPort, 2, 4, 1, 1)

        self.pb_closePort = QPushButton(self.centralwidget)
        self.pb_closePort.setObjectName(u"pb_closePort")
        self.pb_closePort.setEnabled(False)
        palette1 = QPalette()
        brush1 = QBrush(QColor(239, 41, 41, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        self.pb_closePort.setPalette(palette1)

        self.gridLayout.addWidget(self.pb_closePort, 2, 5, 1, 1)

        self.pb_resfreshPorts = QPushButton(self.centralwidget)
        self.pb_resfreshPorts.setObjectName(u"pb_resfreshPorts")

        self.gridLayout.addWidget(self.pb_resfreshPorts, 2, 2, 1, 1)

        self.cb_ports = QComboBox(self.centralwidget)
        self.cb_ports.setObjectName(u"cb_ports")

        self.gridLayout.addWidget(self.cb_ports, 2, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1050, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dw_settings = QDockWidget(MainWindow)
        self.dw_settings.setObjectName(u"dw_settings")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_6 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pb_stop = QPushButton(self.dockWidgetContents)
        self.pb_stop.setObjectName(u"pb_stop")
        self.pb_stop.setEnabled(False)
        palette2 = QPalette()
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush3 = QBrush(QColor(246, 97, 81, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush3)
        brush4 = QBrush(QColor(255, 203, 198, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush4)
        brush5 = QBrush(QColor(250, 150, 139, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush5)
        brush6 = QBrush(QColor(123, 49, 41, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush6)
        brush7 = QBrush(QColor(164, 65, 54, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        brush8 = QBrush(QColor(255, 255, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush8)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush2)
        brush9 = QBrush(QColor(250, 176, 168, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        brush10 = QBrush(QColor(255, 255, 220, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        brush11 = QBrush(QColor(239, 239, 239, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush8)
        brush12 = QBrush(QColor(202, 202, 202, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        brush13 = QBrush(QColor(159, 159, 159, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        brush14 = QBrush(QColor(184, 184, 184, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        brush15 = QBrush(QColor(118, 118, 118, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush15)
        brush16 = QBrush(QColor(247, 247, 247, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush16)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush17 = QBrush(QColor(177, 177, 177, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush17)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush2)
        self.pb_stop.setPalette(palette2)

        self.gridLayout_6.addWidget(self.pb_stop, 14, 0, 1, 2)

        self.pb_settings = QPushButton(self.dockWidgetContents)
        self.pb_settings.setObjectName(u"pb_settings")
        self.pb_settings.setEnabled(False)

        self.gridLayout_6.addWidget(self.pb_settings, 10, 0, 1, 2)

        self.sb_speed = QSpinBox(self.dockWidgetContents)
        self.sb_speed.setObjectName(u"sb_speed")
        self.sb_speed.setMinimum(3)
        self.sb_speed.setMaximum(7)
        self.sb_speed.setValue(5)

        self.gridLayout_6.addWidget(self.sb_speed, 9, 1, 1, 1)

        self.sb_x = QSpinBox(self.dockWidgetContents)
        self.sb_x.setObjectName(u"sb_x")
        self.sb_x.setMaximum(220)
        self.sb_x.setValue(40)

        self.gridLayout_6.addWidget(self.sb_x, 5, 1, 1, 1)

        self.label_2 = QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.label_2, 3, 0, 1, 2)

        self.label = QLabel(self.dockWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 5, 0, 1, 1)

        self.label_12 = QLabel(self.dockWidgetContents)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.label_12, 8, 0, 1, 1)

        self.label_15 = QLabel(self.dockWidgetContents)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.label_15, 11, 0, 1, 2)

        self.sb_axis_z = QSpinBox(self.dockWidgetContents)
        self.sb_axis_z.setObjectName(u"sb_axis_z")
        self.sb_axis_z.setMinimum(2)
        self.sb_axis_z.setMaximum(10)
        self.sb_axis_z.setValue(2)

        self.gridLayout_6.addWidget(self.sb_axis_z, 7, 1, 1, 1)

        self.sb_passages = QSpinBox(self.dockWidgetContents)
        self.sb_passages.setObjectName(u"sb_passages")
        self.sb_passages.setMinimum(1)
        self.sb_passages.setMaximum(10)
        self.sb_passages.setValue(1)

        self.gridLayout_6.addWidget(self.sb_passages, 8, 1, 1, 1)

        self.pb_start = QPushButton(self.dockWidgetContents)
        self.pb_start.setObjectName(u"pb_start")
        self.pb_start.setEnabled(False)
        palette3 = QPalette()
        brush18 = QBrush(QColor(78, 154, 6, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush18)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush18)
        brush19 = QBrush(QColor(190, 190, 190, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        self.pb_start.setPalette(palette3)

        self.gridLayout_6.addWidget(self.pb_start, 13, 0, 1, 2)

        self.sb_y = QSpinBox(self.dockWidgetContents)
        self.sb_y.setObjectName(u"sb_y")
        self.sb_y.setMaximum(220)
        self.sb_y.setValue(40)

        self.gridLayout_6.addWidget(self.sb_y, 4, 1, 1, 1)

        self.pte_displayGCode = QPlainTextEdit(self.dockWidgetContents)
        self.pte_displayGCode.setObjectName(u"pte_displayGCode")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pte_displayGCode.sizePolicy().hasHeightForWidth())
        self.pte_displayGCode.setSizePolicy(sizePolicy3)
        self.pte_displayGCode.setReadOnly(True)

        self.gridLayout_6.addWidget(self.pte_displayGCode, 12, 0, 1, 2)

        self.sb_step = QSpinBox(self.dockWidgetContents)
        self.sb_step.setObjectName(u"sb_step")
        self.sb_step.setValue(8)

        self.gridLayout_6.addWidget(self.sb_step, 6, 1, 1, 1)

        self.lbl_elapsed_time = QLabel(self.dockWidgetContents)
        self.lbl_elapsed_time.setObjectName(u"lbl_elapsed_time")

        self.gridLayout_6.addWidget(self.lbl_elapsed_time, 4, 0, 1, 1)

        self.label_7 = QLabel(self.dockWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 9, 0, 1, 1)

        self.label_4 = QLabel(self.dockWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 7, 0, 1, 1)

        self.label_3 = QLabel(self.dockWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 6, 0, 1, 1)

        self.dw_settings.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dw_settings)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Feutrage de laine", None))
        self.label_10.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Feutrage de laine</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Ce logiciel permet de lancer des cycles de feutrage.</p><p>Avant de lancer un cycle, il faut bien v\u00e9rifier que les param\u00e8tres sont corrects.</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">D\u00e9placements</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Pr\u00e9sentation", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Retour GCode", None))
        self.pb_clear.setText(QCoreApplication.translate("MainWindow", u"Effacer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Lancement du cycle", None))
        self.pb_openPort.setText(QCoreApplication.translate("MainWindow", u"Se connecter", None))
        self.pb_closePort.setText(QCoreApplication.translate("MainWindow", u"Fermer", None))
        self.pb_resfreshPorts.setText(QCoreApplication.translate("MainWindow", u"Mettre \u00e0 jour les ports", None))
        self.pb_stop.setText(QCoreApplication.translate("MainWindow", u"Arr\u00eater le cycle", None))
        self.pb_settings.setText(QCoreApplication.translate("MainWindow", u"Valider les param\u00e8tres", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Param\u00e8tres</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Largeur du plateau (mm)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nombre de passage Z", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">GCode</span></p></body></html>", None))
        self.pb_start.setText(QCoreApplication.translate("MainWindow", u"Lancer le cycle", None))
        self.pte_displayGCode.setPlaceholderText("")
        self.lbl_elapsed_time.setText(QCoreApplication.translate("MainWindow", u"Longueur du plateau (mm)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Vitesse", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"D\u00e9placement de l'axe Z ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"D\u00e9placement du porte-aiguilles (mm)", None))
    # retranslateUi

