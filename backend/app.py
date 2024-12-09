from concurrent.futures import ThreadPoolExecutor
import os
import requests
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

# Fetch API key
api_key = os.getenv('API_KEY')

def clean_articles_to_dataframe(articles):
    """Convert articles to a cleaned pandas DataFrame."""
    formatted_articles = [
        {
            'source': article.get('source', {}).get('name', '').strip() if article.get('source') else None,
            'author': article.get('author', '').strip() if article.get('author') else None,
            'title': article.get('title', '').strip() if article.get('title') else None,
            'description': article.get('description', '').strip() if article.get('description') else None,
            'url': article.get('url', '').strip() if article.get('url') else None,
            'urlToImage': article.get('urlToImage', '').strip() if article.get('urlToImage') else None,
            'publishedAt': article.get('publishedAt', '').strip() if article.get('publishedAt') else None,
            'content': article.get('content', '').strip() if article.get('content') else None
        }
        for article in articles
    ]
    df = pd.DataFrame(formatted_articles)
    df = df.dropna(how='all')
    df.replace('', pd.NA, inplace=True)
    df.dropna(subset=['url'], inplace=True)
    return df

def fetch_full_description_parallel(urls):
    """Fetch full descriptions for multiple URLs in parallel."""
    def fetch(url):
        try:
            page = requests.get(url, timeout=10)
            soup = BeautifulSoup(page.text, 'html.parser')
            text = soup.get_text(separator=' ')
            return ' '.join(text.split())
        except Exception as e:
            print(f"Error fetching URL {url}: {e}")
            return None

    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
        descriptions = list(executor.map(fetch, urls))

    return descriptions

@app.route('/fetch-news', methods=['GET'])
def fetch_news():
    """Fetch news articles and return cleaned data with full descriptions."""
    interest = request.args.get('interest')
    if not interest:
        return jsonify({"error": "No interest parameter provided"}), 400

    # Construct the NewsAPI request URL
    url = f"https://newsapi.org/v2/everything?q={interest}&sortBy=publishedAt&apiKey={api_key}"

    try:
        # Fetch articles from NewsAPI
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({"error": "Error fetching data from NewsAPI", "message": response.json().get('message')}), response.status_code

        data = response.json()
        articles = data.get('articles', [])[:10] 
        if not articles:
            return jsonify({"error": "No articles found for the provided interest"}), 404

        # Clean and process articles
        df_cleaned_articles = clean_articles_to_dataframe(articles)
        urls = df_cleaned_articles['url'].tolist()
        descriptions = fetch_full_description_parallel(urls)
        df_cleaned_articles['Full Description'] = descriptions
        # Save the data to a CSV file
        output_path = 'articles_with_full_description.csv'
        df_cleaned_articles.to_csv(output_path, index=False)

        # Return the cleaned articles as a JSON response
        return jsonify({
            "message": f"Data saved to {output_path}",
            "articles": df_cleaned_articles.to_dict(orient='records')
        })
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching news", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
