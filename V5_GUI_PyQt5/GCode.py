#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import floor

import serial
import time

ser = serial.Serial( '/dev/ttyACM0', 115200,serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=0.1)
ser.flushInput()

if(open):
    print("Communication fonctionnelle !")
else:
    print("Mauvaise communication")

decalagePas = 8 #moitie du porte outil en mm

yWidth = input("Quelle est la longueur du plateau ? (mm) : ")
xWidth = input("Quelle est la largeur du plateau ? (mm) : ")

yIter = floor(int(yWidth)/8)
xIter = floor(int(xWidth)/8)

nbBlocX = xIter/2
deplacementZ = 10 #mm
vitesse=4 #max 6

print("Nombre d'arret sur X : "+str(xIter))
print("Nombre d'arret sur Y : "+str(yIter))

def sendCommand(command):
	print("Commande : "+str(command))
	ser.write(command+'\n')
	result=""
	waitingOK = True
	while (waitingOK==True): # tant que au moins un caractère en réception
		char=ser.read() # on lit le caractère
		if char=='\n': # si saut de ligne, on sort du while
			result=""
		else: #tant que c'est pas le saut de ligne, on l'ajoute à la chaine 
			result=result+char	
			if(result=="<ok>"):
				print("Commande valide")
				waitingOK = False


#Init
print("Mode relatif")
sendCommand("G91") #Mode relatif

#Retour Home
print("Retour origine")
sendCommand("G28 X")
sendCommand("G28 Y")


#Generation du GCode
gcode =""
for xBloc in range(0, int(nbBlocX)):
	#Code bloc
	
	for xStep in range(0,int(yIter)):
		gcode += "G01 Y"+str(decalagePas)+" F4"+"\n"
		gcode += "G04 P0.1"+"\n"
	
	gcode += "G01 X"+str(decalagePas)+" F"+str(vitesse)+"\n"
	
	for xStep in range(0,int(yIter)):
		gcode += "G01 Y-"+str(decalagePas)+" F4"+"\n"
		gcode += "G04 P0.1"+"\n"
	
	gcode += "G01 X"+str(decalagePas)+" F"+str(vitesse)+"\n"
	

print(gcode)

allCommands = gcode.split("\n")
print("Nombre d'instructions a executer :" +str(len(allCommands)))

for line in allCommands:
	sendCommand(line)
	


