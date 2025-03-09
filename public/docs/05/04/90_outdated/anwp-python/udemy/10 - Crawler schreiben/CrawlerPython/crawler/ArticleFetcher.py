import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from .CrawledArticle import CrawledArticle

class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"

        while url != "":
            print(url)
            time.sleep(1)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")

            for card in doc.select(".card"):
                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                title = card.select(".card-title span")[1].text
                image = urljoin(url, card.select_one("img").attrs["src"])

                yield CrawledArticle(title, emoji, content, image)

            next_button = doc.select_one(".navigation .btn")
            if next_button:
                next_href = next_button.attrs["href"]
                next_href = urljoin(url, next_href)
                url = next_href
            else:
                url = ""