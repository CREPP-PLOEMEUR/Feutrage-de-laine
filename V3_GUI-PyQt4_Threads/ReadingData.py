#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import time
exitFlag = 0

class ReadingData (threading.Thread):
	def __init__(self, threadID, name, ):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		
	def initSerial(self, serialObject, commands):
		assert type(commands) is list
		
		self.serialObject = serialObject
		self.commands = commands

		
	def run(self):
		print "Starting " + self.name
		readData(self.serialObject, self.commands)
		print "Exiting " + self.name

def readData(serialObject, commands):
	
	indexCommands = 0
	allCommands = commands
	countCommands = len(allCommands)
	result= ""
	while (True): 	
		#time.sleep(0.01)
		char=serialObject.read() 	#Lecture d'un caractère
		
		if char=='\n': 				#Si retour à la ligne, fin de chaîne
			result=""
		else: 						
			result=result+char		#Concaténation
			if("ok" in result):		#Run next command if available
				
				if(indexCommands+1>=countCommands):
					print("All commands have been called, do nothing")
				else:
					print(">>> Command : "+str(allCommands[indexCommands]))
					#gcodeReturn.appendPlainText(">>> Command : "+str(allCommands[indexCommands]))
					#gcodeReturn.show()
					serialObject.write(allCommands[indexCommands]+"\n")
					indexCommands+=1
					time.sleep(0.050)
				result = ""
		
