import streamlit as st
age = st.number_input("Âge", min_value=15, max_value=100)
gender = st.selectbox("Sexe", ["Homme", "Femme"])
annual_revenue = st.number_input("Revenu annuel ($)", min_value=0)
marital_status = st.selectbox("Situation matrimoniale", ["Marié", "Célibataire", "Divorcé"])