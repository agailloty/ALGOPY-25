import streamlit as st
import forms
import service

st.set_page_config(layout="wide")

service.init_database()

all_eleves = service.read_all_eleve()
eleve_count = len(all_eleves)

def display_student_choice(eleve) -> str:
    return f"{eleve.nom} - {eleve.prenom} - {eleve.classe}"

col1, col2 = st.columns([3, 1])

with col1:
    student_to_display = st.selectbox("Consulter la fiche d'un élève", all_eleves, None, 
                format_func=display_student_choice)

    if eleve_count > 0 and student_to_display is not None:
        leftb, midb, rightb = st.columns(3)
        midb.button("Supprimer" , icon=":material/delete:")

    if eleve_count > 0 and student_to_display is not None:
        forms.student_display_form(student_to_display)

with col2:
    if st.button("Inscrire un(e) élève", icon=":material/add:"):
        forms.registration_form()