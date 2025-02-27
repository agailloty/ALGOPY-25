import streamlit as st
from formulaire import get_forms
import model_helper as models
import numpy as np

from dataclasses import asdict

LINEAR_REGRESSION = "Régression linéaire"
GRADIENT_BOOSTING = "Gradient Boosting"
KNN = "KNN"

selected_model = st.selectbox("Choisir modèle prédiction",
                              ["--", LINEAR_REGRESSION, GRADIENT_BOOSTING, KNN])

if selected_model == LINEAR_REGRESSION:
    model = models.get_linear_model()
elif selected_model == GRADIENT_BOOSTING:
    model = models.get_boosting_model()
else :
    model = models.get_knn_model()


user_input = get_forms()

mlinput = np.array([*asdict(user_input.convert_to_mlinput()).values()]).reshape(1, -1)

prediction = ""

def predict_model():
    if selected_model != "--":
        value_prediction = model.predict(mlinput)
        global prediction
        prediction = f"Le modèle {selected_model} prédit : {value_prediction}"
        print(prediction)

if selected_model != "--":
    value_prediction = model.predict(mlinput)
    prediction = f"Le modèle {selected_model} prédit : {value_prediction}"
    st.markdown(f"### {prediction}")

if st.checkbox("Comparaison"):
    st.markdown("### Voici une comparaison de ce que prédit chaque modèle")

    for model, prediction in zip([LINEAR_REGRESSION, GRADIENT_BOOSTING, KNN],
                                 [models.get_linear_model().predict(mlinput),
                                 models.get_boosting_model().predict(mlinput),
                                 models.get_knn_model().predict(mlinput)]) :
        
        st.markdown(f"#### {model} : {prediction}")
        
