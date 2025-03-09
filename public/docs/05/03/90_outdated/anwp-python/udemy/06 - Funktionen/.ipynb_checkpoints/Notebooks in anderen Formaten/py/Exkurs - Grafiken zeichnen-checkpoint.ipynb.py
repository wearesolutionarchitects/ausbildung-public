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

# ## Exkurs: Grafiken zeichnen
# 
# In dieser Lektion lernst du, wie du schicke Grafiken zeichnen kannst.
# 
# ### Schritt 1: Modul `matplotlib` einbinden + konfigurieren

# In[1]:


import matplotlib.pyplot as plt


# ### Schritt 2: Grafik zeichnen

# In[5]:


xs = [1, 2, 5]
ys = [4, 7, 5]

plt.plot(xs, ys)
plt.show()


