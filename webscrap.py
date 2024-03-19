import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = "https://www.bbc.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2', class_='security-headline')
    return [headline.text for headline in headlines]

#usage
security_headlines = scrape_news()
print("Headlines: ", security_headlines)