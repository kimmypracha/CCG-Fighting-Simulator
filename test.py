import requests
from bs4 import BeautifulSoup

URL = 'https://leetcode.com/contest/weekly-contest-245/ranking/'
page = requests.get(URL)

# soup = BeautifulSoup(page.content, 'html.parser')

# result = soup.find('div', id="contest-app")
# print(result.innerHTML())
print(page.content.decode('utf-8'))
