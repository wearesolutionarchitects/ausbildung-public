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

# # Jupter Widgets: Erstelle interaktive Notebooks
# 
# In dieser Lektion lernst du:
# 
# - Wie du Texteingabefelder, Buttons und Slider erstellst
# - Link: https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html#Complete-list

# In[1]:


import ipywidgets as widgets
from IPython.display import display


# In[2]:


widgets.Button(description="Hallo Welt")


# In[3]:


widgets.Text(description="Beschriftung:", value="123")


# In[4]:


widgets.IntText(description="Beschriftung:", value=123)


# In[5]:


widgets.FloatText(description="Beschriftung:", value=123.5)


# In[6]:


widgets.Checkbox(description="Beschriftung:", value=False)


# In[7]:


widgets.RadioButtons(
    options=['München', 'Berlin', 'Köln'],
    description='Welche Stadt?:',
    disabled=False
)


# In[9]:


widgets.Dropdown(
    options=['München', 'Berlin', 'Köln'],
    description='Welche Stadt?:',
    disabled=False
)


