class Article:
  def __init__(self, soup, url):
    self.soup = soup
    self.url = url

  def get_title(self):
    raise NameError("Function get_title required but not defined")

  def get_date(self):
    raise NameError("Function get_date required but not defined")

  def enumerate_paragraphs(self):
    raise NameError("Function enumerate_paragraphs required but not defined")

  def assemble_text(self):
    raise NameError("Function assemble_text required but not defined")

  def generate_description(self):
    return f"""Title: {self.get_title()}
URL: {self.url}
Date: {self.get_date()}
Summary: {self.assemble_text(self.enumerate_paragraphs())}
"""