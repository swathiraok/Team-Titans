import requests
import config


class NYTimesScraper:
    """
    API integration for New York Times article summaries.
    """
    def __init__(self):
        self.api_key = config.NYTIMES_API_KEY
        self.base_url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'

    def fetch_articles(self, topic) -> list:
        url = f'{self.base_url}?q={topic}&api-key={self.api_key}'
        response = requests.get(url).json()
        if 'response' in response and 'docs' in response['response']:
            articles = response['response']['docs']
            abstract = articles[0].get('abstract', '')
            snippet = articles[0].get('snippet', '')
            lead_paragraph = articles[0].get('lead_paragraph', '')
            return abstract + ' ' + snippet + ' ' + lead_paragraph
        return []


if __name__ == "__main__":
    nytimes_api = NYTimesScraper()

    # Specify the keyword for the article search
    keyword = 'https://theathletic.com/5186510/2024/01/09/brian-flores-vikings-nfl-coaching-lawsuit/'

    # Get and print the concatenated information from the response

    concatenated_info = nytimes_api.fetch_articles(keyword)
    if concatenated_info:
        print(concatenated_info)
    else:
        print("No response or invalid response format.")
