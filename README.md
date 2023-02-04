# Feutrage-de-laine

Un projet pour une machine à feutrer la laine

## Installations Outils Python 2.7

Le code a été exécuté sur une machine Ubuntu 18.04 car la communication série entre la CNC et l'ordinateur n'était pas fonctionnelle en version 3.X de Python,
que ce soit avec la bibliothèque QtSerial ou PySerial sous version 3.X. 

La version 2.X de Python permet la communication avec la bibliothèque Pyserial.

```
sudo apt install python-pip
sudo apt-get install python-qt4
sudo apt-get install pyqt4-dev-tools 
pip install serial
sudo apt-get install qt4-designer
```

## Conversion de l'interface UI en code Python

Cette commande est à réaliser à chaque modification de l'interface graphique (éditée via QtCreator)
```
pyuic4 -x GUI.ui -o GUI.py
```


Le dossier V4_GUI_PyQt4 contient le code source pour l'Interface PyQt4


## Lancement de l'interface

```
python GUIMain.py
```
