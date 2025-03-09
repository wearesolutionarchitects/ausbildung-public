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

# ## Quiz: String-Formatierung

# #### Aufgabe 1
# 
# Mit welchem Befehl wandelst du den String s = `"WeR sO sChReIbT, hAt SiE nIcHt MeHr AlLe"` in einen String um, in dem jeder Buchstabe kleingeschrieben ist?
# 
# - A) `s.toLower()`
# - B) `s.lower()`
# - C) `s.low()`
# - D) `s.small`

# Richtige Lösung: 

# #### Aufgabe 2
# 
# Wie entfernst du die Leerzeichen am Anfang und Ende und die Punkte aus dem String s = `"       ... ein Gedanke...  "`, sodass du den String `"ein Gedanke"` erhälst?
# 
# 
# - A) `s.strip("...")`
# - B) `s.strip()`
# - C) `s.strip(" .")`
# - D) `s.strip(" ", ".")`

# Richtige Lösung: 

# #### Aufgabe 3
# 
# Wie änderst du den String s = `"Morgen werde ich so richtig produktiv sein"` in `"Heute werde ich so richtig produktiv sein"`?
# 
# ```python
# s = "Morgen werde ich so richtig produktiv sein"
# ```
# 
# 
# - A) `s.replace("Morgen", "Heute")`
# - B) `s.replace("Heute", "Morgen")`
# - C) `"Morgen".replace("Heute")`
# - D) `s.replace(s.find("Morgen"), "Heute")`

# Richtige Lösung: 

# #### Aufgabe 4
# 
# Wie formatierst du einen String, um den folgenden Satz auszugeben?:
# 
# `"40.000 Zuschauer bejubelten den 3:1-Sieg in der Sponsoring-Arena."`
# 
# - A) `number + " Zuschauer bejubelten den " + result +"-Sieg " + stadium + ".".format(result = "3:1", stadium = "in der Sponsoring-Arena", number = "40.000")`
# - B) `"{1} Zuschauer bejubelten den {0}-Sieg {2}.".format("in der Sponsoring-Arena", "40.000", "3:1")`
# - C) `"{0} Zuschauer bejubelten den {2}-Sieg {1}.".format("3:1", "in der Sponsoring-Arena", "40.000")`
# - D) `"{number} Zuschauer bejubelten den {result}-Sieg {stadium}.".format(result = "3:1", stadium = "in der Sponsoring-Arena", number = "40.000")`

# Richtige Lösung: 

