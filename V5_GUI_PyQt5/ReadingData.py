#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import time


result = str("")
indexCommands = 0
countCommands = 0
allCommands = []

class ReadingData (threading.Thread):
	"""Class for multithreading"""

	def __init__(self, threadID, name, ):
		"""Constructor of class"""
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.isRunning = True
		
	def initSerial(self, serialObject, commands):
		"""Init serial communication"""
		assert type(commands) is list

		global allCommands
		global countCommands
		global indexCommands

		self.serialObject = serialObject
		allCommands = commands
		indexCommands = 0
		
	def run(self):
		"""Start multithreading"""
		global allCommands
		global countCommands
		print("Starting " + self.name)
		countCommands = len(allCommands)
		while (self.isRunning==True): 	
			readData(self.serialObject)
		#Stop 
		#self.serialObject.write("G28 Z F4\n")
		#print("<stop> ")
		
	def stop(self):
		"""Stop multithreading"""
		self.isRunning = False
		return True
		
	def sendCommand(self, command):
		print("Sending <"+command.replace("\n", "")+"> command...")
		self.serialObject.write(bytes(command, "utf-8"))
		
def readData(serialObject):
	"""Start next command when 'ok' received"""

	global indexCommands
	global countCommands
	global allCommands
	char=serialObject.read() 	#Reading char by char
	if(char==b'<'): 				
		if(indexCommands+1>=countCommands):
			print("All commands have been called, do nothing")
		else:
			print(">>> Command : "+str(allCommands[indexCommands]))
			serialObject.write(bytes(allCommands[indexCommands]+"\n", "utf-8"))
			indexCommands+=1
			time.sleep(0.050)
  

	# elif(char==b'>'):
	# 	print("void")
	# 	result=""
	# else: 	

	# 	result=result+char
	# 	print(result)
		# if("ok" in result):		#Run next command if available
		# 	print("YES")
		# 	print(result)
		# 	print(char)
		# 	if(indexCommands+1>=countCommands):
		# 		print("All commands have been called, do nothing")
		# 	else:
		# 		print(">>> Command : "+str(allCommands[indexCommands]))
		# 		serialObject.write(allCommands[indexCommands]+"\n")
		# 		indexCommands+=1
		# 		time.sleep(0.050)
		# 	result = ""
			
		
