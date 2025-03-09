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

# # Daten umwandeln - Strings und Zahlen
# 

# ### Einen String in eine Ganzzahl umwandeln
# Dazu wenden wir den **int()**-Befehl auf einen String (direkt oder in einer Variable gespeichert) an: **int(string)**
# 
# int steht für Integer, den englischen Begriff für Ganzzahl.

# In[1]:


a = "5"
b = "6"

print(int(a) + int(b))


# ### Einen String in eine Kommazahl umwandeln
# Dazu wenden wir den **float()**-Befehl auf einen String (direkt oder in einer Variable gespeichert) an: **float(string)** 
#  
#  
# Der Name float kommt daher, dass man Kommazahlen auch Fließkommazahlen nennt.

# In[1]:


a = "5.5"
b = "6.6"

print(float(a) + float(b))


# ### Eine Zahl in einen String umwandeln
# Dazu wenden wir den **str()**-Befehl auf eine Ganzzahl oder Kommazahl an (direkt oder in einer Variable gespeichert): **str(zahl)**

# In[3]:


age = 21
print("Ich bin " + str(age) + " Jahre alt")


# ### Spiel doch jetzt ein wenig herum mit dem was du gelernt hast :-) 
# 
# - wandle Zahlen in Strings um und gebe sie als Teil eines verketteten Strings aus
# - wandle Strings in Zahlen um, mit denen du dann rechnen kannst 
# 
# 

