import streamlit as st

with st.sidebar:
    age = st.number_input("Âge", min_value=15, max_value=100)
    gender = st.selectbox("Sexe", ["Homme", "Femme"])
    annual_revenue = st.number_input("Revenu annuel ($)", min_value=0)
    marital_status = st.selectbox("Situation matrimoniale", ["Marié", "Célibataire", "Divorcé"])
    number_dependants = st.number_input("Nombre de personnes à charge", min_value=0, max_value=50)
    education_level = st.selectbox("Niveau d'éducation", ["Lycée", "Licence", "Master", "Doctorat"])
    occupation = st.selectbox("Situation professionnelle", ["Sans emploi", "Autoentrepeneur", "Employé"])
    health_score = st.number_input("Score santé", min_value=0)
