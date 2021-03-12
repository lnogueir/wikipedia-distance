class WikipediaNode:
  def __init__(self, link, title):
    self.link = link
    self.title = desc

  def __hash__(self):
    return hash(self.link)

  def __eq__(self, wkNode):
    return self.link == wkNode.link

  def __str__(self):
    return f'{self.link}: {self.title}'

