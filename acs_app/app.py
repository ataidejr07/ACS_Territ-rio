import streamlit as st
from streamlit_option_menu import option_menu
import base64

st.set_page_config(layout="wide")

# ======== ESTILOS PERSONALIZADOS ========
st.markdown("""
    <style>
        /* Cabeçalho fixo */
        .header {
            background-color: #0056b3;
            padding: 10px 20px;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 999;
            display: flex;
            align-items: center;
        }

        .header h1 {
            color: white;
            font-size: 20px;
            margin: 0;
            padding-left: 10px;
        }

        /* Rodapé fixo */
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #0056b3;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 12px;
            z-index: 999;
        }

        /* Conteúdo com padding para não ficar atrás do cabeçalho e rodapé */
        .main-content {
            padding-top: 70px;
            padding-bottom: 60px;
        }

        /* Botões principais */
        .main-button {
            display: block;
            width: 100%;
            padding: 15px;
            background-color: white;
            border-radius: 15px;
            font-size: 18px;
            color: black;
            text-decoration: none;
            border: none;
            margin-bottom: 15px;
            text-align: left;
        }

        .main-button:hover {
            background-color: #e6e6e6;
        }

        /* Menu lateral */
        .sidebar .sidebar-content {
            background-color: #333;
        }

        .css-1d391kg, .css-1d391kg:hover {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# ======== CABEÇALHO FIXO ========
st.markdown("""
    <div class="header">
        <span style="font-size: 24px;">☰</span>
        <h1>ACS Micro Área</h1>
    </div>
""", unsafe_allow_html=True)

# ======== CONTEÚDO PRINCIPAL ========
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.markdown("## Bem-vindo, Ataide!")
st.markdown("### Cadastros")

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🏠 Domicílios", key="dom", help="Abrir página de Domicílios", use_container_width=True):
        st.switch_page("pages/1_Domicílios.py")
    if st.button("👨‍👩‍👧 Famílias", key="fam", use_container_width=True):
        st.switch_page("pages/2_Famílias.py")
    if st.button("🧒 Cidadãos", key="cid", use_container_width=True):
        st.switch_page("pages/3_Cidadãos.py")

with col2:
    st.markdown("### Análises e Relatórios")
    if st.button("📊 Relatórios", key="rel", use_container_width=True):
        st.switch_page("pages/4_Relatórios.py")
    if st.button("✅ Resumo de Produção", key="res", use_container_width=True):
        st.switch_page("pages/5_Resumo_de_Produção.py")

# ======== MENU LATERAL CUSTOMIZADO ========
with st.sidebar:
    selected = option_menu("Menu", ["Cartões Espelho", "Laudos e Receitas"],
                           icons=["card-text", "file-earmark-medical"],
                           menu_icon="list", default_index=0,
                           styles={
                               "container": {"background-color": "#333"},
                               "icon": {"color": "white", "font-size": "20px"},
                               "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin": "5px"},
                               "nav-link-selected": {"background-color": "#0056b3"}
                           })

    if selected == "Cartões Espelho":
        st.switch_page("pages/6_Cartões_Espelho.py")
    elif selected == "Laudos e Receitas":
        st.switch_page("pages/7_Laudos_e_Receitas.py")

# ======== RODAPÉ FIXO ========
st.markdown("""
    </div> <!-- Fecha main-content -->
    <div class="footer">
        Desenvolvido para uso profissional em campo — ACS Micro Área
    </div>
""", unsafe_allow_html=True)
