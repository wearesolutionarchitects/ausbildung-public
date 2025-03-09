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

# ## Quiz: Datumsfunktionen

# #### Aufgabe 1
# 
# Wie ermittelst du mithilfe des `datetime`-Objektes aus dem `datetime`-Modul das aktuelle Datum inkl. Uhrzeit?
# 
# ```python
# from datetime import datetime
# ```
# 
# - A) `datetime.now()`
# - B) `datetime.jetzt()`
# - C) `datetime.daytime()`
# - D) `date.now(time)`

# Richtige Lösung: 

# #### Aufgabe 2
# 
# Wie erstellst du ein datetime-Objekt für das exakte Datum: `01.04.2018, 06:58:47`?
# 
# ```python
# from datetime import datetime
# ```
# 
# - A) `datetime(47, 58, 6, 1, 4, 2018)`
# - B) `datetime(6, 58, 47, 1, 4, 2018)`
# - C) `datetime(2018, 4, 1, 6, 58, 47)`
# - D) `date = (47, 58, 6, 1, 4, 2018)`

# Richtige Lösung: 

# #### Aufgabe 3
# 
# Wie erstellt du für das `datetime`-Objekt `day`, das per `day = datetime.now()` erzeugt wurde, eine Datumsanzeige in der folgenden Gestalt?:
# 
# `Monday, 12th of January`
# 
# ```python
# from datetime import datetime
# 
# day = datetime.now()
# ```
# 
# Schau zur Erinnerung hier nach: https://docs.python.org/3.6/library/time.html
# 
# - A) `day.strftime("%A, %dth of %B")`
# - B) `day.strftime("%D, %dth of %M")`
# - C) `day.strftime("%a" + ", " + "%D" + "th of " + "%M")`
# - D) `day.strptime("%W, %D th of %M")`

# Richtige Lösung: 

