#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Feutrage Laine
# GPLv3

#Importation des modules
from PyQt5 import QtWidgets

from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

from PyQt5.QtCore import QIODevice
from PyQt5.QtCore import QTimer,QDateTime
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

import os,sys
import serial # communication serie
import time
from math import floor

from FeutrageGUI import *


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		#fonction de lecture
		self.callbackReading = self.readData	
		self.port = "/dev/ttyACM0"
		self.baudrate = 115200

		self.strGCode = ""


		#Signaux et slots
		self.ui.pb_resfreshPorts.clicked.connect(self.refreshPort)
		self.ui.pb_openPort.clicked.connect(self.openPort)
		self.ui.pb_closePort.clicked.connect(self.closePort)
		self.ui.pb_generateGCode.clicked.connect(self.generateGCode)
		self.ui.pb_start.clicked.connect(self.start)


		for port in QSerialPortInfo.availablePorts():
			self.ui.cb_ports.addItem("/dev/"+port.portName())

		#Déclarations internes
		self.serial=None # déclaration initiale
		self.successCommand = True

	def sendCommand(self, command):

		while(self.successCommand==False):
			print("Attente d'une réponse de la commande précédente")
			time.sleep(0.05)
				
		print("Envoi de la commande")
		self.serial.write(bytes(command+'\n', encoding='utf8'))
		#self.successCommand = False
		result=""
		waitingOK = True
		while (waitingOK==True): # tant que au moins un caractère en réception
			char=self.serial.read(10).decode("utf-8") # on lit le caractère

			if(char=='\n'): # si saut de ligne, on sort du while
				result=""
			else: #tant que c'est pas le saut de ligne, on l'ajoute à la chaine 
				result=result+char	
				if(result=="<ok>\n"):
					print("Commande : OK")
					waitingOK = False

	def refreshPort(self):

		self.ui.cb_ports.clear()
		for port in QSerialPortInfo.availablePorts():
			self.ui.cb_ports.addItem("/dev/"+port.portName())

	def openPort(self): #Initialisation du port Série

		print("Initialisation du port série")

		self.serial = QSerialPort(self.ui.cb_ports.currentText(),baudRate=self.baudrate)#, readyRead=self.callbackReading)
		result = self.serial.open(QIODevice.ReadWrite) #Tentative de connexion

		if(result):
			self.statusBar().showMessage("Le port '"+self.port+"' est ouvert ("+str(self.baudrate)+")")
		else:
			self.statusBar().showMessage("Impossible d'ouvrir le port '"+str(self.port)+"'" )

	def closePort(self): #Initialisation du port Série

		self.serial.close()
		self.statusBar().showMessage("")
		
	def readData(self):
		data = self.serial.read(20).decode("utf-8")
		if(data=="<ok>\n"):
			print("OK")
			self.successCommand = True



	def generateGCode(self):


		self.yWidth = int(self.ui.sb_y.value())
		self.xWidth = int(self.ui.sb_x.value())

		self.yIter = floor(int(self.yWidth)/8)
		self.xIter = floor(int(self.xWidth)/8)

		nbBlocX = self.xIter/2
		self.speed = self.ui.sb_speed

		

		gcode = ""
		for xBloc in range(0, int(nbBlocX)):
			#Code bloc	
			for xStep in range(0,int(self.yIter)):
				gcode += "G01 Y"+str(self.ui.sb_step.value())+" F4"+"\n"
				gcode += "G04 P0.1"+"\n"
	
			gcode += "G01 X"+str(self.ui.sb_step.value())+" F"+str(self.ui.sb_speed.value())+"\n"
	
			for xStep in range(0,int(self.yIter)):
				gcode += "G01 Y-"+str(self.ui.sb_step.value())+" F4"+"\n"
				gcode += "G04 P0.1"+"\n"
	
			gcode += "G01 X"+str(self.ui.sb_step.value())+" F"+str(self.ui.sb_speed.value())+"\n"
	

		self.strGCode = gcode
		self.ui.pte_displayGCode.appendPlainText(self.strGCode)

	def start(self):

		print("Mode relatif")
		self.sendCommand("G91") #Mode relatif
		#Retour Home
		print("Retour origine")
		self.sendCommand("G28 X")
		self.sendCommand("G28 Y")


def main():
	
	app = QtWidgets.QApplication(sys.argv) #Creation de l'application
	ihm = MainWindow()                      #Appel de notre classe principale
	ihm.show()                              #Affichage de l'interface
	sys.exit(app.exec_())                   #Loop


if __name__ == "__main__":              
    main()



