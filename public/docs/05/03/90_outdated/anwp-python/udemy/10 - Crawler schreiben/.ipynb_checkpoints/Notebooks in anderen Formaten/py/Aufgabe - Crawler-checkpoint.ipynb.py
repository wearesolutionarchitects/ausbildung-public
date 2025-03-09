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

# ## Aufgabe: Crawler
# 
# **Aufgabe:**
# 
# - Passe den ArticleFetcher so an, dass er die Informationen aus allen Seiten extrahiert
# 
# Hier nochmal die URL: http://python.beispiel.programmierenlernen.io/index.php
# 
# **Tipps:**
# 
# - Schau dir zuerst an, wie du den Button "Zur nächsten Seite" ansteuern kannst
# - Wie greifst du von Python aus auf das "href" - Attribut dieses Buttons zu?
# - (Optional): Probier ggf. erstmal, nur die Infos der ersten 2 Seiten zu holen. Kannst du darauf aufbauend das Programm verallgemeinern, sodass es alle Seiten einliest?
# - Du kannst dich daran orientieren, ob es einen "Zur nächsten Seite"-Button gibt, oder nicht. Wenn es diesen Button nicht mehr gibt, bist du auf der letzten Seite angelangt. Welcher Schleifentyp bietet sich hier an, wenn du die Schleife erst dann stoppen willst, wenn es den Button nicht mehr gibt?

# In[8]:


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

import time


# In[6]:


class CrawledArticle():
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image
        
class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        time.sleep(1)
        print(url)
        r = requests.get(url)
        doc = BeautifulSoup(r.text, "html.parser")
        
        articles = []
        for card in doc.select(".card"):
            emoji = card.select_one(".emoji").text
            content = card.select_one(".card-text").text
            title = card.select(".card-title span")[1].text
            image = urljoin(url, card.select_one("img").attrs["src"])

            crawled = CrawledArticle(title, emoji, content, image)
            articles.append(crawled)
        return articles


# In[7]:


fetcher = ArticleFetcher()
fetcher.fetch()


