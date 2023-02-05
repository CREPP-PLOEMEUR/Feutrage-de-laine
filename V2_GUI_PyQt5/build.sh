#!/bin/bash

echo "Generating Resource file..."
outputFile="resources.qrc"
imgDir="img"
appBaseName="FeutrageGUI"

echo "<!DOCTYPE RCC>" > $outputFile
echo "<RCC version=\"1.0\">" >> $outputFile
echo -e "\t<qresource prefix=\"icon\">" >> $outputFile
for i in $(ls $imgDir);do
    echo -e  "\t\t<file alias=\"$i\">$imgDir/$i</file>" >> $outputFile
done

echo -e "\t</qresource>" >> $outputFile
echo "</RCC>" >> $outputFile
pyrcc5 resources.qrc -o resources.py
echo "Generating Resource file : [OK]"
echo "Exec < pyuic5 -x "$appBaseName".ui -o "$appBaseName.py" >"
pyuic5 -x "$appBaseName".ui -o "$appBaseName.py"