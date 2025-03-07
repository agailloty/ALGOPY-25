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
        values_eur = [value.text for value in content.xpath("//td[@data-col='vl']")]
        wages_eur = [value.text for value in content.xpath("//td[@data-col='wg']")]

        players = []

        for name, age, overall_rating, height, weight, value, wage in \
              zip(player_names, ages, overall_ratings, heights, weights, values_eur, wages_eur):
            player = Player(name, age, overall_rating, height, weight, value, wage)
            players.append(player)
    return players



if os.path.exists(sofifa_files):
    files = os.listdir(sofifa_files)
    files = [sofifa_files / file for file in files]

    extract_players_data(files[0])



else:
    print("L'emplacement n'existe pas")


