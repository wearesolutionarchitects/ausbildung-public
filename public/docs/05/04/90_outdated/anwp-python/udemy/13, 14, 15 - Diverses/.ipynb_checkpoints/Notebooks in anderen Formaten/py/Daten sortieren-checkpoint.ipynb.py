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

# ## Daten sortieren
# 
# Oft hast du das Problem, dass du z.B. eine Liste sortieren möchtest. Python stellt hier bereits eine fertige Funktion zur Verfügung, die wir aber korrekt ansteuern möchten.
# 
# In dieser Lektion lernst du:
# 
# - Wie du Daten in Python sortieren kannst
# - Und die Sortierung beeinflussen kannst

# In[1]:


l = ["Max", "Monika", "Erik", "Franziska"]
l.sort()
print(l)


# In[2]:


l = ["Max", "Monika", "Erik", "Franziska"]
l.sort(reverse=True)
print(l)


# #### Eine eigene Funktion übergeben

# In[5]:


def get_length(item):
    return len(item)
l = ["Max", "Monika", "Erik", "Franziska"]
l.sort(key=get_length)
print(l)


# #### Aber... len(item) ist ja auch eine Funktion!

# In[6]:


l = ["Max", "Monika", "Erik", "Franziska"]
l.sort(key=len)
print(l)


# #### Die Daten sind nicht immer eine Liste!

# In[10]:


d = {"Köln": "CGN", "Budapest": "BUD", "Saigon": "SGN"}

print(sorted(d, reverse = True))


# In[11]:


l = ["Max", "Monika", "Erik", "Franziska"]
l.sort()
print(l)


# In[13]:


l = ["Max", "Monika", "Erik", "Franziska"]
l2 = sorted(l)
print(l)
print(l2)


