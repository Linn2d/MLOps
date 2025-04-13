import requests
import streamlit as st

# URL de l'API
API_URL = "http://server:8000/predict"

# Titre principal
st.set_page_config(page_title="🌸 Prédiction des Iris", layout="centered")
st.title("🌸 Prédiction de la classe d'une fleur Iris")
st.image("image_iris.png", caption="Visualisation des 3 espèces d'Iris", use_container_width=True)

st.write("Remplissez les caractéristiques ci-dessous pour prédire l'espèce.")

# Entrées utilisateur dans deux colonnes
col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input("📏 Longueur du sépale (cm)", min_value=0.0, step=0.1)
    petal_length = st.number_input("📏 Longueur du pétale (cm)", min_value=0.0, step=0.1)

with col2:
    sepal_width = st.number_input("📐 Largeur du sépale (cm)", min_value=0.0, step=0.1)
    petal_width = st.number_input("📐 Largeur du pétale (cm)", min_value=0.0, step=0.1)

# Bouton de prédiction
if st.button("🔍 Prédire la classe"):
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    with st.spinner("Prédiction en cours... ⏳"):
        response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        prediction = response.json()["predicted_class"]
        st.success(f"🌺 La classe prédite est : **{prediction}**")
    else:
        st.error("❌ Une erreur est survenue lors de la prédiction.")
