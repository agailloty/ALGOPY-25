from pathlib import Path
import os
from typing import List

root = Path(__file__).parent
sofifa_files = root / "sofifa-html"

def extract_data(filename : str) -> List[str]:
    """Cette fonction prend en paramètre le chemin vers un fichier html, extraie son contenu et retourne une list de chaine de caractères"""
    with open(filename, "r", encoding="utf-8") as f:
        content = "".join(f.readlines())
        print(content)


if os.path.exists(sofifa_files):
    files = os.listdir(sofifa_files)
    files = [sofifa_files / file for file in files]

    extract_data(files[0])



else:
    print("L'emplacement n'existe pas")


