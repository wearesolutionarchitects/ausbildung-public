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

# # Trump - Twitter - Bot
# In dieser Lektion bauen wir einen Text-Generator, der zufällig generierte Tweets ausgibt :-)

# ### Exkurs: Zufallszahlen
# Wir können in Python mit der **randint()**-Funktion zufällige Zahlen generieren. Doch um auf diese Funktion zurückzugreifen, müssen wir erst das random-Modul einbinden. :-)

# In[5]:


import random


# randint liefert zufällig Ganzzahlen aus einem Intervall, das wir der Funktion mitteilen müssen. Die beiden Grenzen und alle ganzen Zahlen innerhalb des Intervalls können dabei Werte von randint sein.

# In[58]:


print(random.randint(0, 4))


# In[59]:


print(random.randint(0, 4))


# ### Listen mit den Begriffen für unsere Tweets anlegen
# 
# Hier haben wir einfach mal ein paar häufig auftretende Begriffe aus den Tweets kopiert ;-)

# In[60]:


part1 = ["Putin,", "Hillary,", "Obama", "Fake News,", "Mexico,", "Arnold Schwarzenegger", "The Democrats"]
part2 = ["no talent,", "on the way down,", "really poor numbers,", "nasty tone,", "looking like a fool,", "bad hombre,"]
part3 = ["got destroyed by my ratings.", "rigged the election.", "had a much smaller crowd.", "will pay for the wall."]
part4 = ["So sad", "Apologize", "So true", "Media won't report", "Big trouble", "Fantastic job", "Stay tuned"]


# In[61]:


# Wir können auch Listen von Listen erstellen!
best_words = [part1, part2, part3, part4]
print(best_words)


# ### Den Tweet-Generator bauen

# In[76]:


sentence = []

for part in best_words:
    r = random.randint(0, len(part) - 1)
    sentence.append(part[r])

print(" ".join(sentence) + "!")


# ### Jetzt kannst du versuchen, den Tweet Generator zu erweitern. :-)

