import os
import requests
import zipfile

from pathlib import Path

def download_dataset(data_folder : Path):
    # URL du fichier
    url = "https://www.kaggle.com/api/v1/datasets/download/ldausl/regression-with-an-insurance"

    download_path = data_folder / "fichier.zip"

    response = requests.get(url, allow_redirects=True)

    if response.status_code == 200:
        with open(download_path, "wb") as file:
            file.write(response.content)
        print(f"Fichier téléchargé avec succès : {download_path}")
    else:
        print(f"Erreur lors du téléchargement : {response.status_code}")

    with zipfile.ZipFile(download_path, "r") as zip_ref:
        zip_ref.extractall(data_folder)

