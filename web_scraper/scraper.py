import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Nintendo'
URL2 = 'https://en.wikipedia.org/wiki/Sony'

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
  b_soup = BeautifulSoup(page.content, 'html.parser')
  citations = b_soup.find(title='Wikipedia:Citation needed')
  paragraphs = citations.find_parents('p')
  for paragraph in paragraphs:
    print(paragraph)

if __name__ == '__main__':
  count = get_citations_needed_count(URL)
  print(count)
  report = get_citations_needed_report(URL)
  print(report)
  
