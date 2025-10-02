from transformers import pipeline
from fetch_news import fetch_articles
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


articles = fetch_articles()
with open('daily_summary.txt', 'w', encoding='utf-8') as f:
    for art in articles:
        print(f"Summarizing: {art['title']}")
        text = art['summary'] or art['title']
        summary = summarizer(text, max_length=80, min_length=25, do_sample=False)[0]['summary_text']
        f.write(f"Title: {art['title']}\nLink: {art['link']}\nSummary: {summary}\n\n")
