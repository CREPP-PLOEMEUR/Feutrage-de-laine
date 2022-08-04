# Feutrage-de-laine

Un projet pour une machine à feutrer la laine

## Installations Outils Python 2.7

```
sudo apt install python-pip
sudo apt-get install python-qt4
sudo apt-get install pyqt4-dev-tools 
pip install serial
sudo apt-get install qt4-designer
```

## Conversion de l'interface UI en code Python

Cette commande est à réaliser à chaque modification de l'interface graphique.
```
pyuic4 -x GUI.ui -o GUI.py
```


Le dossier GUI contient le code source pour l'Interface PyQt4


## Lancement de l'interface

```
python GUIMain.py
```
