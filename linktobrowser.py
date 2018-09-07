import requests
import bs4
import webbrowser
import commonwords

a = requests.get(input()).text

soup = bs4.BeautifulSoup(a,'html.parser')

[s.extract() for s in soup('script')]
for i in soup("link"):
  i['href'] = 'http://wikipedia.org' + i['href']
for i in soup("img"):
  i['src'] = 'http:' + i['src']

webbrowser.open("data:text/html," + str(soup))
