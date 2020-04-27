import requests
import sys
from bs4 import BeautifulSoup
from article_configurations import articles

def get_domain_from_url(u):
  u = u[u.index("//")+2:]
  u = u[:u.index("/")]
  return u

if "-u" in sys.argv:
  url = sys.argv[sys.argv.index("-u") + 1]

else:
  url = input("Article URL: ")

domain = get_domain_from_url(url)
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

try:
  article = articles[domain](soup, url)
  print(article.generate())
except KeyError:
  print("Article type not configured")