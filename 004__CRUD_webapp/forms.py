import streamlit as st
import models
# Formulaire pour ajouter une transaction

def get_transation_form() -> models.Transaction:
    type = st.sidebar.selectbox("Type", ["Revenu", "Dépense"])
    categorie = st.sidebar.text_input("Catégorie (ex: Loyer, Salaire, Bourse)")
    montant = st.sidebar.number_input("Montant (€)", min_value=0.0, step=0.1)
    transaction = models.Transaction(type, categorie, montant)
    return transaction