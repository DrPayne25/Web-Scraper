import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Nintendo'
URL2 = 'https://en.wikipedia.org/wiki/Sony'

def get_passages(URL):
  page = requests.get(URL)
  b_soup = BeautifulSoup(page.content, 'html.parser').find_all(title='Wikipedia:Citation needed')
  return [match.find_parent('p').text for match in b_soup]

def get_citations_needed_count(URL):
  citations = get_passages(URL)
  return len(citations)

def get_citations_needed_report(URL):
  citations = get_passages(URL)
  return '\n'.join([citation.strip() for citation in citations])

  # Was having issues getting my way below to work worked with Brandon and he walked me through how to do it a different way
  # page = requests.get(URL)
  # b_soup = BeautifulSoup(page.content, 'html.parser').find_all('p')
  # citations_list = []
  # for item in b_soup:
  #   paragraph = item.find_all('a',title="Wikipedia:Citation needed")
  #   if paragraph:
  #     citations_list.append(item.text)
  #     citations_list += '\n'
  #     print(f'Citation Needed : {item.text}')

if __name__ == '__main__':
  count = get_citations_needed_count(URL)
  print(count)
  print(get_citations_needed_report(URL).split('\n')[0])
  
  
