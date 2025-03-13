import streamlit as st
import forms
import service

st.set_page_config(layout="wide")

service.init_database()

st.header("Ecole primaire d'Angers")

col1, col2, col3 = st.columns(3)

with col3:
    if st.button("Inscrire un(e) élève"):
        forms.registration_form()