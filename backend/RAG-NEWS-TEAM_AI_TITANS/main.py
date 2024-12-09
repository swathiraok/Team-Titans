import sys
from model_api import ModelAPI
from nyt_scraper import NYTimesScraper
from web_scraper import GenericScraper
from summary_pipeline import Summarization
from chromadb.utils import embedding_functions
import chromadb


def fetch_related_links(collection, query):
    client = chromadb.PersistentClient(path="database/chroma_data")
    embed_func = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="sentence-transformers/sentence-t5-base"
    )
    collection = client.get_collection(name=collection.capitalize(), embedding_function=embed_func)

    search_results = collection.query(query_texts=[query], n_results=2)
    return [meta['link'] for meta in search_results['metadatas'][0]]


def classify_prompt(prompt, model_name):
    api = ModelAPI(model_name)
    output = api.execute(prompt)
    categories = ['technology', 'science', 'health', 'sports']
    return next((cat for cat in output if cat.lower().strip() in categories), "")


def summarize_news(link):
    scraper = NYTimesScraper() if 'nytimes.com' in link else GenericScraper(link)
    article = scraper.fetch_articles(link) if 'nytimes.com' in link else scraper.scrape_content()
    summarizer = Summarization()
    return summarizer.generate(" ".join(article))


if __name__ == "__main__":
    user_input = input("Enter keywords for news search: ")
    model = 'mistralai/mixtral-8x7b-instruct-v0.1'
    category = classify_prompt(user_input, model)
    if not category:
        print("Unable to categorize prompt. Exiting.")
        sys.exit()

    links = fetch_related_links(category, user_input)
    for link in links:
        summary = summarize_news(link)
        print(f"Summary:\n{summary[0]['generated_text']}")
        print("--------------------")