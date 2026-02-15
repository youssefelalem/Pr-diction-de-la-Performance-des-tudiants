import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="EduPredictors | Full Student Data", layout="wide")

st.title("🎓 Detailed Student Profile Entry")
st.markdown("Enter all relevant data from the Moroccan Student Dataset for accurate prediction.")

# Organizing the fields into 4 Tabs based on the CSV structure
tab1, tab2, tab3, tab4 = st.tabs([
    "Identification & Personal", 
    "Socio-Economic Factors", 
    "Academic Background", 
    "Health & Living Conditions"
])

# --- TAB 1: Identification & Personal ---
with tab1:
    st.header("Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Massar Code")
        st.text_input("First Name (prenom)")
        st.text_input("Last Name (nom)")
        st.selectbox("Gender (sexe)", ["M", "F"])
    with col2:
        st.number_input("Age", min_value=15, max_value=25, value=17)
        st.selectbox("Region", ["Casablanca-Settat", "Rabat-Salé-Kénitra", "Fès-Meknès", "Marrakech-Safi", "Oriental"])
        st.selectbox("Zone", ["Urbain", "Rural"])
        st.text_input("Province")

# --- TAB 2: Socio-Economic Factors ---
with tab2:
    st.header("Family & Economic Background")
    col3, col4 = st.columns(2)
    with col3:
        st.number_input("Family Income (revenu familial)", min_value=0)
        st.selectbox("Father's Profession (profession pere)", ["Enseignant", "Commercant", "Ouvrier", "Sans emploi", "Autre"])
        st.selectbox("Mother's Profession (profession mere)", ["Foyer", "Enseignante", "Fonctionnaire", "Autre"])
    with col4:
        st.selectbox("Parental Status (statut parental)", ["Maries", "Divorces", "Veuf"])
        st.number_input("Number of Siblings (nombre freres, soeurs)", 0, 15, 2)
        st.checkbox("Internet Access (internet)")
        st.checkbox("Personal Room (chambre personnelle)")

# --- TAB 3: Academic Background (The core for Task ED-13) ---
with tab3:
    st.header("Academic Performance Data")
    col5, col6 = st.columns(2)
    with col5:
        st.selectbox("School Level (niveau)", ["2BAC", "1BAC", "Tronc Commun"])
        st.selectbox("Filiere", ["Sciences Physiques", "SVT", "Sciences Maths", "Lettres", "Eco"])
        st.number_input("Last Year Average (moyenne annuelle)", 0.0, 20.0, 10.0)
    with col6:
        st.slider("Target Performance Score (performance cible)", 0, 100, 75)
        st.number_input("Absence Days", 0, 50, 0)
        st.selectbox("Mention (Last Year)", ["Passable", "Assez Bien", "Bien", "Tres Bien"])

# --- TAB 4: Health & Living Conditions ---
with tab4:
    st.header("Lifestyle & Environment")
    col7, col8 = st.columns(2)
    with col7:
        st.selectbox("Transport Mode (moyen transport)", ["Bus", "A pied", "Transport scolaire", "Voiture", "Velo"])
        st.number_input("Commute Time (min)", 0, 120, 20)
    with col8:
        st.selectbox("General Health (etat sante)", ["Bon", "Moyen", "Fragile"])
        st.checkbox("Has Scholarship (bourse)")

# Final Action
st.markdown("---")
if st.button("Analyze & Predict Outcome", use_container_width=True):
    st.balloons()
    st.success("All data points have been collected. Ready for model inference.")