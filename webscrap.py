import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = "https://www.bbc.com/news/world-us-canada-68602748"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the container that holds the headlines
    container = soup.find('div', class_='ssrcss-uf6wea-RichTextComponentWrapper e1xue1i83')
    
    # Within the container, find all elements with the appropriate class for headlines
    headlines = container.find_all('h3')

    # Extract the text from each headline and strip any leading/trailing whitespace
    return [headline.text.strip() for headline in headlines]

# Usage
security_headlines = scrape_news()
print("Headlines: ", security_headlines)
