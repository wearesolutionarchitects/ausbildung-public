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

# ## Rechnen mit Datumswerten in Python

# Zur Darstellung von Datumswerten gibt's in Python das datetime - Modul (https://docs.python.org/3/library/datetime.html). Damit kannst du Datumswerte repräsentieren, und damit rechnen.

# In[1]:


from datetime import datetime


# Über `datetime.now()` hast du die Möglichkeit, ein Datumsobjekt zum aktuellen Datum erstellen zu lassen

# In[4]:


now = datetime.now()
print(now)


# Alternativ kannst du auch ein spezifisches Datum angeben (hier: 20.8.2017, 20:00:00).

# In[8]:


day = datetime(2017, 8, 20, 20, 0, 0)
print(day)


# Wenn du ein solches Datumsobjekt erstellt hast, kannst du z.B. über `.year` auf das Jahr direkt zugreifen. Du hast also direkten Zugriff auf alle einzelnen Angaben.

# In[10]:


print(day.year)
print(day.month)
print(day.day)
print(day.hour)
print(day.minute)
print(day.second)


# Die `.timestamp()` - Methode gibt dir den entsprechenden Unix-Timestamp zu einem bestimmten Datumswert zurück. Unix-Timestamp ist einfach nur eine Zahl, die die Sekunden seit dem 01.01.1970 hochzählt.
# 
# Vorteil bei einem Unix-Timestamp ist, dass wir ihn recht kompakt speichern können, intern muss der Computer ja nur eine Zahl speichern, um einen Datumswert zu repräsentieren.
# 
# Wir können ihn hier aber verwenden, um den Zeitunterschied in Sekunden zu berechnen :) 

# In[17]:


print(day.timestamp() - now.timestamp())


# ### `date`- und `time`- Angaben
# 
# Das `datetime` - Paket stellt uns auch weitere Klassen zur Verfügung, die wir verwenden können, um mit Datumsangaben zu arbeiten.
# 
# Beispielsweise repräsentiert `date` eine Datumsangabe, `time` eine Zeitangabe.
# 
# - `datetime`: Datumsangabe + Zeitangabe
# - `date`: Nur Datumsangabe
# - `time`: Nur Zeitangabe

# In[2]:


from datetime import date, time


# In[3]:


d = date(2017, 8, 20)
print(d)


# In[21]:


t = time(20, 1, 4)
print(t)


# Natürlich kannst du auch Datumswerte vergleichen.
# 
# Aber Achtung! Bei `date` ist `==` beim gleichen Datum erfüllt, bei einem `datetime` - Objekt muss natürlich sowohl die Datumsangabe, als auch die Zeitangabe übereinstimmen.
# 
# Ausführlich also:
# 
# 
# - `datetime`: Datumsangabe + Zeitangabe müssen übereinstimmen
# - `date`: Datumsangabe muss übereinstimmen
# - `time`: Zeitangabe muss übereinstimmen

# In[26]:


print(date(2017, 8, 20) == date(2017, 8, 20))
print(datetime(2017, 8, 20, 20, 0, 0) == datetime(2017, 8, 20, 15, 0, 0))


# ### `datetime` in `date` und `time` umwandeln
# 
# Natürlich kannst du ein `datetime` - Objekt auch in ein `date` und ein `time` - Objekt zerlegen:

# In[28]:


dt = datetime(2017, 8, 20, 20, 0, 0)
print(dt.time())
print(dt.date())


# ### `date` und `time` in `datetime` umwandeln
# 
# Und natürlich geht das auch anders herum :)

# In[30]:


print(datetime.combine(date(2017, 8, 20), time(20, 30, 0)))


