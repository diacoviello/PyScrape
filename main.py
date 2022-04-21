# Import library
from doctest import OutputChecker
from bs4 import BeautifulSoup
import requests

# Define URL
url = "https://game8.co/games/Pokemon-Legends-Arceus/archives/356251"
# Ask hosting server to fetch url
requests.get(url)
resp = requests.get(url)

if resp.status_code == 200:
    print ('OK!')
else:
    print ('Boo!')