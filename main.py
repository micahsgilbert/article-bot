import requests
from bs4 import BeautifulSoup
from Article import Article

class WiredArticle(Article):
  def __init__(self, soup, url):
    super().__init__(soup, url)
  
  def get_title(self):
    return self.soup.title.string

  def get_date(self):
    return self.soup.time.string

  def enumerate_paragraphs(self):
    return self.soup.find_all("p")[2:-4]

  def assemble_text(self, paragraphs):
    text = ""
    # Just gets the first line of every paragraph if it isn't a quote or first-person thing
    for p in paragraphs:
      line = p.get_text().split(".")[0]
      if ("my" not in line and "I" not in line and '"' not in line):
        text += line + ". "
    return text

url = "https://www.wired.com/story/sneaky-zero-click-attacks-hidden-menace/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

w = WiredArticle(soup, url)

print(w.generate_description())