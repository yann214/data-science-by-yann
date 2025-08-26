import streamlit as st
import pandas as pd
import joblib
from pretraitement import pretraitement

# Configuration de la page
st.set_page_config(page_title="Classification du Diabète", layout="wide", page_icon="🩺")

# CSS personnalisé pour un style plus agréable
st.markdown("""
    <style>
    .main {
        background-color: #F0F2F6;
    }
    .title {
        color: #2E8BC0;
        font-size: 36px;
        font-weight: bold;
    }
    .sub-title {
        color: #145DA0;
        font-size: 22px;
    }
    .stButton>button {
        background-color: #2E8BC0;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        margin-top: 10px;
    }
    
    </style>
""", unsafe_allow_html=True)

# Chargement du modèle entraîné
model = joblib.load("Classification_diabete.pkl")

# Titre de l'application
st.markdown('<div class="title">🩺 Application de Classification du Type de Diabète</div>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">📁 Chargez vos données, puis prédisez automatiquement le type de diabète.</p>', unsafe_allow_html=True)
st.markdown("---")

# Étape 1 : Upload du fichier
uploaded_file = st.file_uploader("📂 Charger un fichier CSV ou Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Étape 2 : Lire le fichier
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement du fichier : {e}")
        st.stop()

    # Étape 3 : Afficher les données
    st.markdown("### 🔍 Données chargées")
    st.dataframe(df, use_container_width=True)

    # Étape 4 : Prétraitement
    df_clean = pretraitement(df)

    # Étape 5 : Bouton pour lancer les prédictions
    if st.button("Prédire le type de diabète"):
        try:
            predictions = model.predict(df_clean)
            df_resultats = df.copy()
            df_resultats["🧬 Prédiction"] = predictions

            st.success("✅ Prédictions effectuées avec succès !")
            st.markdown("### 📊 Résultats de la prédiction")
            st.dataframe(df_resultats, use_container_width=True)

            # Télécharger le fichier
            csv_result = df_resultats.to_csv(index=False).encode('utf-8')
            st.download_button("💾 Télécharger les résultats au format XlSX", data=csv_result, file_name="predictions_diabete.xlsx", mime="text/xlsx")
        except Exception as e:
            st.error(f"❌ Erreur pendant la prédiction : {e}")
