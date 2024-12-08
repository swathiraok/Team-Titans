import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from flask_cors import CORS  # Import CORS

load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Fetch API key from .env
api = os.getenv('API_KEY')

@app.route('/fetch-news', methods=['GET'])
def fetch_news():
    # Get 'interest' from query parameter
    interest = request.args.get('interest')
    if not interest:
        return jsonify({"error": "No interest parameter provided"}), 400

    # Construct the URL with the provided interest and API key
    url = f"https://newsapi.org/v2/everything?q={interest}&sortBy=publishedAt&apiKey={api}"

    try:
        # Send the request to NewsAPI
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            # If the API response status is not OK
            return jsonify({"error": "Error fetching data from NewsAPI", "message": data.get('message')}), response.status_code

        # Get the list of articles from the response
        articles = data.get('articles', [])

        if articles:
            return jsonify(articles)
        else:
            return jsonify({"error": "No articles found for the provided interest"}), 404
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching news", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
