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

# # Abschluss Funktionen

# Nimm dir die Zeit, um die Aufgaben sorgfältig zu bearbeiten. :-) Viel Erfolg!
# 
# Wenn du mit diesem Übungsblatt fertig bist, kannst du deine Lösung mit der Musterlösung in Textform (Datei: `Abschluss Funktionen (Musterloesung)`) vergleichen. 
# 
# Die Video - Musterlösung (in der nächsten Lektion) ist besonders ausführlich gehalten. Wenn du alles richtig gelöst hast, ist es vollkommen okay, wenn du diese Lektion dann überspringst.

# ### Ein funktionaler Online-Shop
# Die Mathemagierin will ihren Online-Shop auf Funktionen umrüsten. Es wartet also wieder einiges an Arbeit auf dich. 

# #### a.) Schreibe eine Funktion, die den Gesamtpreis der Produkte im Warenkorb berechnet.
# Vervollständige die Funktion list_sum(), der als Parameter eine Liste mit den Preisen übergeben wird. Die Funktion soll dann die Summe der Zahlen aus der Liste ausgeben.

# In[4]:


cart_prices = [20, 3.5, 6.49, 8.99, 9.99, 14.98]

def list_sum(l):
    # hier kommt dein Code hin
    print("Hier kommt dein Code hin")
    
list_sum(cart_prices)
        


# Folgende Ausgabe wird erwartet: `63.95`

# #### b.) Schreibe eine Funktion, die für einen Artikel eine Preis-Tabelle erstellt.
# 
# Nun wünscht sich die Mathmagierin eine Funktion, der sie einen Artikelnamen und den Verkaufspreis übergeben kann. Daraus soll die Funktion eine Liste erstellen, in der die Preise von einem, zwei, drei,... bis zehn Einheiten des Artikels
# stehen. Genauer soll jedes Element in der Liste so aussehen: "Anzahl x Artikel: Preis".
# 
# Du wunderst dich nur kurz über die Ansprüche der Mathemagierin.

# In[5]:


def prices_list(name, price):
    # hier kommt dein Code hin, das "pass" kannst du durch deinen Code ersetzen
    return []

print(prices_list("Wunderkeks", 0.79))


# Folgende Ausgabe wird erwartet (muss nicht farbig sein):
# 
# ```python
# ['1 x Wunderkeks: 0.79', '2 x Wunderkeks: 1.58', '3 x Wunderkeks: 2.37', '4 x Wunderkeks: 3.16', '5 x Wunderkeks: 3.95', '6 x Wunderkeks: 4.74', '7 x Wunderkeks: 5.53', '8 x Wunderkeks: 6.32', '9 x Wunderkeks: 7.11', '10 x Wunderkeks: 7.9']
# ```

# #### c.) Schreibe eine Funktion, die die Listen mit den Artikeln auffüllt.
# 
# Von nun an soll auch eine Funktion die Waren in die virtuellen Regale einräumen, d.h. an die erste noch leere Position in der Liste _shelf_ packen. Als Parameter soll der Funktion _shelve()_ der einzusortierende Artikel übergeben werden. Die Funktion aktualisiert dann die Liste `shelf`, und der neue Artikel wurde in das erste leere Regalfach eingeräumt. 

# In[8]:


shelf = ["Zaubersäge", "leer", "Wunderkekse", "Trickarten", "leer"]

def add_shelf(article):
    # hier kommt dein Code hin. 
    # Du darfst von innerhalb der Funktion direkt auf die Variable "shelf"
    # zugreifen, diese muss nicht als Parameter übergeben werden, da sie
    # schon außerhalb der Funktion existiert.
    print("Hier kommt dein Code hin")

add_shelf("Rubik's Cube")
print(shelf)


# Folgende Ausgabe wird erwartet (braucht nicht farbig zu sein):
# 
# ```python
# ['Zaubersäge', "Rubik's Cube", 'Wunderkekse', 'Trickkarten', 'leer']
# ```

# ### Gute Arbeit :-)

