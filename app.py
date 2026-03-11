import streamlit as st
from PIL import Image
import os


st.set_page_config(page_title="GEEKSECURE21 | HUB", page_icon="🛡️", layout="wide")


st.markdown("""
    <style>
    /* Fond global sombre et police tech */
    .stApp {
        background-color: #050a14;
        color: #00ccff;
    }
    /* Style des boutons type "Cyber" */
    div.stButton > button {
        background-color: #001a33;
        color: #00ccff;
        border: 2px solid #00ccff;
        border-radius: 10px;
        font-weight: bold;
        box-shadow: 0 0 10px #00ccff;
        transition: 0.3s;
        width: 100%;
        height: 3em;
    }
    div.stButton > button:hover {
        background-color: #00ccff;
        color: #050a14;
        box-shadow: 0 0 25px #00ccff;
    }
    /* Titre avec effet néon */
    .neon-text {
        text-align: center;
        color: #00ccff;
        text-shadow: 0 0 10px #00ccff, 0 0 20px #00ccff;
        font-family: 'Courier New', Courier, monospace;
        font-size: 45px;
        margin-bottom: 0px;
    }
    </style>
    """, unsafe_allow_html=True)


col_l1, col_l2, col_l3 = st.columns([1, 1, 1])
with col_l2:
    if os.path.exists("logo.png"):
        image = Image.open("logo.png")
        st.image(image, width=200)
    else:
        st.error("⚠️ Fichier 'logo.png' introuvable dans le dossier !")


st.markdown('<p class="neon-text">GEEKSECURE21</p>', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>SYSTEM ACCESS : GRANTED ✅</h3>", unsafe_allow_html=True)
st.write(f"<p style='text-align: center; color: #aaaaaa;'>By Babacar SARR - Cyber Engineer 🇸🇳</p>", unsafe_allow_html=True)

st.divider()


st.markdown("### ⚡ SÉLECTIONNEZ VOTRE MODULE DE FORMATION")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 🛡️ SECURITY")
    if st.button("Google Cybersecurity"):
        st.link_button("ACCÉDER AU COURS", "https://www.coursera.org/professional-certificates/google-cybersecurity")
    if st.button("Cisco Academy"):
        st.link_button("ACCÉDER AU PORTAIL", "https://www.netacad.com/portal/learning")

with col2:
    st.markdown("#### 📊 DATA & CLOUD")
    if st.button("Google Data Analytics"):
        st.link_button("ACCÉDER AU COURS", "https://www.coursera.org/professional-certificates/google-data-analytics")
    if st.button("AWS Cloud Essentials"):
        st.link_button("ACCÉDER AU CLOUD", "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials")

with col3:
    st.markdown("#### 🤖 INTELLIGENCE")
    if st.button("Elements of AI"):
        st.link_button("DÉCOUVRIR L'IA", "https://www.elementsofai.fr/")
    if st.button("💰 AIDE FINANCIÈRE"):
        st.link_button("OBTENIR LA GRATUITÉ", "https://www.coursera.org/financial-aid")

st.divider()
st.caption("Terminal sécurisé Geeksecure21 | Guediawaye, Dakar Region")

