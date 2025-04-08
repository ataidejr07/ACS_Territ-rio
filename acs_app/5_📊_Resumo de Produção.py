
import streamlit as st

st.markdown(f"<h2 style='color: white;'>Resumo de Produção</h2>", unsafe_allow_html=True)

if st.button("Voltar à Página Inicial"):
    st.switch_page("app.py")
