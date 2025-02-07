import streamlit as st
from formulaire import get_forms
from model_helper import get_linear_model
import numpy as np

from dataclasses import asdict

linear_model = get_linear_model()

user_input = get_forms()

st.markdown("### Les données que vous avez saisies")
st.text(user_input)

st.markdown("### Les données converties pour ML")
st.text(user_input.convert_to_mlinput())


mlinput = np.array([*asdict(user_input.convert_to_mlinput())]).reshape(1, -1)

st.markdown(f"Le modèle prédit : {linear_model.predict(mlinput)} ")
