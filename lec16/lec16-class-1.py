import requests
from bs4 import BeautifulSoup
import webbrowser
import random
res = requests.get('https://zh.wikipedia.org/wiki/%E9%AE%9F%E9%B1%87%E9%AD%9A')
soup = BeautifulSoup(res.text, 'lxml')
links = soup.find_all('a')
for link in links:
    if link.get('href')!=None:
        print(link.get('href'))

output = []
while len(output)<5:
    link = random.choice(links)
    href = link.get('href')
    if href!=None and href not in output:
        output.append(href)

for url in output:
    if url.startswith('//'):
        webbrowser.open('https:'+url)
    elif url.startswith('/'):
        webbrowser.open('https://zh.wikipedia.org'+url)
    else:
        webbrowser.open(url)
