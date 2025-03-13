import streamlit as st
from models import Eleve
import service

@st.dialog("Inscrire un(e) élève", width="large")
def registration_form():
    st.title("Formulaire d'inscription des élèves")
    col1, col2 = st.columns(2)

    with col1:
        nom = st.text_input("Nom")
        date_naissance = st.date_input("Date de naissance")
        classe = st.text_input("Classe")
        telephone = st.text_input("Téléphone")
    with col2:
        prenom = st.text_input("Prénom")
        adresse = st.text_area("Adresse")
        email = st.text_input("Email")
    
    photo = st.file_uploader("Photo", type=["png", "jpg", "jpeg"])

    if st.button("Inscrire"):
        try:
            if nom and prenom and date_naissance and classe:
                photo_data = photo.read() if photo else None
                eleve = Eleve(nom, prenom, date_naissance, adresse, classe, telephone, email, photo_data)
                service.create_eleve(eleve)
                st.success("Élève enregistré avec succès!")
            else:
                st.error("Veuillez remplir tous les champs obligatoires.")
        except Exception as e:
            st.error(e)
            print(e)

def student_display_form():
    pass