#!/usr/bin/python
# -*- coding: utf-8 -*-

#Feutrage de laine
#V1 : Nicolas Le Guerroué
#nicolasleguerroue@gmail.com

#Importations 
from PyQt4.QtGui import *
from PyQt4.QtCore import * 
import serial.tools.list_ports
from math import floor
from ReadingData import *


import os,sys	#Commandes system
import serial 	#Liaison série
import time 	#Délai

from GUI import *  #Fichier généré par pyuic4

class myApp(QWidget, Ui_Feutrage): # la classe reçoit le Qwidget principal ET la classe définie dans test.py obtenu avec pyuic4
	
	def __init__(self, parent=None):
		"""Constructeur de classe"""
		QWidget.__init__(self) 		#Initialisation du QWidget 
		self.setupUi(parent) 		#Définition de l'interface graphique

		#Port série
		self.serial=None
		self.startNextCommand = False
		
		self.allCommands = []

		#GCode
		self.strGCode = ""
		self.gcodeIndex = 0
		self.startCommands = False
		
		self.readingThread = ReadingData(1, "ReadingData Thread")
		

		#Signaux et slots
		self.connect(self.pb_start, SIGNAL("clicked()"), self.start)
		self.connect(self.pb_openPort, SIGNAL("clicked()"), self.openPort)
		self.connect(self.pb_closePort, SIGNAL("clicked()"), self.closePort)
		self.connect(self.pb_generateGCode, SIGNAL("clicked()"), self.generateGCode)
		self.connect(self.pb_clear, SIGNAL("clicked()"), self.clear)
		self.connect(self.pb_refreshPorts, SIGNAL("clicked()"), self.refreshPort)
		
		

		#Affiche les ports disponibles
		for port in serial.tools.list_ports.comports():
			self.cb_ports.addItem(str(port.device))



	def refreshPort(self):
		"""Mise à jour des ports disponibles"""

		self.cb_ports.clear()
		for port in serial.tools.list_ports.comports():
			self.cb_ports.addItem(str(port.device))
			print(port.device)

	def openPort(self): 
		"""Initialisation du port Série"""

		print("Initialisation du port série")
		self.serial = serial.Serial(str(self.cb_ports.currentText()), int(self.cb_bauds.currentText()),serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=0.1)

		self.pb_generateGCode.setEnabled(True)
		self.lbl_status.setText("Connecte - GCode non genere")


	def closePort(self): #Initialisation du port Série
		"""Fermeture du port série"""

		self.serial.close()
		print("Deconnnexion")
		self.statusBar().showMessage("Deconnecte")
		self.pb_generateGCode.setEnabled(False)
	
				
	def generateGCode(self):
		"""Génération des instructions GCode"""

		#Calcul des itérations
		self.yWidth = int(self.sb_y.value())
		self.xWidth = int(self.sb_x.value())

		self.yIter = floor(int(self.yWidth)/8)
		self.xIter = floor(int(self.xWidth)/8)

		nbBlocX = self.xIter/2
		self.speed = self.sb_speed

		gcode = "" 		#variable contenant tout le GCode
		
		#Retour Home
		gcode += "G28 X F4\n"
		gcode += "G28 Y F4\n"
		gcode += "G28 Z F4\n"

		for xBloc in range(0, int(nbBlocX)):

			#Code bloc	
			for xStep in range(0,int(self.yIter)):
				gcode += "G01 Y"+str(self.sb_step.value())+" F"+str(self.sb_speed.value())+"\n"
				for i in range(0, int(self.sb_passages.value())):
					gcode += "G01 Z"+str(self.sb_axis_z.value())+" F"+str(self.sb_speed_z.value())+"\n"
					gcode += "G28 Z"+" F"+str(self.sb_speed_z.value())+"\n"
	
			gcode += "G01 X"+str(self.sb_step.value())+" F"+str(self.sb_speed.value())+"\n"
			for i in range(0, int(self.sb_passages.value())):
				gcode += "G01 Z"+str(self.sb_axis_z.value())+" F"+str(self.sb_speed_z.value())+"\n"
				gcode += "G28 Z"+" F"+str(self.sb_speed_z.value())+"\n"
	
			for xStep in range(0,int(self.yIter)):
				gcode += "G01 Y-"+str(self.sb_step.value())+" F"+str(self.sb_speed.value())+"\n"
				for i in range(0, int(self.sb_passages.value())):
					gcode += "G01 Z"+str(self.sb_axis_z.value())+" F"+str(self.sb_speed_z.value())+"\n"
					gcode += "G28 Z"+" F"+str(self.sb_speed_z.value())+"\n"
	
			gcode += "G01 X"+str(self.sb_step.value())+" F"+str(self.sb_speed.value())+"\n"
			for i in range(0, int(self.sb_passages.value())):
				gcode += "G01 Z"+str(self.sb_axis_z.value())+" F"+str(self.sb_speed_z.value())+"\n"
				gcode += "G28 Z"+" F"+str(self.sb_speed_z.value())+"\n"

		self.strGCode = gcode
		self.pte_displayGCode.appendPlainText(self.strGCode)
		self.lbl_lines.setText("0 / "+str(len(self.strGCode.split("\n"))-1))
		self.lbl_status.setText("Connecte - GCode genere")
		self.pb_start.setEnabled(True)

	def start(self):
		
		self.allCommands = self.strGCode.split("\n")  #Creation des commandes

		self.readingThread.initSerial(self.serial, self.allCommands)
		self.readingThread.start()
		
		self.lbl_status.setText("En cours")

		self.serial.write("G91\n")

		"""self.sendCommand("G28 X F4")		#Home X
		self.sendCommand("G28 Y F4")		#Home Y
		self.sendCommand("G28 Z F4")		#Home Z
		

		print("NB instruction : "+str(len(self.allCommands)))
		#Pour toutes les commandes
		for line in range (0,len(self.allCommands)):
			self.sendCommand(self.allCommands[line])
			self.lbl_lines.setText(str(line)+" / "+str(len(self.allCommands)-1))
			self.lbl_lines.show()
			print(self.lbl_lines.text())
			self.pte_gcodeReturn.appendPlainText(">>> "+self.allCommands[line])
			self.pte_gcodeReturn.appendPlainText(">>> OK")
			self.pte_gcodeReturn.show()
			time.sleep(0.05)

	
		#self.pb_progressBar.setValue(100)
		self.lbl_status.setText("Termine")
		self.close()"""


	def clear(self):

		self.pte_gcodeReturn.clear()
	

def main(args):
	
	a=QApplication(args) 	#Création de l'application 
	f=QWidget() 			#Création du Widget
	c=myApp(f) 				#Création de la fenêtre graphique 
	f.show() 				#Affichage de la fenêtre QWidget
	r=a.exec_() 			#Exécution de l'application 
	return r				#Valeur de retour

#Code exécuté si ce fichier est appelé
if __name__=="__main__": 
	main(sys.argv) 



