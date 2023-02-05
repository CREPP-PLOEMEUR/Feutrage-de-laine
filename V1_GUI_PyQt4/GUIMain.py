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
		self.isStopped = False
		
		self.readingThread = ReadingData(1, "ReadingData Thread")
		

		#Signaux et slots
		self.connect(self.pb_start, SIGNAL("clicked()"), self.start)
		self.connect(self.pb_openPort, SIGNAL("clicked()"), self.openPort)
		#self.connect(self.pb_closePort, SIGNAL("clicked()"), self.closePort)
		self.connect(self.pb_refreshPorts, SIGNAL("clicked()"), self.refreshPort)
		self.connect(self.pb_stop, SIGNAL("clicked()"), self.stop)
		
		

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

		self.lbl_status.setText("Connecte")
		self.pb_start.setEnabled(True)


	def closePort(self): #Initialisation du port Série
		"""Fermeture du port série"""

		self.serial.close()
		print("Deconnnexion")
		self.statusBar().showMessage("Deconnecte")

				
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
		gcode += "G91\n"
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
		

	def start(self):
		"""Démarre le processus"""
		
		self.generateGCode()
		
		self.allCommands = self.strGCode.split("\n")  #Creation des commandes
		self.lbl_status.setText("Cycle en cours")
		self.pb_start.setEnabled(False)
		self.pb_stop.setEnabled(True)
		if(self.isStopped==True):
			self.readingThread = ReadingData(1, "ReadingData Thread")
			self.readingThread.initSerial(self.serial, self.allCommands)
			self.readingThread.start()
			self.serial.write("G91\n")
		else:
			self.readingThread.initSerial(self.serial, self.allCommands)
			self.readingThread.start()
			self.pb_stop.setEnabled(True)

			self.serial.write("G91\n")
		
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
		
		

	def clear(self):

		self.pte_gcodeReturn.clear()
		
	def endThread(self):
		
		self.isStopped = self.readingThread.stop()
		self.readingThread = None
		print("<Exit Thread>")
		
def quitApp():
	print("Exit")

def main(args):
	
	a=QApplication(args) 					#Création de l'application 
	f=QWidget() 							#Création du Widget
	c=myApp(f) 								#Création de la fenêtre graphique 
	a.aboutToQuit.connect(c.endThread) 		#Fonction de fermeture 
	f.show() 								#Affichage de la fenêtre QWidget
	r=a.exec_() 							#Exécution de l'application 
	return r								#Valeur de retour

#Code exécuté si ce fichier est appelé
if __name__=="__main__": 
	main(sys.argv) 



