import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="ACS Micro Área", layout="wide")

# --- Estilo personalizado ---
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
        }
        .css-18e3th9 {
            padding-top: 2rem;
        }
        .css-1d391kg {
            padding-top: 2rem;
        }
        header {
            background-color: #007BFF;
            padding: 10px 16px;
            color: white;
            font-size: 24px;
            font-weight: bold;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 999;
        }
        footer {
            background-color: #007BFF;
            padding: 8px;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: white;
        }
        .stButton > button {
            background-color: #e0e0e0;
            color: black;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 1em;
            margin: 0.3em;
            text-decoration: none;
        }
        .stButton > button:hover {
            background-color: #d0d0d0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<header>ACS Micro Área</header>', unsafe_allow_html=True)
st.markdown('<div style="height:60px;"></div>', unsafe_allow_html=True)  # Espaço abaixo do cabeçalho

# Menu lateral com "Página Inicial"
with st.sidebar:
    st.markdown("### Menu")
    menu = option_menu(
        menu_title=None,
        options=[
            "Página Inicial",
            "Cartões Espelho",
            "Laudos e Receitas"
        ],
        icons=["house", "card-text", "file-earmark-medical"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"background-color": "#343a40", "padding": "5px"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"color": "white", "font-size": "16px", "text-align": "left"},
            "nav-link-selected": {"background-color": "#007BFF"},
        }
    )

if menu == "Cartões Espelho":
    st.switch_page("pages/7_Cartões_Espelho.py")
elif menu == "Laudos e Receitas":
    st.switch_page("pages/8_Laudos_Receitas.py")

# Conteúdo da Página Inicial
st.markdown("### Acesse uma das seções do aplicativo:")
col1, col2 = st.columns(2)

with col1:
    if st.button("Domicílios"):
        st.switch_page("pages/1_Domicílios.py")
    if st.button("Cidadãos"):
        st.switch_page("pages/3_Cidadãos.py")
    if st.button("Resumo de Produção"):
        st.switch_page("pages/5_Resumo_de_Produção.py")
    if st.button("Nascimentos e Óbitos"):
        st.switch_page("pages/6_Nascimentos_e_Óbitos.py")

with col2:
    if st.button("Famílias"):
        st.switch_page("pages/2_Famílias.py")
    if st.button("Relatórios"):
        st.switch_page("pages/4_Relatórios.py")

# Rodapé fixo
st.markdown('<footer>Desenvolvido para uso em campo por ACS</footer>', unsafe_allow_html=True)
