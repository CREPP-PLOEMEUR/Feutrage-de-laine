#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Feutrage Laine
# GPLv3
#Importation des modules

from PyQt5 import QtWidgets
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

import resources
from PyQt5.QtCore import QTimer,QDateTime

import serial 	#Serial link
import sys		#OS

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

		#Reading function
		self.port = "/dev/ttyACM0"
		self.baudrate = 115200

		self.strGCode = ""
  
		self.ui.pb_settings.setIcon(QtGui.QIcon(":/icon/gear.png"))
		self.ui.pb_start.setIcon(QtGui.QIcon(":/icon/run.png"))
  
		self.gcodeIndex = 0
		self.startCommands = False
		self.isStopped = False
  
		self.readingThread = ReadingData(1, "ReadingData Thread")
		self.readingThread.addProgressBar(self.ui.pb_progressBar)
		self.readingThread.addStatusBar(self.statusBar())
  
		self.statusBar().showMessage("Déconnecté")
		#Signals & slots
		self.ui.pb_resfreshPorts.clicked.connect(self.refreshPort)
		self.ui.pb_openPort.clicked.connect(self.openPort)
		self.ui.pb_closePort.clicked.connect(self.closePort)
		self.ui.pb_settings.clicked.connect(self.generateGCode)
		self.ui.pb_start.clicked.connect(self.start)
		self.ui.pb_stop.clicked.connect(self.stopButton)

		#Display available ports
		for port in QSerialPortInfo.availablePorts():
			
			if(sys.platform == 'win32'):
				self.ui.cb_ports.addItem(port.portName())
			elif(sys.platform == "linux"):
				self.ui.cb_ports.addItem("/dev/"+port.portName())
			else:
				self.ui.cb_ports.addItem("Unknown")
		
		if(self.ui.cb_ports.count()>0):
			self.ui.pb_openPort.setEnabled(True)
		else:
			self.ui.pb_openPort.setEnabled(False)
		self.serial=None #Serial object
		self.successCommand = True
  
		#Timer to check end of ps
		self.timer=QTimer()
		self.timer.timeout.connect(self.endHandler)
		self.timer.start(500)

		#*Display image cycle
		self.ui.label_10.setPixmap(QtGui.QPixmap(":/icon/cycle.png"))

		self.alreadyPaused = False

	def endHandler(self):
		if(self.readingThread!=None):
			if(self.readingThread.cycleIsOver==True):
				self.statusBar().showMessage("Cycle terminé")
    
				self.ui.pb_stop.setDisabled(True)
				self.ui.sb_passages.setEnabled(True)
				self.ui.sb_y.setEnabled(True)
				self.ui.sb_x.setEnabled(True)
				self.ui.sb_step.setEnabled(True)
				self.ui.sb_axis_z.setEnabled(True)
				self.ui.sb_passages.setEnabled(True)
				self.ui.sb_speed.setEnabled(True)
    
				self.ui.pb_settings.setEnabled(True)
				self.ui.pb_start.setEnabled(False)
				self.ui.pb_start.setStyleSheet("background-color:green;")
				self.ui.pb_start.setText("Lancer le cycle")
				self.ui.pb_start.setIcon(QtGui.QIcon(":/icon/run.png"))
    
				#reset all var
				self.stop()
				self.readingThread.reset()
				time.sleep(0.2)
				self.readingThread = ReadingData(1, "ReadingData Thread")
				self.readingThread.addProgressBar(self.ui.pb_progressBar)
				self.readingThread.addStatusBar(self.statusBar())
				self.allCommands = str("G91 \n").split("\n") 
				self.readingThread.initSerial(self.serial, self.allCommands)
				self.ui.pb_start.clicked.connect(self.start)
				if(not self.alreadyPaused==True):
					self.ui.pb_start.clicked.disconnect(self.resume)
  
	def stopButton(self):
		print("Stop forced")
		if(self.readingThread!=None):
			if(self.readingThread.cycleIsOver==False):
				self.statusBar().showMessage("Cycle arrêté par l'utilisateur")
    
				self.ui.pb_stop.setDisabled(True)
				self.ui.sb_passages.setEnabled(True)
				self.ui.sb_y.setEnabled(True)
				self.ui.sb_x.setEnabled(True)
				self.ui.sb_step.setEnabled(True)
				self.ui.sb_axis_z.setEnabled(True)
				self.ui.sb_passages.setEnabled(True)
				self.ui.sb_speed.setEnabled(True)
    
				self.ui.pb_settings.setEnabled(True)
				self.ui.pb_start.setEnabled(False)
				self.ui.pb_start.setStyleSheet("background-color:green;")
				self.ui.pb_start.setText("Lancer le cycle")
				self.ui.pb_start.setIcon(QtGui.QIcon(":/icon/run.png"))
    
				#reset all var
				self.stop()
				self.readingThread.reset()
				time.sleep(0.2)
				self.readingThread = ReadingData(1, "ReadingData Thread")
				self.readingThread.addProgressBar(self.ui.pb_progressBar)
				self.readingThread.addStatusBar(self.statusBar())
				self.allCommands = str("G91 \nG28 Z\nG28 Y\nG28 X\n").split("\n") 
				self.readingThread.initSerial(self.serial, self.allCommands)
				self.readingThread.start()
				self.ui.pb_start.clicked.connect(self.start)
				if(self.alreadyPaused == True):
					self.ui.pb_start.clicked.disconnect(self.resume)
    
	def refreshPort(self):

		self.ui.cb_ports.clear()
		for port in QSerialPortInfo.availablePorts():
			if(sys.platform == 'win32'):
				self.ui.cb_ports.addItem(port.portName())
			elif(sys.platform == "linux"):
				self.ui.cb_ports.addItem("/dev/"+port.portName())
			else:
				self.ui.cb_ports.addItem("Unknown")


		if(self.ui.cb_ports.count()>0):
			self.ui.pb_openPort.setEnabled(True)
		else:
			self.ui.pb_openPort.setEnabled(False)
	def openPort(self): 
		"""Opening Serial port"""
		self.serial = serial.Serial(str(self.ui.cb_ports.currentText()), self.baudrate,serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=0.1)
		self.statusBar().showMessage("Connecté, en attente de validation des paramètres")
		self.ui.pb_settings.setEnabled(True)
		self.ui.pb_closePort.setEnabled(True)
		self.ui.pb_openPort.setEnabled(False)

	def closePort(self): 
		"""Closing serial port"""
		self.serial.close()
		self.statusBar().showMessage("Déconnecté")
		
	def start(self):
		"""Start processus"""
		
		#Avoid change settings
		self.ui.sb_passages.setEnabled(False)
		self.ui.sb_y.setEnabled(False)
		self.ui.sb_x.setEnabled(False)
		self.ui.sb_step.setEnabled(False)
		self.ui.sb_axis_z.setEnabled(False)
		self.ui.sb_passages.setEnabled(False)
		self.ui.sb_speed.setEnabled(False)
  

  
		self.allCommands = self.strGCode.split("\n")  
		self.statusBar().showMessage("Cycle en cours...")
		self.ui.pb_settings.setEnabled(False)
		self.ui.pb_stop.setEnabled(True)

		if(self.readingThread==None):	
			print("Restart with command "+str(self.savedIndexCommand))
			self.readingThread = ReadingData(1, "ReadingData Thread", self.savedIndexCommand)
			self.readingThread.addProgressBar(self.ui.pb_progressBar)
			self.readingThread.addStatusBar(self.statusBar())
			self.readingThread.initSerial(self.serial, self.allCommands)
			self.readingThread.start()
			time.sleep(0.1)
   
		else:
			self.readingThread.initSerial(self.serial, self.allCommands)
			self.readingThread.addProgressBar(self.ui.pb_progressBar)
			self.readingThread.addStatusBar(self.statusBar())
			self.readingThread.start()
			self.ui.pb_stop.setEnabled(True)
			time.sleep(0.1)
			self.readingThread.sendCommand("G91\n")
   
		self.ui.pb_start.setEnabled(True)
		self.ui.pb_start.clicked.disconnect(self.start)
		self.ui.pb_start.clicked.connect(self.resume)
		self.ui.pb_start.setIcon(QtGui.QIcon(":/icon/pause.png"))
		self.ui.pb_start.setText("Mettre en pause")
		self.ui.pb_start.setStyleSheet("background-color:blue;")
  
	def resume(self):
		
		self.statusBar().showMessage("Cycle en pause")
		self.ui.sb_speed.setEnabled(True)
		self.ui.pb_settings.setEnabled(True)
		self.readingThread.stop()
		self.readingThread.isRunning = False
		self.readingThread.isWorking = False
		self.savedIndexCommand = self.readingThread.currentIndexCommand
		self.ui.pb_start.clicked.disconnect(self.resume)
		self.ui.pb_start.clicked.connect(self.start)
		self.ui.pb_start.setStyleSheet("background-color:green;")
		self.ui.pb_start.setText("Relancer le cycle")
		self.ui.pb_start.setIcon(QtGui.QIcon(":/icon/run.png"))
		self.readingThread = None
		self.alreadyPaused = True
		
  
	def stop(self):
		"""Stop processus"""

		self.isStopped = self.readingThread.stop()
		#self.ui.pb_start.setEnabled(True)
		self.ui.pb_stop.setEnabled(False)
		self.strGCode = ""
		self.ui.pte_displayGCode.setPlainText("")
		



	def generateGCode(self):
		"""GCode generator"""

		self.ui.pb_start.setEnabled(True)
		#Computing
		self.yWidth = int(self.ui.sb_y.value())
		self.xWidth = int(self.ui.sb_x.value())

		self.yIter = floor(int(self.yWidth)/self.ui.sb_step.value())
		self.xIter = floor(int(self.xWidth)/self.ui.sb_step.value())

		nbBlocX = self.xIter/2
		self.speed = self.ui.sb_speed.value()

		gcode = "" 		#All GCode values
		
		#Home
		gcode += "G91\n"
		gcode += "G28 Z F"+str(self.ui.sb_speed.value())+"\n"
		gcode += "G28 X F"+str(self.ui.sb_speed.value())+"\n"
		gcode += "G28 Y F"+str(self.ui.sb_speed.value())+"\n"
		for i in range(0, int(self.ui.sb_passages.value())):
			gcode += "G01 Z"+str(self.ui.sb_axis_z.value())+" F"+str(self.ui.sb_speed.value())+"\n"
			gcode += "G28 Z"+" F"+str(self.ui.sb_speed.value())+"\n"
   
		for xBloc in range(0, int(nbBlocX)):

			#Code bloc	
			for xStep in range(0,int(self.yIter)):
				gcode += "G01 Y"+str(self.ui.sb_step.value())+" F"+str(self.ui.sb_speed.value())+"\n"
				#gcode += "#1=1\n"
				for i in range(0, int(self.ui.sb_passages.value())):
					gcode += "G01 Z"+str(self.ui.sb_axis_z.value())+" F"+str(self.ui.sb_speed.value())+"\n"
					gcode += "G28 Z"+" F"+str(self.ui.sb_speed.value())+"\n"
				
    
			gcode += "G01 X"+str(self.ui.sb_step.value())+" F"+str(self.ui.sb_speed.value())+"\n"
			#gcode += "#1=1\n"
			for i in range(0, int(self.ui.sb_passages.value())):
				gcode += "G01 Z"+str(self.ui.sb_axis_z.value())+" F"+str(self.ui.sb_speed.value())+"\n"
				gcode += "G28 Z"+" F"+str(self.ui.sb_speed.value())+"\n"
			
	
			for xStep in range(0,int(self.yIter)):
				gcode += "G01 Y-"+str(self.ui.sb_step.value())+" F"+str(self.ui.sb_speed.value())+"\n"
				#gcode += "#1=1\n"
				for i in range(0, int(self.ui.sb_passages.value())):
					gcode += "G01 Z"+str(self.ui.sb_axis_z.value())+" F"+str(self.ui.sb_speed.value())+"\n"
					gcode += "G28 Z"+" F"+str(self.ui.sb_speed.value())+"\n"
    
			gcode += "G01 X"+str(self.ui.sb_step.value())+" F"+str(self.ui.sb_speed.value())+"\n"
			#gcode += "#1=1\n"
			for i in range(0, int(self.ui.sb_passages.value())):
				gcode += "G01 Z"+str(self.ui.sb_axis_z.value())+" F"+str(self.ui.sb_speed.value())+"\n"
				gcode += "G28 Z"+" F"+str(self.ui.sb_speed.value())+"\n"

		self.strGCode = gcode
		self.ui.pte_displayGCode.clear()
		self.ui.pte_displayGCode.appendPlainText(self.strGCode)
		self.statusBar().showMessage("Paramètres validés")
  

	def clear(self):

		self.ui.pte_gcodeReturn.clear()

def main():
	
	app = QtWidgets.QApplication(sys.argv) #Creation de l'application
	ihm = MainWindow()                      #Appel de notre classe principale
	ihm.show()                              #Affichage de l'interface
	sys.exit(app.exec_())                   #Loop


if __name__ == "__main__":              
    main()



