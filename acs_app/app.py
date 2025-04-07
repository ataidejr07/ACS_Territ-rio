import streamlit as st

# Configuração da página
st.set_page_config(page_title="ACS Micro Área", layout="wide")

# Estilo CSS customizado
st.markdown("""
<style>
    /* Zera margens padrão */
    .main {
        padding: 0 !important;
    }

    /* Cabeçalho fixo */
    .header {
        background-color: #0056b3;
        color: white;
        padding: 10px 16px;
        font-size: 20px;
        font-weight: bold;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    /* Botão do menu */
    .menu-button {
        background-color: #003d80;
        color: white;
        border: none;
        padding: 6px 12px;
        font-size: 20px;
        border-radius: 8px;
        cursor: pointer;
        box-shadow: 1px 1px 4px rgba(0,0,0,0.4);
    }

    /* Container do conteúdo principal */
    .content {
        margin-top: 70px;
        margin-bottom: 60px;
        padding: 0 16px;
    }

    /* Rodapé fixo */
    .footer {
        background-color: #0056b3;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        z-index: 9999;
    }

    /* Estilo dos botões principais */
    .custom-button {
        display: block;
        width: 100%;
        padding: 14px 20px;
        margin: 8px 0;
        font-size: 18px;
        font-weight: bold;
        text-align: left;
        background-color: #ffffff;
        border: 2px solid #ccc;
        border-radius: 10px;
        transition: 0.3s;
    }

    .custom-button:hover {
        background-color: #f0f0f0;
    }

    /* Menu lateral personalizado */
    .sidebar-container {
        position: fixed;
        top: 60px;
        left: 0;
        width: 250px;
        background-color: #1e1e1e;
        color: white;
        padding: 15px;
        border-right: 2px solid #444;
        z-index: 9998;
        display: none;
    }

    .menu-visible {
        display: block !important;
    }

    .sidebar-button {
        background: none;
        border: none;
        color: white;
        text-align: left;
        padding: 10px 5px;
        font-size: 16px;
        cursor: pointer;
        width: 100%;
    }

    .sidebar-button:hover {
        background-color: #333;
    }

    /* Ajuste de responsividade */
    @media (max-width: 768px) {
        .custom-button {
            font-size: 16px;
            padding: 12px;
        }

        .header {
            font-size: 18px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Script para o menu lateral (requer streamlit_javascript se quiser usar JS no futuro)
menu_html = """
<div class="header">
    <span>ACS Micro Área</span>
    <button class="menu-button" onclick="document.querySelector('.sidebar-container').classList.toggle('menu-visible')">☰</button>
</div>

<div class="sidebar-container">
    <button class="sidebar-button">🗂️ Cartões Espelho</button>
    <button class="sidebar-button">📄 Laudos e Receitas</button>
</div>
"""
st.markdown(menu_html, unsafe_allow_html=True)

# Conteúdo principal
st.markdown('<div class="content">', unsafe_allow_html=True)

st.markdown("### Bem-vindo, Ataide!")
st.markdown("#### Cadastros")
st.markdown('<button class="custom-button">🏡 Domicílios</button>', unsafe_allow_html=True)
st.markdown('<button class="custom-button">👨‍👩‍👧‍👦 Famílias</button>', unsafe_allow_html=True)
st.markdown('<button class="custom-button">🧑 Cidadãos</button>', unsafe_allow_html=True)

st.markdown("#### Análises e Relatórios")
st.markdown('<button class="custom-button">📊 Relatórios</button>', unsafe_allow_html=True)
st.markdown('<button class="custom-button">📈 Resumo de Produção</button>', unsafe_allow_html=True)
st.markdown('<button class="custom-button">👶⚰️ Nascimentos e Óbitos</button>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Rodapé
st.markdown('<div class="footer">Desenvolvido para ACS</div>', unsafe_allow_html=True)
