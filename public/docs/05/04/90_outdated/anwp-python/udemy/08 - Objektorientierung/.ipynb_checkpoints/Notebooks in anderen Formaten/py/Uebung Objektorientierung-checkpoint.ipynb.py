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

# # Übung: Objektorientierte Programmierung
# 
# Anbei findest du ein paar Aufgaben zum Programmieren. Viel Spaß dabei! :)
# 
# Wenn du mit diesem Übungsblatt fertig bist, kannst du deine Lösung mit der Musterlösung in Textform (Datei: `Uebung Objektorientierung (Musterloesung)`) vergleichen. 
# 
# Die Video - Musterlösung (in der nächsten Lektion) ist besonders ausführlich gehalten. Wenn du alles richtig gelöst hast, ist es vollkommen okay, wenn du diese Lektion dann überspringst.

# ### Aufgabe 1: Modelliere einen Würfel

# Erstelle eine Klasse _Cube_, mit der du einen Würfel modellierst. Die Würfel-Klasse soll als Eigenschaft die Länge einer Würfel-Seite besitzen. Darüber hinaus soll die Klasse auch zwei Methoden haben: die Methode `volume()` berechnet das Volumen und gibt es aus, die Methode `surface()` berechnet die Oberfläche und gibt sie aus.

# In[1]:


class Cube():
    # Ergänze hier deinen Code
        

# danach erzeugen wir eine Instanz deiner Cube-Klasse 
a = Cube(3)

# und testen die Methoden
a.surface()
a.volume()


# Erwartete Ausgabe:
# 
# ```
# 54
# 27
# ```

# ### Aufgabe 2: Modelliere ein Kugel

# Die Kugel-Klasse soll als Eigenschaft den Radius übergeben bekommen. Zudem soll sie - ähnlich wie der Würfel - zwei Methoden haben: `surface()` um den Oberflächeninhalt zu berechnen, `volume()` um das Volumen zu berechnen.
# 
# Damit du diese Berechnungen durchführen kannst, benötigst du die Kreiszahl Pi. Diese steht dir nach einem `import math` unter `math.pi` zur Verfügung (was der `import` - Befehl genau macht, schauen wir uns noch später im Kurs an).
# 
# Die Formeln für die Oberflächeninhalt / Volumen einer Kugel darfst du im Internet nachgucken.

# In[6]:


import math
print(math.pi)


# In[8]:


import math

class Ball():
    # Ergänze hier deinen Code
        

b = Ball(4)
b.surface()
b.volume()


# Erwartete Ausgabe (es reicht, wenn die Zahlenwerte auf ein paar Nachkommastellen genau sind):
# 
# ```
# 201.06192982974676
# 268.082573106329
# ```

# ### Aufgabe 3: Modelliere ein Konto
# 
# #### a.) 
# 
# Erstelle die Konto-Klasse _Account_ mit der Eigenschaft Kontostand _credits_; diese Eigenschaft wird mit einem Startkapital initialisiert. Die Methode `display()` soll den aktuellen Kontostand ausgeben. 

# In[8]:


class Account():
    # Ergänze hier deinen Code
        
Kunde111 = Account(500)
Kunde111.display()


# Erwartete Ausgabe:
# 
# ```
# 500
# ```

# **b.)**
# 
# Ergänze die Klasse _Account_ um zwei Methoden (`pay_in()` zum Einzahlen, `withdraw()` zum Abheben), sodass du Geldbeträge einzahlen und abbuchen kannst und der Kontostand entsprechend angepasst wird. 
# 
# Du sollst nur Geld abheben können, solange auch Geld auf dem Konto ist. Ein Dispo-Kredit wird nicht gewährt. In dem Fall soll eine Fehlermeldung ausgegeben werden, in der steht, wieviel Geld maximal abgebucht werden kann.

# In[9]:


class Account():
    
    # Ergänze hier deinen Code. Du darfst den Code aus a) 
    # natürlich hierhin übernehmen.
    
        
