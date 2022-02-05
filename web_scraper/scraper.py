import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Nintendo'

def get_citations_needed_count(URL):
  URL = URL
  page = requests.get(URL)
  b_soup = BeautifulSoup(page.content, 'html.parser')
  citations = b_soup.find_all(title="Wikipedia:Citation needed")
  count = 0
  for citation in citations:
    count += 1
  return(count)
  

def get_citations_needed_report(URL):
  URL = URL
  page = requests.get(URL)
  pretty_page = BeautifulSoup(page.content, 'html.parser')

if __name__ == '__main__':
  count = get_citations_needed_count(URL)
  print(count)
