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

# # Übung Exceptions
# 
# Viel Erfolg bei diesen Übungsaufgaben :)
# 
# Wenn du mit diesem Übungsblatt fertig bist, kannst du deine Lösung mit der Musterlösung in Textform (Datei: `Uebung Exceptions (Musterloesung)`) vergleichen. 
# 
# Die Video - Musterlösung (in der nächsten Lektion) ist besonders ausführlich gehalten. Wenn du alles richtig gelöst hast, ist es vollkommen okay, wenn du diese Lektion dann überspringst.

# ### Aufgabe
# 
# Deine Zeit im Online-Shop der Mathemagierin neigt sich dem Ende entgegen - du bist bereit für größere Aufgaben! Doch du solltest zuvor noch sicherstellen, dass auch weniger kompetente Anwender deines Codes den Shop nicht ins Verderben führen werden...

# **a.)** 
# 
# Schreibe eine Exception, die den Fehler abfängt, wenn jemand versucht die folgende Datei zu öffnen, die nicht in diesem Verzeichnis existiert. Gebe in dem Fall die Nachricht "Datei wurde nicht gefunden" aus. Achte auch darauf, die Datei mit einem geeigneten Konstrukt zu öffnen, falls sie zukünftig doch existieren sollte - ohne dass es dann zu Fehlern kommen kann, weil die Datei nicht richtig geschlossen würde.

# In[2]:


# hier kommt dein Code hin

file = open("nicht_oeffnen.txt", "r")
print(file)


# **b.)**
# 
# Schaue dir an, welcher Fehlertyp bei der Ausführung des folgenden Code auftritt. Fange den Fehler mit **try except** ab und gebe eine passende Fehlermeldung aus.

# In[4]:


articles = ["Unsichtbare Tastatur", "Holographisches Display", "Endlosschleifenschneider"]

prices = {"Unsichtbare Tastatur": 150, "Holographisches Display": 1150}

def print_prices():
    for article in articles:
        print(prices[article])

print_prices()


# Erwartete Ausgabe:
# 
# ```
# 150
# 1150
# key fehlt im dictionary
# ```

# **c.)** 
# 
# Zuletzt erstellst du noch eine Fehlerklasse, die aufgerufen wird, wenn es sich bei d um ein leeres dictionary handelt. Dann soll ein `EmptyDictionaryError` auftreten mit dem Hinweis, dass das dictionary d kein Element enthält.

# In[1]:


d = {}

if len(d) == 0:
    print("Hier soll jetzt ein Fehler ausgelöst werden")
# hier kommt dein Code hin


# Erwartete Ausgabe:
# 
# ```
# ---------------------------------------------------------------------------
# EmptyDictionaryError                      Traceback (most recent call last)
# <ipython-input-7-75e49afb1af6> in <module>()
#       5 
#       6 if len(d) == 0:
# ----> 7     raise EmptyDictionaryError("d enthält kein Element")
# 
# EmptyDictionaryError: d enthält kein Element
# ```
# 

# ### Gut gemacht! :-)

