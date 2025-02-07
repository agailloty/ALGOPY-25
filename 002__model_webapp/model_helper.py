from pathlib import Path
import os
import pickle

rootPath = Path(__file__).parent

modelPaths = rootPath.parent / "002__model_training" / "models"

# print(os.listdir(modelPaths))

def get_linear_model():
    with open(modelPaths / 'LinearReg_Model.pkl', "rb") as f:
        model = pickle.load(f)
        return model