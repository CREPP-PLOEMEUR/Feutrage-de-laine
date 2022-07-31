# Feutrage-de-laine

Un projet pour une machine à feutrer la laine

## Installations

```
sudo apt-get install pyqt5-dev-tools
sudo apt-get install python3-pyqt5
sudo apt-get install python3-pyqt5.qtserialport
```

## Conversion de l'interface UI en code Python

Cette commande est à réaliser à chaque modification de l'interface graphique.
```
pyuic5 -x FeutrageGUI.ui -o FeutrageGUI.py
```


Le dossier FeutrageGUI contient le code source pour l'Interface PyQt5


## Lancement de l'interface

```
python3 FeutrageGUIMain.py
```
