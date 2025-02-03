from pathlib import Path
import os
# Si dossier /dataset vide ou que son contenu est vide, alors télécharger les données
rootPath = Path(__file__).parent
datasetFolder = rootPath / "dataset"
if not os.path.exists(datasetFolder):
    os.mkdir(datasetFolder)
if "train.csv" not in  os.listdir(datasetFolder):
    import utilitaire
    utilitaire.download_dataset(datasetFolder)

import polars as pl
import polars.selectors as cs
df = pl.read_csv("dataset/train.csv")

df = df.drop_nulls()

df =  df.drop("Policy Start Date")
df = df.to_dummies(cs.string(), separator="_",  drop_first=True)

y = df['Premium Amount']
X = df.drop('Premium Amount')

import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor

print("Entrainement des modèles")

print("Régression linéaire")
lin_reg = LinearRegression()
lin_reg.fit(X, y)
print("Régression linéaire terminée")

print("Gradient boosting")
gb_model = GradientBoostingRegressor()
gb_model.fit(X, y)
print("Gradient boosting terminé")

print("KNN")
kn_model = KNeighborsRegressor()
kn_model.fit(X, y)
print("KNN terminé")

# Enregistrer les modèles
model_location = rootPath / "models"
if not os.path.exists(model_location):
  os.mkdir(model_location)

import pickle

model_export_names = ["LinearReg_Model.pkl", "GradientB_Model.pkl", "KNN_Model.pkl"]

for model, export_name in zip([lin_reg, gb_model, kn_model], model_export_names):
  with open(model_location / export_name, "wb") as f:
    pickle.dump(model, f)
