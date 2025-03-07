import streamlit as st
from forms import get_transation_form
import service
import models


# Interface utilisateur
st.title("📊 Simulateur de Budget Étudiant")
st.sidebar.header("Ajouter une transaction")

service.init_database()

transaction = get_transation_form()

if st.sidebar.button("Ajouter"):
    if transaction.categorie and transaction.montant > 0:
        service.save_data(transaction)
        st.sidebar.success("Transaction ajoutée !")
    else:
        st.sidebar.error("Veuillez remplir tous les champs.")

# Formulaire pour importer un fichier CSV
st.sidebar.header("Importer des transactions depuis un CSV")
uploaded_file = st.sidebar.file_uploader("Choisir un fichier CSV", type="csv")

if uploaded_file is not None:
    new_data = service.import_csv(uploaded_file)
    st.sidebar.subheader("Aperçu des données importées")
    st.sidebar.dataframe(new_data)
    if st.sidebar.button("Importer"):
        for index, row in new_data.iterrows():
            new_transaction = models.Transaction(type=row['type'], categorie=row['categorie'], montant=row['montant'])
            service.save_data(new_transaction)
        st.sidebar.success("Transactions importées depuis le CSV !")

# Afficher les données
df = service.load_data()
st.subheader("📌 Transactions enregistrées")
st.dataframe(df)

# Calcul du solde total
solde = df[df["type"] == "Revenu"]["montant"].sum() - df[df["type"] == "Dépense"]["montant"].sum()
st.metric("💰 Solde total", f"{solde:.2f} €")