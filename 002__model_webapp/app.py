import streamlit as st
from formulaire import get_forms

user_input = get_forms()

st.markdown("### Les données que vous avez saisies")
st.text(user_input)

st.markdown("### Les données converties pour ML")
st.text(user_input.convert_to_mlinput())