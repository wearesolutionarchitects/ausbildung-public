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

# ## Mit Strings arbeiten
# 
# In Python musst du oft mit Strings (Zeichenketten) arbeiten. In dieser Lektion zeige ich dir weitere Funktionen, die du immer mal wieder brauchst, wenn du mit denen rumhantierst.

# Mit der `.upper()` bzw. `.lower()` - Methode kannst du dafür sorgen, dass alle Zeichen in Groß- bzw. Kleinbuchstaben angezeigt werden.

# In[6]:


w = "Hallo"
print(w.upper())
print("Hallo".upper())


# In[7]:


w = "Hallo"
print(w.lower())
print("Hallo".lower())


# Mit der `.startswith()` bzw. `.endswith()` - Methode kannst du prüfen, ob ein String mit einem anderen String beginnt / aufhört:

# In[12]:


sentence = "Ist das Wetter heute gut???"

if sentence.endswith("???"):
    print("Der Satz endet mit drei Fragezeichen")
    
if sentence.startswith("Ist"):
    print("Der Satz beginnt mit einem 'ist'")


# ### Die `.strip()` - Methode
# 
# Standardmäßig entfernt die `.strip()` - Methode Leerzeichen vom Anfang und vom Ende des Strings.

# In[1]:


"   Hallo Welt.    ".strip()


# Du kannst der `strip()` - Methode aber auch als Parameter übergeben, welche Zeichen entfernt werden sollen. Hier in den nächsten Beispielen sagen wir z.B., dass nur Unterstrichte und Punkte entfernt werden sollen.
# 
# Die `.lstrip()` bzw. `.rstrip()` - Methode funktioniert analog der `.strip()` - Methode, wobei aber `.lstrip()` nur die linke Seite und `.rstrip()` nur die rechte Seite betrachtet:

# In[23]:


word = "____Hallo.__"
print(word.strip("_."))
print(word.lstrip("_"))
print(word.rstrip("_"))

sentence = "Ist das Wetter heute, und morgen gut???"
print(sentence.rstrip("!?.,"))


# ### Die `.find()` - Methode
# 
# Mit der `.find()` - Methode kannst du herausfinden, an welcher Stelle ein Zeichen in einem String vorkommt. Beispielsweise können wir so herausfinden, dass das Komma an der 21. Stelle (Position 20 also) vorkommt.
# 
# Wenn die `.find()` - Methode die Zahl `-1` zurückgibt, bedeutet dass, dass das Zeichen im String nicht vorkommt.

# In[26]:


sentence = "Ist das Wetter heute, und morgen gut???"
print(sentence.find(","))
print(sentence.find("!"))


# ### Zeichen ersetzen (`.replace()`)
# 
# Mit der `.replace()` - Methode kannst du eine Ersetzung durchführen. Beispielsweise kannst du so z.B. das Komma durch ein Semikolon ersetzen lassen, etc.

# In[29]:


sentence = "Ist das Wetter heute, und morgen gut???"

print(sentence.replace(",", ";"))
print(sentence.replace("u", "ü"))
print(sentence.replace("und", "oder"))


