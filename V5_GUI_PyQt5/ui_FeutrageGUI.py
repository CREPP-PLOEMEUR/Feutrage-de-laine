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
        self.lbl_status = QLabel(self.centralwidget)
        self.lbl_status.setObjectName(u"lbl_status")

        self.gridLayout.addWidget(self.lbl_status, 2, 6, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 5, 1, 1)

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
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pte_displayGCode = QPlainTextEdit(self.tab_2)
        self.pte_displayGCode.setObjectName(u"pte_displayGCode")
        self.pte_displayGCode.setReadOnly(True)

        self.gridLayout_4.addWidget(self.pte_displayGCode, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
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

        self.gridLayout.addItem(self.horizontalSpacer, 2, 4, 1, 1)

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
        self.label_13 = QLabel(self.dockWidgetContents)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 2)

        self.cb_ports = QComboBox(self.dockWidgetContents)
        self.cb_ports.setObjectName(u"cb_ports")

        self.gridLayout_6.addWidget(self.cb_ports, 2, 1, 1, 1)

        self.sb_speed = QSpinBox(self.dockWidgetContents)
        self.sb_speed.setObjectName(u"sb_speed")
        self.sb_speed.setMaximum(8)
        self.sb_speed.setValue(4)

        self.gridLayout_6.addWidget(self.sb_speed, 10, 1, 1, 1)

        self.label_14 = QLabel(self.dockWidgetContents)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_3 = QLabel(self.dockWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 7, 0, 1, 1)

        self.label_4 = QLabel(self.dockWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 8, 0, 1, 1)

        self.sb_x = QSpinBox(self.dockWidgetContents)
        self.sb_x.setObjectName(u"sb_x")
        self.sb_x.setMaximum(600)
        self.sb_x.setValue(30)

        self.gridLayout_6.addWidget(self.sb_x, 6, 1, 1, 1)

        self.pb_closePort = QPushButton(self.dockWidgetContents)
        self.pb_closePort.setObjectName(u"pb_closePort")
        palette = QPalette()
        brush = QBrush(QColor(239, 41, 41, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.pb_closePort.setPalette(palette)

        self.gridLayout_6.addWidget(self.pb_closePort, 3, 1, 1, 1)

        self.label_7 = QLabel(self.dockWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 10, 0, 1, 1)

        self.pb_generateGCode = QPushButton(self.dockWidgetContents)
        self.pb_generateGCode.setObjectName(u"pb_generateGCode")
        self.pb_generateGCode.setEnabled(False)

        self.gridLayout_6.addWidget(self.pb_generateGCode, 11, 0, 1, 2)

        self.pb_openPort = QPushButton(self.dockWidgetContents)
        self.pb_openPort.setObjectName(u"pb_openPort")
        palette1 = QPalette()
        brush1 = QBrush(QColor(138, 226, 52, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        self.pb_openPort.setPalette(palette1)

        self.gridLayout_6.addWidget(self.pb_openPort, 3, 0, 1, 1)

        self.sb_passages = QSpinBox(self.dockWidgetContents)
        self.sb_passages.setObjectName(u"sb_passages")
        self.sb_passages.setValue(2)

        self.gridLayout_6.addWidget(self.sb_passages, 9, 1, 1, 1)

        self.sb_y = QSpinBox(self.dockWidgetContents)
        self.sb_y.setObjectName(u"sb_y")
        self.sb_y.setMaximum(600)
        self.sb_y.setValue(30)

        self.gridLayout_6.addWidget(self.sb_y, 5, 1, 1, 1)

        self.label = QLabel(self.dockWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 6, 0, 1, 1)

        self.sb_axis_z = QSpinBox(self.dockWidgetContents)
        self.sb_axis_z.setObjectName(u"sb_axis_z")
        self.sb_axis_z.setMinimum(2)
        self.sb_axis_z.setMaximum(10)
        self.sb_axis_z.setValue(2)

        self.gridLayout_6.addWidget(self.sb_axis_z, 8, 1, 1, 1)

        self.pb_resfreshPorts = QPushButton(self.dockWidgetContents)
        self.pb_resfreshPorts.setObjectName(u"pb_resfreshPorts")

        self.gridLayout_6.addWidget(self.pb_resfreshPorts, 1, 0, 1, 2)

        self.sb_step = QSpinBox(self.dockWidgetContents)
        self.sb_step.setObjectName(u"sb_step")
        self.sb_step.setValue(8)

        self.gridLayout_6.addWidget(self.sb_step, 7, 1, 1, 1)

        self.pb_start = QPushButton(self.dockWidgetContents)
        self.pb_start.setObjectName(u"pb_start")
        self.pb_start.setEnabled(False)
        palette2 = QPalette()
        brush2 = QBrush(QColor(78, 154, 6, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        brush4 = QBrush(QColor(239, 239, 239, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        brush5 = QBrush(QColor(190, 190, 190, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        self.pb_start.setPalette(palette2)

        self.gridLayout_6.addWidget(self.pb_start, 12, 0, 1, 2)

        self.lbl_elapsed_time = QLabel(self.dockWidgetContents)
        self.lbl_elapsed_time.setObjectName(u"lbl_elapsed_time")

        self.gridLayout_6.addWidget(self.lbl_elapsed_time, 5, 0, 1, 1)

        self.label_2 = QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.label_2, 4, 0, 1, 2)

        self.pb_stop = QPushButton(self.dockWidgetContents)
        self.pb_stop.setObjectName(u"pb_stop")

        self.gridLayout_6.addWidget(self.pb_stop, 13, 0, 1, 2)

        self.label_12 = QLabel(self.dockWidgetContents)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.label_12, 9, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 14, 0, 1, 1)

        self.dw_settings.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dw_settings)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Feutrage de laine", None))
        self.lbl_status.setText(QCoreApplication.translate("MainWindow", u"Non connect\u00e9", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Cycle : ", None))
        self.label_10.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Feutrage de laine</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Ce logiciel permet de lancer des cycles de feutrage.</p><p>Avant de lancer un cycle, il faut bien v\u00e9rifier que les param\u00e8tres sont corrects.</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">D\u00e9placements</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Pr\u00e9sentation", None))
        self.pte_displayGCode.setPlaceholderText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9ration du GCode", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Retour GCode", None))
        self.pb_clear.setText(QCoreApplication.translate("MainWindow", u"Effacer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Lancement du cycle", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Connexion</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Port connect\u00e9", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"D\u00e9placement du porte-aiguilles (mm)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"D\u00e9placement de l'axe Z (mm)", None))
        self.pb_closePort.setText(QCoreApplication.translate("MainWindow", u"Fermer", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Vitesse", None))
        self.pb_generateGCode.setText(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rer le GCode", None))
        self.pb_openPort.setText(QCoreApplication.translate("MainWindow", u"Se connecter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Largeur du plateau (mm)", None))
        self.pb_resfreshPorts.setText(QCoreApplication.translate("MainWindow", u"Mettre \u00e0 jour les ports", None))
        self.pb_start.setText(QCoreApplication.translate("MainWindow", u"Lancer le cycle", None))
        self.lbl_elapsed_time.setText(QCoreApplication.translate("MainWindow", u"Longueur du plateau (mm)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Param\u00e8tres</span></p></body></html>", None))
        self.pb_stop.setText(QCoreApplication.translate("MainWindow", u"Arreter", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nombre de passage Z", None))
    # retranslateUi

