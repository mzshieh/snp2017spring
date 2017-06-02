import requests
from bs4 import BeautifulSoup

res = requests.get('https://mzshieh.github.io/snp2016/html/1.html')

soup = BeautifulSoup(res.text, 'lxml')

div = soup.find('div')
print('===== whole tag ========================== begin =====')
print(div)
print('===== whole tag =========================== end ======')

print('')

print('===== only text ========================== begin =====')
print(div.text)
print('===== only text =========================== end ======')
