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

# ## Datumswerte ausgeben
# 
# Wir haben uns jetzt schon angeschaut, wie wir Datumswerte vergleichen konnten.
# 
# In dieser Lektion lernst du:
# 
# - Wie du Datumswerte korrekt ausgeben kannst
# 
# Dokumentation: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

# In[1]:


from datetime import datetime

now = datetime.now()


# In[2]:


print(now)


# In[11]:


print(now.strftime("%d.%m.%Y"))
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%Y%m%d"))


# ### Datumswerte einlesen
# 
# Das ganze funktioniert auch anders herum: Du kannst auch Datumswerte aus einem String extrahieren, wenn du z.B. mit den Python - Funktionen später mit dem Datum weiter rechnen willst.

# In[13]:


d = "18.07.2017"


# In[15]:


print(datetime.strptime(d, "%d.%m.%Y"))


