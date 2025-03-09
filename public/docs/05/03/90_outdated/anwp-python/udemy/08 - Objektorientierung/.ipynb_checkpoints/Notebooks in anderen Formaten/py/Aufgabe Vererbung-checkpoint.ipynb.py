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

# ## Aufgabe: Vererbung
# 
# #### Aufgabe 1:
# 
# Vervollständige die Klasse "FileReader" so, dass bei Aufruf der lines() - Methode die Datei Zeile für Zeile eingelesen wird. Die lines() - Methode soll dann eine Liste der Zeilen in der Datei zurückgeben.
# 
# #### Aufgabe 2:
# 
# Erstelle die Klasse "CsvReader", sodass der "FileReader" erweitert wird. Bei Aufruf der lines() soll die Datei als .csv - Datei eingelesen werden, sprich es soll eine mehrdimensionale Liste zurückgegeben werden. 
# 
# **Wichtig:** Überlass' das Einlesen der Datei dem "FileReader", und erweitere die lines() - Methode im Csv-Reader um die Funktionalität, die benötigt wird, damit die mehrdimensionale Liste zurückgegeben wird. 

# In[1]:


class FileReader():
    pass


# In[ ]:


f = FileReader("./datei.csv")
print(f.lines())

# Hier soll ausgegeben werden:
# ["Nachname,Vorname", "Mustermann,Max", "Mueller,Monika"]


# In[ ]:


f = CsvReader("./datei.csv")
print(f.lines())

# Hier soll ausgegeben werden:
# [["Nachname", "Vorname"], ["Mustermann", "Max"], ["Mueller", "Monika"]]


