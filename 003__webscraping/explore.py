import requests
from pathlib import Path
from lxml.html import fromstring


root = Path(__file__).parent

french_cities = "https://fr.wikipedia.org/wiki/Liste_des_communes_de_France_les_plus_peupl%C3%A9es"

res = requests.get(french_cities)

with open(root / "wiki.html", "w", encoding="utf-8") as f:
    f.write(res.text)