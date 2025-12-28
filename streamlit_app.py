import streamlit as st
import random

# Configurazione stile (Pulsante Arancione)
st.markdown("""
    <style>
    .stButton>button {
        background-color: #FF8C00;
        color: white;
        border-radius: 20px;
        height: 3em;
        width: 100%;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FF7F50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🍳 Cosa Cucino Oggi?")

# Database iniziale di ricette
if 'ricette' not in st.session_state:
    st.session_state.ricette = [
        {"nome": "Pasta al Pomodoro", "ing": ["Pasta", "Pomodoro"]},
        {"nome": "Omelette veloce", "ing": ["Uova", "Formaggio"]},
        {"nome": "Insalata Tonno e Mais", "ing": ["Tonno", "Mais", "Insalata"]}
    ]

# Sezione Aggiunta Ingredienti
with st.expander("➕ Aggiungi una nuova ricetta"):
    nuovo_nome = st.text_input("Nome piatto")
    nuovi_ing = st.text_input("Ingredienti (separati da virgola)")
    if st.button("Salva Ricetta"):
        if nuovo_nome and nuovi_ing:
            st.session_state.ricette.append({"nome": nuovo_nome, "ing": nuovi_ing.split(",")})
            st.success("Ricetta salvata!")

st.write("---")

# Il Pulsante Arancione
if st.button("COSA CUCINO OGGI?"):
    scelta = random.choice(st.session_state.ricette)
    st.balloons()
    st.subheader(f"Ti suggerisco: **{scelta['nome']}**")
    st.write(f"Ingredienti necessari: {', '.join(scelta['ing'])}")

# Visualizza ricette salvate
if st.checkbox("Mostra tutte le mie ricette"):
    for r in st.session_state.ricette:
        st.write(f"• {r['nome']}")
