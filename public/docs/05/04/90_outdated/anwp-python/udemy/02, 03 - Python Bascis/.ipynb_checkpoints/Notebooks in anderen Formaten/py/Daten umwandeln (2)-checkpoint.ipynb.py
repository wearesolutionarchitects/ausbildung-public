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

# # Daten umwandeln - Listen und Strings
# Wir können mit Python Elemente zu einer Liste zusammenfügen oder eine Liste in einzelne Elemente zerlegen.

# ### Strings aus einer Liste zu einem String zusammenfügen
# 
# Mit dem  **join()**-Befehl, der auf einen String angewendet wird, verbinden wir die Strings aus einer Liste zu einem neuen String: **string.join(liste)**
# 
# Der String, auf den join() angewendet wird, bildet dabei die Nahtstelle: dieser String wird als Verbindung zwischen den einzelnen Listenelementen im neuen String gesetzt.

# In[2]:


students = ["Max", "Monika", "Erik", "Franziska"]
print(", ".join(students))


# In[1]:


students_as_string = ", ".join(students)
print("An unserer Uni studieren: " + students_as_string)


# In[1]:


students = ["Max", "Monika", "Erik", "Franziska"]
print(" - ".join(students))


# ### Einen String in eine Liste aufspalten
# 
# Mit dem **split()**-Befehl, der auf einen String angewendet wird, wird dieser String an seinen Leerzeichen aufgespalten und die daraus resultierenden Einzelstrings in einer Liste gespeichert: **string.split()**

# In[3]:


i = "Max, Monika, Erik, Franziska"


# In[10]:


print(i.split())


# Wir können sogar noch genauer festlegen, an welchen Stellen der String von split() aufgespaltet werden soll.

# In[4]:


print(i.split(", "))


# In[5]:


print(i.split("a"))


# Insbesondere können wir auch mehrere der Befehle, die wir schon kennen gelernt haben, miteinander kombinieren:

# In[1]:


# Hier zählen wir die Anzahl der Wörter des Satzes s

s = "Ich bin ein Satz mit vielen Wörtern"
print(len(s.split()))


# ### Spiel doch jetzt ein wenig herum mit dem was du gelernt hast:
# - Zerlege Strings in Listen mit split() und erzeuge eine Liste aus einzelnen Strings per join() :-)
# - Du kannst auch versuchen, die Funktionen miteinander zu kombinieren, die du schon kennst :-)

# In[ ]:







