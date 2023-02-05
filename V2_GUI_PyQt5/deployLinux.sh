#!/bin/bash
appName="CNC_Feutrage"
appSource="FeutrageGUIMain.py"
pyinstaller --onefile --name "$appName" "$appSource"
