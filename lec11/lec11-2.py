import requests
from bs4 import BeautifulSoup

res = requests.get('https://mzshieh.github.io/snp2016/html/2.html')

soup = BeautifulSoup(res.text, 'lxml')

a = soup.find('a')
print('===== whole tag ========================== begin =====')
print(a)
print('===== whole tag =========================== end ======')
print('')
print('===== only text ========================== begin =====')
print(a.text)
print('===== only text =========================== end ======')

# access attributes like a dictionary
print(a.get('href'))
print(a['href'])

# get return None
print(a.get('xd'))

# The following fails
print(a['xd'])
