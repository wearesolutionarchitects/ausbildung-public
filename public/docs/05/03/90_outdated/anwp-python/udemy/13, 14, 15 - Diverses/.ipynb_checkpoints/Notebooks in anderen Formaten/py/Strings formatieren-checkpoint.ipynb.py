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

# ## Strings formatieren
# 
# Manchmal möchtest du in einen String irgendwelche Werte einsetzen. Also z.B. möchtest du die Ausgabe erzeugen, "Ich habe 5 Hunde". Bisher war das immer recht unhandlich, mit der str() - Funktion:

# In[1]:


n = 5
print("Ich habe " + str(n) + " Hunde")


# In dieser Lektion lernst du eine neue, praktsiche Methode kennen, um eine solche Ausgabe zu erzeugen!

# ### Schauen wir uns dazu mal ein Beispiel an
# 
# Stell dir vor, du möchtest deine Anwendung übersetzen. Spätestens dann stößt du auf Probleme:

# In[2]:


n = 5
print("Ich habe " + str(n) + " Hunde")
print("I got " + str(n) + " dogs")


# Wie bekommst du es jetzt hin, dass der Sprachbaustein austauschbar ist, und nicht mit dem `+ str(n) +` - Befehl "verwoben" ist?
# 
# **Idee:** Du könntest die Sprachbausteine in einem Dictionary definieren, und einen Platzhalter per `.replace()` einsetzen:

# In[3]:


translations = {
    "number_of_dogs": "Ich habe XXX Hunde"
}
print(translations["number_of_dogs"].replace("XXX", str(n)))


# **Problem:** Das wird aber schnell unübersichtlich. 
# 
# **Lösung:** Glücklicherweise stellt uns Python hier eine `.format()` - Methode zur Verfügung, die das ganze sehr viel einfacher macht. Hierbei verwenden wir `{0}` für die Position, wo wir den Parameter `n` des `.format(n)` - Aufrufs einsetzen möchten:

# In[4]:


print("Ich habe {0} Hunde".format(n))


# **Ergebnis:** Unserer Übersetzungs-Code ist sehr viel angenehmer:

# In[5]:


translations = {
    "number_of_dogs": "Ich habe {0} Hunde"
}
print(translations["number_of_dogs"].format(n))


# Diese `.format()` - Methode funktioniert auch mit mehreren Parametern. Hierbei definiert dann `{0}` die Position für den ersten Parameter, `{1}` die Position, an die Stelle, wo der 2. Parameter hin gesetzt werden soll. 
# 
# Hier in folgendem Fall wird also die `{1}` durch `"Katzen"` ersetzt, und `{0}` durch die Zahl 5.

# In[6]:


print("Ich habe {1} {0}x".format(5, "Katzen"))


# #### Kommazahlen und runden
# 
# Der `format()` - Befehl erlaubt es, Kommazahlen komfortabel zu runden. Hierbei wird an einen Formatierungs-Befehl (das war z.B. `{0}` oder `{1}`) noch innerhalb der geschweiften Klammern ein `f` drangehängt.
# 
# Dadurch sagen wir Python, dass diese Zahl als Kommazahl betrachtet werden soll. Entsprechend wird hier jetzt die Zahl 5 eingesetzt, die `.000000` werden aber ergänzt, weil es als Kommazahl ausgegeben wird:

# In[9]:


print("So viele Katzen habe ich: {0:f}".format(5))


# Wenn wir die Anzahl der Stellen beschränken möchten, können wir das tun, indem wir nach dem Doppelpunkt schreiben `.2`, um z.B. die Kommazahl auf 2 Nachkommastellen zu limitieren:

# In[10]:


print("So viele Katzen habe ich: {0:.2f}".format(5))


# Das können wir jetzt auch für echte Kommazahlen nutzen, um diese zu runden! :)

# In[44]:


print("Pi hat den Wert: {0:.3f}".format(3.141529))


# ### Parameter bennennen
# 
# Wenn du einen String hast, in den viele Platzhalter eingesetzt werden, wird die Schreibweise `{0}`, `{1}`, `{2}`, `{3}`, `{4}`, `{5}`, ... irgendwann unübersichtlich.
# 
# Glücklicherweise können wir die Parameter auch benennen. Hierbei ist wichtig, dass wenn auf der linken Seiten ein Parameter z.B. `{animal}` heißt, dass der Parameter `animal` dann entsprechend auch der `.format()` - Funktion übergeben wird. 
# 
# Hier in dem Fall ist es also so, dass an die Stelle, wo `{animal}` steht, dass da der Wert vom `.format()` - Aufruf `animal = "Hunde"`, also konkret, das Wort "Hunde" eingesetzt wird. 

# In[47]:


print("Ich habe {number:.3f} {animal}".format(number = 5, animal = "Hunde"))


