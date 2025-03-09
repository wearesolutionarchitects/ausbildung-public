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

# # Abschluss Python Grundlagen (Musterlösung)
# 
# Nehme dir die Zeit, um die Aufgaben sorgfältig zu bearbeiten. Viel Erfolg! :)
# 
# Wenn du mit diesem Übungsblatt fertig bist, kannst du deine Lösung mit der Musterlösung in Textform (Datei: `Abschluss Python Grundlagen (Musterloesung)`) vergleichen. 
# 
# Die Video - Musterlösung (in der nächsten Lektion) ist besonders ausführlich gehalten. Wenn du alles richtig gelöst hast, ist es vollkommen okay, wenn du diese Lektion dann überspringst.

# ### 1.) Ein automatisierter Trick
# 
# #### a.) 
# Eine Mathemagierin bittet dich darum einen ihrer Tricks durch ein kleines Programm zu automatisieren. Der Trick beginnt wie folgt: 
# 
# 1. Denke dir eine Zahl aus (Variable `number`)
# 2. Multipliziere sie mit 2
# 3. Addiere 10 zum Ergebnis
# 4. Teile das Ergebnis durch 2
# 
# Führe diese Rechnung  für die Variable _number_ durch und gebe das Ergebnis aus. 

# In[1]:


number = 6

# Schreibe die Berechnung in folgende Zeile
result = 0

print(result)


# Korrekte Ausgabe (braucht nicht farbig zu sein):
# 
# ```python
# 11.0
# ```
# 

# ####  b.) 
# Als sie das sieht, rümpft die Mathemagierin die Nase: Das Ergebnis wird nämlich noch als Kommazahl angezeigt. 
# 
# Wandle das Ergebnis in eine Ganzzahl um, bevor du es ausgibst.

# In[2]:


# Gebe das Ergebnis der Berechnung hier als Ganzzahl aus.


# Korrekte Ausgabe (braucht nicht farbig zu sein):
# 
# ```python
# 11
# ```

# ####  c.)
# Die Mathemagierin weißt noch darauf hin, dass es bei Zaubertricks auch auf die Präsentation ankommt. Gebe nun einen Antwortsatz der Form 
# 
# **"Du hast 6 ausgewählt, das magische Ergebnis ist 11!"**
# 
# aus, wobei für die Zahl 6 die Variable `number` und für die Zahl 11 das Ergebnis (Variable `result`) eingesetzt werden soll.
# 
# **Hinweis:** In Python darf ein `print` - Befehl wie folgt über mehrere Zeilen gehen. Das könnte praktisch sein, gerade wenn du viele Strings hintereinander hängen möchtest:
# 
# ```python
# 
# print("Hallo" + 
#       "Welt")
# ```

# In[3]:


# Gebe hier den Zaubertrick als Satz aus


# Korrekte Ausgabe:
# 
# ```
# Du hast 6 ausgewählt, das magische Ergebnis ist 11!
# ```

# ### Aufgabe 2: Zersägte E-Mail-Adressen
# 
# Die Mathemagierin ist sehr zufrieden mit deiner Arbeit und bittet dich um Hilfe bei der Betreuung von ihrem Online-Shop. Sie kennt nur die Mailadressen ihrer Kunden und du sollst anhand der Mailadressen ein vereinfachtes Verzeichnis mit ihren Namen anlegen. 

# #### a. ) Ziehe einen Namen aus einer Mailadresse der Form name@service.com
# 
# Wenn die Mailadresse _Max-Mustermann@gmail.com_ lautet, sollst du _Max-Mustermann_ ausgeben, wenn die Mailadresse _KlaraKlarnamen@uni-berlin.de_ heisst, sollst du _KlaraKlarnamen_ ausgeben.
# 
# **Hinweis:** Schau dir dazu auf jeden Fall nochmal die `.split()` - Methode an. Damit kannst du z.B. eine E-Mail-Adresse am `@` - Symbol zersägen / zerlegen.

# In[5]:


mail = "willy.wizard@zauberschule.de"


# Korrekte Ausgabe:
# 
# ```
# willy.wizard
# ```

# #### b.) Ziehe einen Namen aus einer Mailadresse der Form info@name.com
# 
# Manchmal stehen die Namen bei einer Mailadresse auch erst hinter dem @-Zeichen. Gebe auch für solche Fälle die Namen aus; entferne dabei die Endung _.com_ bzw. _.de_. Du darfst dazu voraussetzen, dass innerhalb des Namens kein Punkt vorkommt. Wenn die Mailadresse also _info@Max-Mustermann.com_ lautet, sollst du _Max-Mustermann_ ausgeben.
# 
# **Hinweis:** Es ist okay, wenn du für die Berechnung mehere `.split()` - Befehle benötigst, oder ein Ergebnis zwischenspeichern möchtest. Gerne kannst du auch den Code aus der Teilaufgabe `a)` hier mitverwenden.

# In[6]:


mail = "info@helena-hexe.com"

# Berechne hier den hinteren Teil der gegebenen E-Mail - Adresse


# Korrekte Ausgabe:
# 
# ```
# helena-hexe
# ```

# #### c.) Berechne: Wie viele Kunden gibt es im Online-Shop?
# 
# Aktuell legen alle Kunden (`mail1`, `mail2`, `mail3`) als separate Variable vor. Wir möchten daraus jetzt eine Liste bauen, sodass wir die Möglichkeit hätten, später noch weitere Kunden in diese Liste hinzuzufügen.
# 
# Überführe deswegen die Kunden `mail1`, `mail2` und `mail3` in die Liste `clients`, und lasse dir anschließend die Anzahl der Elemente der Liste `clients` mit Hilfe von Python ausgeben.

# In[8]:


mail1 = "zarah.zauber@zauberberg.de"
mail2 = "info@trixie-trickser.com"
mail3 = "uwe_unhold@dunkelnetz.de" 

clients = []

# Füge hier mail1, mail2, mail3 zur clients - Liste hinzu

print(clients)


# Korrekte Ausgabe (braucht nicht farbig zu sein):
# 
# ```python
# ['zarah.zauber@zauberberg.de', 'info@trixie-trickser.com', 'uwe_unhold@dunkelnetz.de']
# ```

# In[9]:


# Gebe hier die Anzahl der Elemente der Liste clients aus


# Gewünschte Ausgabe:
# 
# ```
# 3
# ```

# #### d.) Eine Mailadresse aus Strings zusammenbauen
# 
# Plötzlich fällt der Mathemagierin ein, dass in der Liste _clients_ noch ihr wichtigster Onlineshop-Kunde fehlt. Die Infos zu ihm wurden bei einem misslungenen Trick in zwei Teile zersägt und liegen seitdem in der Liste `["Buehnenzauberer", "magic.com"]` herum. 
# 
# Rekonstruiere mit Hilfe von Python die Mailadresse des Kunden (da fehlt ein `@` zwischen "Buehnenzauberer" und "magic.com") und gebe sie aus, damit sich der Onlineshop-Kundendienst nach seinem Wohlbefinden erkundigen kann.

# In[10]:


zauberer = ["Buehnenzauberer", "magic.com"]

# Ergänze hier den Code


# Gewünschte Ausgabe:
# 
# ```
# Buehnenzauberer@magic.com
# ```

# ## Gut gemacht! :-)

