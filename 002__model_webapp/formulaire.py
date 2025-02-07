import streamlit as st
from objets import UserInput

"""
Cette fonction permet d'afficher un formulaire Streamlit et de retourner les données
saisies par l'utilisateur en tant qu'instance de UserInput
"""
def get_forms() -> UserInput:
    with st.sidebar:
        age = st.number_input("Âge", min_value=15, max_value=100)
        gender = st.radio("Sexe", ["Homme", "Femme"])
        annual_revenue = st.number_input("Revenu annuel ($)", min_value=0)
        marital_status = st.selectbox("Situation matrimoniale", ["Marié", "Célibataire", "Divorcé"])
        number_dependants = st.number_input("Nombre de personnes à charge", min_value=0, max_value=50)
        education_level = st.selectbox("Niveau d'éducation", ["Lycée", "Licence", "Master", "Doctorat"])
        occupation = st.selectbox("Situation professionnelle", ["Sans emploi", "Autoentrepeneur", "Employé"])
        health_score = st.number_input("Score santé", min_value=0)
        location = st.selectbox("Milieu géographique", ["Rural", "Semi-urbain", "Urbain"])
        policy_type = st.selectbox("Police d'assurance", ["Complet", "Premium", "Basic"])
        previous_claims = st.number_input("Nombre de réclamations", min_value=0)
        vehicle_age = st.number_input("Âge du véhicule", min_value=0)
        insurance_duration = st.number_input("Durée de l'assurance", min_value=0)
        smoking_status = st.radio("Fumeur", ["Non", "Oui"])
        exercise_frequency = st.selectbox("Fréquence d'activité sportive", ["Mensuel", "Hebdomadaire", "Quotidien", "Rarement"])
        property_type = st.selectbox("Type de propriété", ["Maison", "Appartement", "Copropriété"])

        user_input = UserInput(
            age,
            gender,
            annual_revenue,
            marital_status,
            number_dependants,
            education_level,
            occupation,
            health_score,
            location,
            policy_type,
            previous_claims,
            vehicle_age,
            insurance_duration,
            smoking_status,
            exercise_frequency,
            property_type
        )
    return user_input