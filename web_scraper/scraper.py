import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Nintendo'

def get_citations_needed_count(URL):
  URL = URL
  page = requests.get(URL)
  pretty_page = BeautifulSoup(page.content, 'html.parser')
  paragraph = pretty_page.find_all('p')
  print(paragraph)
  

def get_citations_needed_report():
  pass

if __name__ == '__main__':
  count = get_citations_needed_count(URL)
  print(count)
