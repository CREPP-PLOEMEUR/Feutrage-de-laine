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
import time
from math import floor

from FeutrageGUI import *  #Fenêtre générée par pyuic5


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
		self.ui.pb_clear.clicked.connect(self.clear)

		#Affiche les ports disponibles
		for port in QSerialPortInfo.availablePorts():
			self.ui.cb_ports.addItem("/dev/"+port.portName())

		#Déclarations internes
		self.serial=None # déclaration initiale
		self.successCommand = True

	def sendCommand(self, command):

		# while(self.successCommand==False):
		# 	print("Attente d'une réponse de la commande précédente")
		# 	time.sleep(0.05)
				
		print(">>> Envoi de la commande '" +command+"'")
		self.serial.write(str.encode(command+"\n"))

		# data = self.serial.readLine(100)
		# while(not bytes("ok", "utf-8") in data):
		# 	data = self.serial.readLine(100)
		# 	time.sleep(0.01)
		# print(data)
		# print(len(data))
		# sortedData = data[-40:]
		# if(">>>" in sortedData):
		# 	print("OK")
		# 	self.successCommand = True
		#self.successCommand = False

	def refreshPort(self):

		self.ui.cb_ports.clear()
		for port in QSerialPortInfo.availablePorts():
			self.ui.cb_ports.addItem("/dev/"+port.portName())

	def openPort(self): #Initialisation du port Série

		print("Initialisation du port série")

		self.serial = QSerialPort(self.ui.cb_ports.currentText(),baudRate=self.baudrate, readyRead=self.callbackReading)
		result = self.serial.open(QIODevice.ReadWrite) #Tentative de connexion

		if(result):
			self.statusBar().showMessage("Le port '"+self.port+"' est ouvert ("+str(self.baudrate)+")")
			self.ui.pb_generateGCode.setEnabled(True)
			self.ui.lbl_status.setText("GCode non généré")
		else:
			self.statusBar().showMessage("Impossible d'ouvrir le port '"+str(self.port)+"'" )

	def closePort(self): #Initialisation du port Série

		self.serial.close()
		self.statusBar().showMessage("")
		self.ui.pb_generateGCode.setEnabled(False)
		
	def readData(self):
		print("READ CALLBACk")
		data = self.serial.read(100).decode("utf-8")
		print(data)
		print(len(data))
		sortedData = data[-40:]
		if(">>>" in sortedData):
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
		self.ui.lbl_status.setText("GCode généré")
		self.ui.pb_start.setEnabled(True)

	def start(self):

		self.allCommands = self.strGCode.split("\n")
		self.ui.lbl_status.setText("En cours")
		self.sendCommand("G91")
		self.sendCommand("G28 X")
		#self.serial.write(bytes("G91"+'\n'+"G28 X", encoding='utf-8'))
		time.sleep(1)

		#self.sendCommand("G28 X")
		#self.serial.write(bytes("G91"+'\n', encoding='utf-8'))
		#self.sendCommand("G28 Y")

		# for line in range (0,len(self.allCommands)):
		# 	#print(self.allCommands[line])
		# 	print(line)
		# 	while(self.successCommand==False):
		# 		continue
		# 		print("waiting")
		# 	#print("OK command")
		# 	#time.sleep(2)
		# 	#print("OK command")
		# 	self.sendCommand(self.allCommands[line])

			# time.sleep(0.01)
			# self.ui.pb_progressBar.setValue(int(line/len(self.allCommands)*100))
			# self.ui.pte_gcodeReturn.appendPlainText(">>> "+self.allCommands[line])
			# time.sleep(0.005)
			# self.ui.pte_gcodeReturn.appendPlainText(">>> OK")



		# self.ui.pb_progressBar.setValue(100)
		# self.ui.lbl_status.setText("Terminé")
		# print("Mode relatif")
		# self.sendCommand("G91") #Mode relatif
		# #Retour Home
		# print("Retour origine")
		# self.sendCommand("G28 X")
		# self.sendCommand("G28 Y")

	def clear(self):

		self.ui.pte_gcodeReturn.clear()

def main():
	
	app = QtWidgets.QApplication(sys.argv) #Creation de l'application
	ihm = MainWindow()                      #Appel de notre classe principale
	ihm.show()                              #Affichage de l'interface
	sys.exit(app.exec_())                   #Loop


if __name__ == "__main__":              
    main()



