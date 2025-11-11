from bs4 import BeautifulSoup
import requests

# Some websites need you to use proper headers when fetching them:
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

def fetch_website_links(url: str) -> list[str]:
    """
    Fetch all the links from a website
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return [link for link in links if link.startswith('http')]

def fetch_website_contents(url: str):
    """
    Fetch the title and contents of a website at the given url
    truncate to 2000 characters as a sensible limit
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string if soup.title else 'No title found'
    if soup.body:
        for irrelevant in soup.body(['script', 'style', 'img', 'input']):
            irrelevant.decompose()
        contents = soup.body.get_text(separator='\n', strip=True)[:2000]
    else:
        contents = 'No contents found'
    return (title + "\n\n" + contents)[:2_000]