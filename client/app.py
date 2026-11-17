import os
from pathlib import Path

import requests
import streamlit as st

BASE_DIR = Path(__file__).parent
def get_api_url() -> str:
    if os.getenv("API_URL"):
        return os.getenv("API_URL")
    try:
        return st.secrets["API_URL"]
    except (KeyError, FileNotFoundError, st.errors.StreamlitSecretNotFoundError):
        return "http://localhost:8000/predict"


API_URL = get_api_url()

st.set_page_config(page_title="🌸 Prédiction des Iris", layout="centered")
st.title("🌸 Prédiction de la classe d'une fleur Iris")
st.image(BASE_DIR / "image_iris.png", caption="Visualisation des 3 espèces d'Iris", width="stretch")

st.write("Remplissez les caractéristiques ci-dessous pour prédire l'espèce.")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input("📏 Longueur du sépale (cm)", min_value=0.0, step=0.1)
    petal_length = st.number_input("📏 Longueur du pétale (cm)", min_value=0.0, step=0.1)

with col2:
    sepal_width = st.number_input("📐 Largeur du sépale (cm)", min_value=0.0, step=0.1)
    petal_width = st.number_input("📐 Largeur du pétale (cm)", min_value=0.0, step=0.1)

if st.button("🔍 Prédire la classe"):
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }

    try:
        with st.spinner("Prédiction en cours... ⏳"):
            response = requests.post(API_URL, json=payload, timeout=60)
        response.raise_for_status()
        prediction = response.json()["predicted_class"]
        st.success(f"🌺 La classe prédite est : **{prediction}**")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Impossible de joindre l'API : {e}")