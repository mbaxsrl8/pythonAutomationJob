# lucky.py - Open several Google search results

import requests
import sys
import webbrowser
import bs4

print('Googling...')  ## display text while downloading Google page
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

## Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

## Open a browser tab for each result
linkElems = soup.select('.r a')          ## 找到所有具有CSS类r的元素中的<a>元素
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))