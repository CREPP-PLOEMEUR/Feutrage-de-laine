#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import time


result = str("")
indexCommands = 0
countCommands = 0
allCommands = []
i=0

class ReadingData (threading.Thread):
	"""Class for multithreading"""

	def __init__(self, threadID, name, currentIndexDefault=0):
		"""Constructor of class"""
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.isRunning = True
		self.isWorking = False
		self.cycleIsOver = False
  
		#ProgressBar
		self.progressBar = None
		self.statusBar = None

		#After resume
		self.currentIndexCommand = currentIndexDefault
		self.currentCommand = ""

	def addProgressBar(self, progressBar):

		self.progressBar = progressBar
  
	def addStatusBar(self, statusBar):
		self.statusBar = statusBar

	def initSerial(self, serialObject, commands):
		"""Init serial communication"""
		assert type(commands) is list

		global allCommands
		global countCommands
		global indexCommands

		self.serialObject = serialObject
		allCommands = commands
		indexCommands = self.currentIndexCommand
		#resume
		if(self.currentIndexCommand!=0):
			print("Start command to go home")
			self.sendCommand(commands[self.currentIndexCommand])
		
	def run(self):
		"""Start multithreading"""
		global allCommands
		global countCommands
		self.isWorking = True
		countCommands = len(allCommands)
		while (self.isRunning==True): 	
			self.currentIndexCommand  = readData(self.serialObject, self)
			self.currentCommand = allCommands[self.currentIndexCommand]
			if(countCommands!=0):
				self.progressBar.setValue(int((1+self.currentIndexCommand)/countCommands*100))
				self.progressBar.show()
			if(self.currentIndexCommand==-1):
				self.cycleIsOver = True

		
	def stop(self):
		"""Stop multithreading"""
		self.isRunning = False
		self.isWorking = False
		self.isStopped = True
		return True
		
	def sendCommand(self, command):
		"""Initial command to start ps"""
		self.statusBar.showMessage("Commande <"+str(command.replace("\n", ""))+"> en cours")
		self.serialObject.write(bytes(command, "utf-8"))
		print("Commande <"+str(command.replace("\n", ""))+"> en cours")

	def reset(self):
		global indexCommands
		indexCommands = 0
		global countCommands
		countCommands = 0
		self.currentIndexCommand = 0
 
def readData(serialObject, readingData):
	"""Start next command when 'ok' received and return -1 when finished"""

	global indexCommands
	global countCommands
	global allCommands
	char=serialObject.read() 	#Reading char by char
	if(char==b'<'): 				
		if(indexCommands+1>=countCommands):
			return -1
		else:
			readingData.sendCommand(allCommands[indexCommands]+"\n")
			#serialObject.write(bytes(allCommands[indexCommands]+"\n", "utf-8"))
			indexCommands+=1
			time.sleep(0.050)
   
	return indexCommands
