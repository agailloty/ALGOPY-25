from pathlib import Path
import os
from typing import List
from lxml.html import fromstring
from models import Player

root = Path(__file__).parent
sofifa_files = root / "sofifa-html"

def extract_players_data(filename : str) -> List[Player]:
    """Cette fonction prend en paramètre le chemin vers un fichier html, extraie son contenu et retourne une list de joueurs"""
    with open(filename, "r", encoding="utf-8") as f:
        content = fromstring("".join(f.readlines()))
        player_names = content.xpath("//a[starts-with(@href, '/player/') and @aria-expanded='false']")
        player_names = [player.text for player in player_names]
        ages = content.xpath("//td[@data-col='ae']")
        ages = [age.text for age in ages]
        overall_ratings = [rating.text for rating in content.xpath("//td[@data-col='oa']/em")]
        heights = [height.text for height in content.xpath("//td[@data-col='hi']")]
        weights = [weight.text for weight in content.xpath("//td[@data-col='wi']")]
        heights = [height.split("/")[0] for height in heights]
        values_eur = [value.text for value in content.xpath("//td[@data-col='vl']")]
        wages_eur = [value.text for value in content.xpath("//td[@data-col='wg']")]

        players = []

        for name, age, overall_rating, height, weight, value, wage in \
              zip(player_names, ages, overall_ratings, heights, weights, values_eur, wages_eur):
            player = Player(name, age, overall_rating, height, weight, value, wage)
            players.append(player)
    return players

def export_to_csv(data: list[Player], filename: str, sep = ","):
    "Exporte la liste des joueurs en format csv"
    header = "".join(["name", sep, "age", sep, "overall_rating", sep, 
              "height", sep, "weight", sep, "value", sep, "wage"])

    with open(filename, "w", encoding="utf-8") as f:
        f.write(header + "\n")

        for player in data:
            line = "".join([player.name, sep, str(player.age), sep, str(player.overall_rating), sep, 
                player.height, sep, player.weight, sep, player.value_eur, sep, 
                player.weekly_wage])
            f.write(line + "\n")


        

        
    


if os.path.exists(sofifa_files):
    files = os.listdir(sofifa_files)
    files = [sofifa_files / file for file in files]

    all_players = []
    for file in files:
        all_players.append(extract_players_data(file))

    total_players = [player for players in all_players for player in players]

    export_to_csv(total_players, root / "players.csv", sep= ";")

else:
    print("L'emplacement n'existe pas")


