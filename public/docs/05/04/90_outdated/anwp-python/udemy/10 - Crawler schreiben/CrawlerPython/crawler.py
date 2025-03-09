import crawler

fetcher = crawler.ArticleFetcher()

for element in fetcher.fetch():
    print(element.emoji + ": " + element.title)