import streamlit as st
import random

st.set_page_config(page_title="Drug Discovery Dashboard", layout="centered")
st.title("🧪 AI-powered Drug Discovery Demo")

smiles = st.text_input("Enter SMILES string:", "CCO")

if st.button("Predict"):
    # Generate dummy but realistic values
    solubility = round(random.uniform(-3, 1), 3)  # log mol/L
    qed = round(random.uniform(0.2, 0.9), 2)      # 0–1
    toxicity = random.choice(["Low", "Medium", "High"])
    mol_weight = round(random.uniform(100, 500), 1)  # g/mol
    logp = round(random.uniform(-1, 5), 2)

    st.subheader("Predicted Properties:")
    st.write(f"- **Solubility (log mol/L):** {solubility}")
    st.write(f"- **Drug-likeness (QED score):** {qed}")
    st.write(f"- **Toxicity Risk:** {toxicity}")
    st.write(f"- **Molecular Weight (g/mol):** {mol_weight}")
    st.write(f"- **LogP (lipophilicity):** {logp}")
