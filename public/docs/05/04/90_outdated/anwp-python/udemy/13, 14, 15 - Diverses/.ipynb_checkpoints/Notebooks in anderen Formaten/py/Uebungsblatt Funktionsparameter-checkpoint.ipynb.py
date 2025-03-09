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

# # Übungsblatt Funktionsparameter & Sortierfunktionen
# 
# In diesem Übungsblatt habe ich ein paar Aufgaben für dich vorbereitet. Viel Spaß bei diesen Übungen :)
# 
# Wenn du mit diesem Übungsblatt fertig bist, kannst du deine Lösung mit der Musterlösung in Textform (Datei: `Uebungsblatt Funktionsparameter (Musterloesung)`) vergleichen. 
# 
# Die Video - Musterlösung (in der nächsten Lektion) ist besonders ausführlich gehalten. Wenn du alles richtig gelöst hast, ist es vollkommen okay, wenn du diese Lektion überspringst :)

# ### Aufgabe 1
# 
# Vervollständige die Funktion `shortest_word()`: Ihr sollen mehrere Strings übergeben werden (KEINE Liste von Strings!), von denen sie den String mit den wenigsten Zeichen zurückliefert.
# 
# Hinweis: Benutze variable Parameter (mit Sternchen `*` oder doppelten Sternche `**`)

# In[39]:


def shortest_word():
    # Ersetze pass durch deinen Code
    pass
    
print(shortest_word("Max", "Moritz", "Monika", "Tim", "Jo"))


# Erwartete Ausgabe:
# 
# ```
# Jo
# ```

# ### Aufgabe 2

# **a.)**
# 
# Sortiere die Tupel in der Liste `tupels` aufsteigend nach ihrer Summe.
# 
# **Hinweis:**  Schreibe dazu zuerst eine normale Funktion, und löse die Aufgabe anschließend nochmal mit einer lambda - Funktion.

# In[91]:


tupels = [(10, 2), (4, 1), (0, 17), (3, 3), (5, 7), (11, 3)]

# hier kommt dein Code hin

print(tupels)


# Erwartete Ausgabe (braucht nicht farbig zu sein):
# 
# ```python
# [(4, 1), (3, 3), (10, 2), (5, 7), (11, 3), (0, 17)]
# ```

# **b.)** 
# 
# Sortiere die Liste `names` mit Namen nach dem Nachnamen. Du kannst annehmen, dass alle Namen in der Liste nur einen Vornamen enthalten. Das Format der Namen ist immer "Vorname Nachname".
# 
# Überlege dir dazu zuerst, wie du den Nachnamen ermittelst, und schreibe dann die entsprechende Funktion, die du der `.sort()` - Funktion übergibst.
# 
# **Hinweis:**  Schreibe dazu zuerst eine normale Funktion, und löse die Aufgabe anschließend nochmal mit einer lambda - Funktion.

# In[3]:


names = ["Elif Else", "Sebastian Klarnamen", "Anna Boa", "Anton Adel", "Conny Coder", "Anne Wortmann", "Willy Cordes"]

# hier kommt dein Code hin

print(names)


# Erwartete Ausgabe:
# 
# ```python
# ['Anna Boa', 'Conny Coder', 'Willy Cordes', 'Elif Else', 'Sebastian Klarnamen', 'Anton Adel', 'Anne Wortmann']
# ```

# **c.)**
# 
# Sortiere die Liste `sentences` absteigend nach der Anzahl der Wörter, die ein Element aus `sentences` jeweils enthält. Du kannst annehmen, dass in den Sätzen alle Wörter ordnungsgemäß mit Leerzeichen voneinander getrennt sind. :-)
# 
# Überlege dir dazu zuerst, wie du die Anzahl Wörter in einem Satz ermitteln kannst.
# 
# **Hinweis:**  Schreibe dazu zuerst eine normale Funktion, und löse die Aufgabe anschließend nochmal mit einer lambda - Funktion.

# In[56]:


sentences = ["Sie liefen weiter den Strand entlang.", "Der Hund bellte laut.", "Er rutschte aus.", "Sie lachte."]

# hier kommt dein Code hin

print(sentences)


# Erwartete Ausgabe:
# 
# ```python
# ['Sie liefen weiter den Strand entlang.', 'Der Hund bellte laut.', 'Er rutschte aus.', 'Sie lachte.']
# ```

# ### Zusatzaufgabe (schwer)
# 
# Verändere den folgenden Code, sodass die Liste `l` nicht mehr innerhalb der Funktion `make_row()` überschrieben wird. Die Liste, die `make_row()`ausgibt soll also identisch mit der bisherigen sein, `l` soll aber am Ende in seiner ursprünglichen Form ausgegeben werden.

# In[127]:


l = ["o", "x", "o"]

def make_row(row):
    # hier kommt dein Code hin
    row[2] = "x"
    print(row)
    
make_row(l)
print(l)


# Erwartete Ausgabe:
# 
# ```python
# ['o', 'x', 'x']
# ['o', 'x', 'o']
# ```

