import feedparser
RSS_URLS = [
    'https://rss.cnn.com/rss/edition.rss',
    'https://feeds.bbci.co.uk/news/rss.xml',
    'https://rss.app/feeds/mNU4RmLkdgvt2IfY.xml' 
]


def fetch_articles():
    articles = []
    for url in RSS_URLS:
        feed = feedparser.parse(url)
        print(f"Number of entries in feed {url}: {len(feed.entries)}")
        for entry in feed.entries[:5]:
            print("Entry keys:", entry.keys())
            articles.append({
                'title': entry.get('title', ''),
                'link': entry.get('link', ''),
                'summary': entry.get('summary', '')
            })
    print("Fetched articles:", articles)
    return articles

if __name__ == "__main__":
    fetch_articles()