Kunde111 = Account(500)
Kunde111.display()
Kunde111.pay_in(40)
Kunde111.display()
Kunde111.withdraw(25)
Kunde111.display()
Kunde111.withdraw(600)


# Erwartete Ausgabe:
# 
# ```
# 500
# 540
# 515
# Du kannst nur noch 515€ abheben!
# ```

# **c.)**
# 
# Bislang ist das Konto noch ungeschützt - wir brauchen eine PIN! Ergänze in der Klasse die Eigenschaft _pin_; so wie mit dem Startkapital soll das Konto auch mit einer PIN initialisiert werden.
# 
# Von nun an muss man beim Geldabheben nicht nur den Betrag, sondern auch die PIN angeben: Nur wenn die PIN mit der des Kontos übereinstimmt, kann auch Geld abgebucht werden, ansonsten kommt es zu einer Fehlermeldung!

# In[11]:


class Account():
    # Ergänze hier deinen Code. Du darfst den Code aus b) 
    # natürlich hierhin übernehmen.
    
        
Kunde111 = Account(500, "1234")
Kunde111.display()
Kunde111.pay_in(40)
Kunde111.display()
Kunde111.withdraw(25, "1234")
Kunde111.display()
Kunde111.withdraw(600, "12345")


# Erwartete Ausgabe:
# 
# ```
# 500
# 540
# 515
# Falsche PIN! Konto gesperrt! Du bist verhaftet! Hände hoch!
# ```

# ### Aufgabe 4: Modelliere einen Zug
# 
# 
# **a.)**
# 
# Jetzt wirst du Zugobjekte bauen! Erstelle die Klasse _Train_, die mit den Eigenschaften _route_ und _position_ initialisiert wird. Bei _route_ handelt es sich um eine Liste mit den Haltebahnhöfen des Zuges. _position_ steht für den Index des Bahnhofs aus der Liste, an dem sich der Zug gerade befindet bzw. von dem er zuletzt abgefahren ist (wo genau sich der Zug auf der Strecke zwischen zwei Bahnhöfen befindet, interessiert uns hier nicht). Mit der Methode `show_station()` soll der Name dieses Bahnhofs ausgegeben werden.

# In[12]:


class Train():
    # Ergänze hier deinen Code
    
orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.show_station()


# Erwartete Ausgabe:
# 
# ```
# Paris
# ```
# 

# **b.)**
# 
# Bisher sitzt ein Zug der Klasse _Train_ noch in seinem Startbahnhof fest. Ergänze nun zwei Methoden `move()` und `move_back()` mit denen man einen Zug auf seiner Route zur nächsten bzw. zur vorherigen Station bewegen kann - sofern es diese Station auf der Route gibt: Der Zug darf seine Route nicht verlassen!
# 

# In[14]:


class Train():
    
    # Ergänze hier deinen Code. Du darfst natürlich deinen Code aus
    # Teilaufgabe a) hierhin übernehmen.
            
orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.move_back()
orientexpress.show_station()


# Erwartete Ausgabe:
# 
# ```
# Paris
# Budapest
# Bukarest
# Istanbul
# Endstation! Alle aussteigen!
# Bukarest
# ```

# **c.)**
# 
# Die Route soll nachträglich bearbeitet werden können, indem man mit einer Methode `bypass_station()` einen anzugebenden Haltebahnhof von der Route entfernt. Der Zug soll dann sicherheitshalber an den Start der Route versetzt werden, sofern er sich nicht schon dort befindet.
# 
# **Tipp:** Erinnere dich an die Methoden für Listen. :-)

# In[15]:


class Train():
    
    # Ergänze hier deinen Code. Du darfst natürlich deinen Code aus
    # Teilaufgabe b) hierhin übernehmen.
    
            
orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.bypass_station("Budapest")
orientexpress.move()
orientexpress.show_station()


# Erwartete Ausgabe:
# 
# ```
# Bukarest
# ```

# #### Gut gemacht :-) 

