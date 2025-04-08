import streamlit as st
from streamlit_option_menu import option_menu

# === CONFIGURAÇÕES GERAIS ===
st.set_page_config(
    page_title="ACS Micro Área",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === ESCONDER MENU LATERAL PADRÃO DO STREAMLIT ===
hide_menu_style = """
    <style>
        #MainMenu, header, footer {visibility: hidden;}
        [data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# === BARRA SUPERIOR AZUL FIXA COM TÍTULO ===
st.markdown("""
    <style>
        .header-bar {
            background-color: #0d6efd;
            color: white;
            padding: 1rem;
            font-size: 1.4rem;
            font-weight: bold;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .main-content {
            padding-top: 80px;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #0d6efd;
            color: white;
            text-align: center;
            padding: 8px;
            font-size: 0.9rem;
        }
        .stButton>button {
            font-size: 18px;
            color: black;
            text-decoration: none;
        }
    </style>
    <div class="header-bar">ACS Micro Área</div>
    <div class="main-content">
""", unsafe_allow_html=True)

# === MENU LATERAL PERSONALIZADO ===
with st.sidebar:
    st.markdown("## Menu")
    selected = option_menu(
        menu_title=None,
        options=["Página Inicial", "Cartões Espelho", "Laudos e Receitas"],
        icons=["house", "card-text", "file-earmark-medical"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"background-color": "#1e1e1e", "padding": "10px", "border-radius": "10px"},
            "icon": {"color": "#ffffff", "font-size": "20px"},
            "nav-link": {
                "color": "#ffffff",
                "font-size": "18px",
                "text-align": "left",
                "margin": "5px 0",
                "--hover-color": "#0d6efd"
            },
            "nav-link-selected": {"background-color": "#0d6efd", "font-weight": "bold"}
        }
    )
    if selected == "Cartões Espelho":
        st.switch_page("pages/7_🧾_Cartões Espelho.py")
    elif selected == "Laudos e Receitas":
        st.switch_page("pages/8_📝_Laudos e Receitas.py")

# === CONTEÚDO PRINCIPAL COM BOTÕES DE NAVEGAÇÃO ===
st.markdown("## Acesse uma das seções do aplicativo:")
st.page_link("pages/1_📄_Domicílios.py", label="Domicílios", icon=None)
st.page_link("pages/3_👤_Cidadãos.py", label="Cidadãos", icon=None)
st.page_link("pages/5_📊_Resumo de Produção.py", label="Resumo de Produção", icon=None)
st.page_link("pages/6_⚰️_Nascimentos e Óbitos.py", label="Nascimentos e Óbitos", icon=None)
st.page_link("pages/2_👪_Famílias.py", label="Famílias", icon=None)
st.page_link("pages/4_📈_Relatórios.py", label="Relatórios", icon=None)

# === RODAPÉ AZUL FIXO ===
st.markdown("""
    </div>
    <div class="footer">
        Desenvolvido para uso em campo | ACS Micro Área
    </div>
""", unsafe_allow_html=True)
