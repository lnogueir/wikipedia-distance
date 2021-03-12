from bs4 import BeautifulSoup
from WikipediaNode import WikipediaNode
import urllib.request
import ssl, re

sslContext = ssl.SSLContext()
startUrl = 'https://en.wikipedia.org/wiki/WebRTC'

source = urllib.request.urlopen(startUrl, context=sslContext).read()
soup = BeautifulSoup(source, 'lxml')

uniqueWkpNodes = set({})
for tag in soup.find_all(href=True):
  if not re.match(r'^\/wiki\/[^\/:#]*\/?$', tag['href']):
    continue
  wkpNode = WikipediaNode(tag['href'], tag.get('title') or tag.text)
  uniqueWkpNodes.add(wkpNode)

print(unique)
