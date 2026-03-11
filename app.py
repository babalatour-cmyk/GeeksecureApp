import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Geeksecure21", page_icon="🛡️")

# Design et Logo
st.title("🛡️ GEEKSECURE21")
st.subheader("Par Babacar SARR - Sécurisons votre futur 🇸🇳")

st.write("Bienvenue sur votre plateforme de certifications gratuites.")

# Création des sections
st.info("Sélectionnez votre parcours pour commencer :")

col1, col2 = st.columns(2)

with col1:
    if st.button("🛡️ Cybersécurité (Google)"):
        st.write("[Cliquez ici](https://www.coursera.org/professional-certificates/google-cybersecurity)")
    
    if st.button("📊 Data Analytics"):
        st.write("[Cliquez ici](https://www.coursera.org/professional-certificates/google-data-analytics)")

with col2:
    if st.button("💰 Aide Financière"):
        st.write("[Cliquez ici](https://www.coursera.org/financial-aid)")
        
    if st.button("🌐 Cisco Academy"):
        st.write("[Cliquez ici](https://www.netacad.com/portal/learning)")

st.divider()
st.caption("© 2026 Geeksecure21 | Guédiawaye, Sénégal")