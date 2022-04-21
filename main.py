# Import library
from doctest import OutputChecker
from bs4 import BeautifulSoup
import requests

# Define URL
url = "https://game8.co/games/Pokemon-Legends-Arceus/archives/356252"
# Ask hosting server to fetch url
requests.get(url)
resp = requests.get(url)

if resp.status_code == 200:
    print ('OK!')
else:
    print ('Boo!')

pages = requests.get(url).text

# parser-lxml = Change html to Python friendly format
soup = BeautifulSoup(pages, 'lxml')

table = soup.find_all('table', class_='a-table a-table a-table', style_='')[5]
# element = soup.find_all_next('table')
print(table)