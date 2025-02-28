import requests
from pathlib import Path
from lxml.html import fromstring


root = Path(__file__).parent

res = requests.get("https://www.leboncoin.fr/")
print(res.text)