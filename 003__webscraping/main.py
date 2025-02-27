import requests
from pathlib import Path
from lxml.html import fromstring


root = Path(__file__).parent

french_cities = "https://fr.wikipedia.org/wiki/Liste_des_communes_de_France_les_plus_peupl%C3%A9es"

res = requests.get(french_cities)

#with open(root / "wiki.html", "w", encoding="utf-8") as f:
#    f.write(res.text)

content = fromstring(res.text)
print(content)

dataset = []

tables = content.xpath("//table[starts-with(@class, 'wikitable')]")

for table in tables:
    rows = table.xpath(".//tbody/tr")
    data = []
    for res in rows:
        for td in res.xpath(".//td"):
            for a in td.xpath(".//a[starts-with(@href, '/wiki/')]/text()"):
                data.append(a)
            for span in td.xpath(".//span[@class='datasortkey']/text()"):
                data.append(span)
    dataset.append(data)

with open(root / "result.txt", "w", encoding="utf-8") as f:
    for row in dataset:
        f.write(",".join(row))
    f.write("\n")


# print(dataset)



        





