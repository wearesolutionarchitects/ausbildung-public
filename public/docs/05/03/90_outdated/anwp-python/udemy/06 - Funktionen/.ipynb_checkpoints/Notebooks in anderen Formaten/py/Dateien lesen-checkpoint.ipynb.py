# Diese .py - Datei wurde automatisch aus dem IPython - Notebook (.ipynb) generiert.
# 
# Gelegentlich wurde ich von Teilnehmern gefragt, ob ich die Kursmaterialien nicht 
# auch als normale .py - Datien bereitstellen könne. Dadurch ist es möglich, den Code
# ohne Jupyter zu öffnen, beispielsweise wenn Python-Programme in einem Terminal oder in 
# Eclipse entwickelt werden.
# 
# Dem möchte ich hiermit nachkommen. Ich empfehle dir aber trotzdem, schau' dir lieber die
# IPython - Notebooks direkt an, oder den HTML-Export eben dieser. Dieser reine .py-Export
# ist meiner Meinung nach etwas unübersichtlich.

# coding: utf-8

# # Eine txt-Datei lesen und ihren Inhalt ausgeben

# In[1]:


# Wir öffnen die Datei lesen.txt zum Lesen ("r") und speichern ihren Inhalt in die Variable file
file = open("lesen.txt", "r")

# Wir gehen alle Zeilen nacheinander durch
# In der txt-Datei stehen für uns nicht sichtbare Zeilenumbruchszeichen, durch die jeweils das Ende einer Zeile markiert ist
for line in file:
    # Eine Zeile ohne Zeilenumbruch ausgeben
    print(line.strip())


