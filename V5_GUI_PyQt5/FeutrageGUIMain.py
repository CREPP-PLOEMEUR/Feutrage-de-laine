#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Feutrage Laine
# GPLv3
#Importation des modules

from PyQt5 import QtWidgets
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

import serial 	#Liaison série

from PyQt5.QtCore import QIODevice
from PyQt5.QtCore import QTimer,QDateTime
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

from ReadingData import ReadingData
import os,sys
import time
from math import floor

from FeutrageGUI import *  #Fenêtre générée par pyuic5


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		#fonction de lecture
		#self.callbackReading = self.readData	
		self.port = "/dev/ttyACM0"
		self.baudrate = 115200

		self.strGCode = ""
  
		self.gcodeIndex = 0
		self.startCommands = False
		self.isStopped = False
  
		self.readingThread = ReadingData(1, "ReadingData Thread")
		#Signaux et slots
		self.ui.pb_resfreshPorts.clicked.connect(self.refreshPort)
		self.ui.pb_openPort.clicked.connect(self.openPort)
		self.ui.pb_closePort.clicked.connect(self.closePort)
		self.ui.pb_generateGCode.clicked.connect(self.generateGCode)
		self.ui.pb_start.clicked.connect(self.start)
		self.ui.pb_clear.clicked.connect(self.clear)

		#Affiche les ports disponibles
		for port in QSerialPortInfo.availablePorts():
			self.ui.cb_ports.addItem("/dev/"+port.portName())

		#Déclarations internes
		self.serial=None # déclaration initiale
		self.successCommand = True

	def refreshPort(self):

		self.ui.cb_ports.clear()
		for port in QSerialPortInfo.availablePorts():
			self.ui.cb_ports.addItem("/dev/"+port.portName())

	def openPort(self): 
		"""Initialisation du port Série"""

		print("Initialisation du port série")
		self.serial = serial.Serial(str(self.ui.cb_ports.currentText()), self.baudrate,serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=0.1)
		self.ui.lbl_status.setText("Connecte")
		self.ui.pb_start.setEnabled(True)

	def closePort(self): #Initialisation du port Série
		"""Fermeture du port série"""

		self.serial.close()
		print("Déconnnexion")
		self.statusBar().showMessage("Déconnecté")
		
	def start(self):
		"""Démarre le processus"""
		
		self.generateGCode()
		print("Starting GCODE")
		self.allCommands = self.strGCode.split("\n")  #Creation des commandes
		self.ui.lbl_status.setText("Cycle en cours")
		self.ui.pb_start.setEnabled(False)
		self.ui.pb_stop.setEnabled(True)
		if(self.isStopped==True):
			self.readingThread = ReadingData(1, "ReadingData Thread")
			self.readingThread.initSerial(self.serial, self.allCommands)
			self.readingThread.start()
			self.serial.write(b"G91\n")
		else:
			self.readingThread.initSerial(self.serial, self.allCommands)
			self.readingThread.start()
			self.ui.pb_stop.setEnabled(True)

			#self.serial.write(b"G91\n")
			time.sleep(0.5)
			self.readingThread.sendCommand("G91\n")

		
	def stop(self):
		"""Stop proprement le processus"""
		print("stop")
		self.isStopped = self.readingThread.stop()
		self.lbl_status.setText("Fin du cycle")
		self.pb_start.setEnabled(True)
		self.pb_stop.setEnabled(False)
		self.strGCode = ""
		self.pte_displayGCode.setPlainText("")
		self.readingThread = None
		self.tabWidget.setCurrentIndex(1)



	def generateGCode(self):
		"""Génération des instructions GCode"""

		#Calcul des itérations
		self.yWidth = int(self.ui.sb_y.value())
		self.xWidth = int(self.ui.sb_x.value())

		self.yIter = floor(int(self.yWidth)/8)
		self.xIter = floor(int(self.xWidth)/8)

		nbBlocX = self.xIter/2
		self.speed = self.ui.sb_speed

		gcode = "" 		#variable contenant tout le GCode
		
		#Retour Home
		gcode += "G91\n"
		gcode += "G28 X F4\n"
		gcode += "G28 Y F4\n"
		gcode += "G28 Z F4\n"

		for xBloc in range(0, int(nbBlocX)):

			#Code bloc	
			for xStep in range(0,int(self.yIter)):
				gcode += "G01 Y"+str(self.ui.sb_step.value())+" F"+str(self.ui.sb_speed.value())+"\n"
				for i in range(0, int(self.ui.sb_passages.value())):
					gcode += "G01 Z"+str(self.ui.sb_axis_z.value())+" F"+str(self.ui.sb_speed.value())+"\n"
					gcode += "G28 Z"+" F"+str(self.ui.sb_speed.value())+"\n"
	
			gcode += "G01 X"+str(self.ui.sb_step.value())+" F"+str(self.ui.sb_speed.value())+"\n"
			for i in range(0, int(self.ui.sb_passages.value())):
				gcode += "G01 Z"+str(self.ui.sb_axis_z.value())+" F"+str(self.ui.sb_speed.value())+"\n"
				gcode += "G28 Z"+" F"+str(self.ui.sb_speed.value())+"\n"
	
			for xStep in range(0,int(self.yIter)):
				gcode += "G01 Y-"+str(self.ui.sb_step.value())+" F"+str(self.ui.sb_speed.value())+"\n"
				for i in range(0, int(self.ui.sb_passages.value())):
					gcode += "G01 Z"+str(self.ui.sb_axis_z.value())+" F"+str(self.ui.sb_speed.value())+"\n"
					gcode += "G28 Z"+" F"+str(self.ui.sb_speed.value())+"\n"
	
			gcode += "G01 X"+str(self.ui.sb_step.value())+" F"+str(self.ui.sb_speed.value())+"\n"
			for i in range(0, int(self.ui.sb_passages.value())):
				gcode += "G01 Z"+str(self.ui.sb_axis_z.value())+" F"+str(self.ui.sb_speed.value())+"\n"
				gcode += "G28 Z"+" F"+str(self.ui.sb_speed.value())+"\n"

		self.strGCode = gcode
		self.ui.pte_displayGCode.appendPlainText(self.strGCode)

	def clear(self):

		self.ui.pte_gcodeReturn.clear()

def main():
	
	app = QtWidgets.QApplication(sys.argv) #Creation de l'application
	ihm = MainWindow()                      #Appel de notre classe principale
	ihm.show()                              #Affichage de l'interface
	sys.exit(app.exec_())                   #Loop


if __name__ == "__main__":              
    main()



