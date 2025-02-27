from pathlib import Path
import pickle

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor

rootPath = Path(__file__).parent

modelPaths = rootPath.parent / "002__model_training" / "models"

def get_linear_model() -> LinearRegression:
    with open(modelPaths / 'LinearReg_Model.pkl', "rb") as f:
        model = pickle.load(f)
        return model

def get_boosting_model() -> GradientBoostingRegressor:
    with open(modelPaths / 'GradientB_Model.pkl', "rb") as f:
        model = pickle.load(f)
        return model
    
def get_knn_model() -> KNeighborsRegressor:
    with open(modelPaths / 'KNN_Model.pkl', "rb") as f:
        model = pickle.load(f)
        return model