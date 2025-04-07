import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="ACS Micro Área",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados
st.markdown("""
    <style>
        .block-container { padding-top: 0rem; }

        .custom-header {
            background-color: #1976D2;
            padding: 0.8rem 1rem;
            color: white;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            display: flex;
            align-items: center;
            z-index: 100;
        }

        .custom-header h1 {
            font-size: 1.4rem;
            margin: 0;
            padding-left: 0.8rem;
        }

        .menu-button {
            background-color: #1565C0;
            color: white;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            padding: 0.3rem 0.6rem;
            border-radius: 5px;
            box-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .menu-button:hover {
            background-color: #0D47A1;
        }

        .main-button {
            display: inline-block;
            background-color: #2196F3;
            color: white;
            padding: 0.9rem 1.5rem;
            margin: 0.5rem;
            border-radius: 10px;
            text-align: center;
            font-size: 1rem;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
            transition: background-color 0.3s ease;
            text-decoration: none;
        }

        .main-button:hover {
            background-color: #1976D2;
            text-decoration: none;
        }

        .footer {
            background-color: #1976D2;
            padding: 0.6rem;
            color: white;
            text-align: center;
            position: fixed;
            bottom: 0;
            width: 100%;
            z-index: 100;
        }

        .main-content {
            margin-top: 4.5rem;
            margin-bottom: 3rem;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho com botão hambúrguer funcional com script robusto
st.markdown("""
    <div class="custom-header">
        <button class="menu-button" onclick="openMenu()">&#9776;</button>
        <h1>ACS Micro Área</h1>
    </div>

    <script>
        function openMenu() {
            const sidebarToggle = window.parent.document.querySelector('button[title="Main menu"]');
            if (sidebarToggle) {
                sidebarToggle.click();
            }
        }
    </script>
""", unsafe_allow_html=True)

# Conteúdo principal
st.markdown('<div class="main-content">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown('<a href="/Domicílios" class="main-button">Domicílios</a>', unsafe_allow_html=True)
    st.markdown('<a href="/Famílias" class="main-button">Famílias</a>', unsafe_allow_html=True)
    st.markdown('<a href="/Cidadãos" class="main-button">Cidadãos</a>', unsafe_allow_html=True)

with col2:
    st.markdown('<a href="/Relatórios" class="main-button">Relatórios</a>', unsafe_allow_html=True)
    st.markdown('<a href="/Resumo de Produção" class="main-button">Resumo de Produção</a>', unsafe_allow_html=True)

with col3:
    st.markdown('<a href="/Nascimentos e Óbitos" class="main-button">Nascimentos e Óbitos</a>', unsafe_allow_html=True)
    st.markdown('<a href="/Cartões Espelho" class="main-button">Cartões Espelho</a>', unsafe_allow_html=True)
    st.markdown('<a href="/Laudos e Receitas" class="main-button">Laudos e Receitas</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Rodapé fixo
st.markdown('<div class="footer">Desenvolvido para uso do ACS</div>', unsafe_allow_html=True)
