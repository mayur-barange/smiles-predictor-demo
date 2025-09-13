import streamlit as st
import random

st.set_page_config(page_title="SMILES Predictor", layout="centered")
st.title("🧪 SMILES → Solubility (Demo Mode)")

smiles = st.text_input("Enter SMILES string:", "CCO")

if st.button("Predict"):
    # Generate a dummy "prediction"
    pred = round(random.uniform(-3, 3), 3)
    st.success(f"Predicted solubility (log mol/L): {pred}")
    st.info("⚠️ Note: This is a demo version without the trained BiLSTM model.")

