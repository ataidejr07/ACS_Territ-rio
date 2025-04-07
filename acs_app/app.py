import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="ACS Micro Área", layout="wide")

# Estilo e JS para botão hambúrguer
st.markdown("""
    <style>
        /* Header fixo */
        .header {
            background-color: #0056b3;
            color: white;
            padding: 10px 20px;
            font-size: 24px;
            font-weight: bold;
            display: flex;
            align-items: center;
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
        }

        /* Espaço abaixo do cabeçalho fixo */
        .main {margin-top: 70px;}

        /* Rodapé fixo */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #0056b3;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            z-index: 9999;
        }

        /* Estilo dos botões */
        .botao {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            display: block;
            text-decoration: none !important;
            color: black !important;
            font-size: 18px;
            font-weight: bold;
        }

        /* Menu lateral */
        section[data-testid="stSidebar"] {
            background-color: #1e1e1e;
        }

        section[data-testid="stSidebar"] .block-container {
            padding: 1rem;
        }

        section[data-testid="stSidebar"] a {
            color: white;
            font-weight: bold;
        }

        /* Botão menu flutuante */
        #openSidebar {
            position: fixed;
            top: 12px;
            left: 15px;
            background-color: transparent;
            border: none;
            color: white;
            font-size: 26px;
            z-index: 1001;
        }
    </style>

    <script>
        // Função para clicar no ícone do menu da Streamlit
        function abrirMenuLateral() {
            let menuButton = window.parent.document.querySelector('button[kind="header"]');
            if (menuButton) {
                menuButton.click();
            }
        }
    </script>
""", unsafe_allow_html=True)

# Botão hamburguer funcional
st.markdown('<button id="openSidebar" onclick="abrirMenuLateral()">☰</button>', unsafe_allow_html=True)

# Cabeçalho fixo
st.markdown('<div class="header">ACS Micro Área</div>', unsafe_allow_html=True)

# Conteúdo principal
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown("## Bem-vindo, Ataide!")
st.markdown("### Cadastros")

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    if st.button("🏠 Domicílios"):
        switch_page("Domicílios")
    if st.button("👨‍👩‍👧 Famílias"):
        switch_page("Famílias")
    if st.button("🧑‍⚕️ Cidadãos"):
        switch_page("Cidadãos")

st.markdown("### Análises e Relatórios")
with col2:
    if st.button("📊 Relatórios"):
        switch_page("Relatórios")
    if st.button("✅ Resumo de Produção"):
        switch_page("Resumo de Produção")
    if st.button("👶 Nascimentos e Óbitos"):
        switch_page("Nascimentos e Óbitos")
    if st.button("🪪 Cartões Espelho"):
        switch_page("Cartões Espelho")
    if st.button("📄 Laudos e Receitas"):
        switch_page("Laudos e Receitas")
st.markdown("</div>", unsafe_allow_html=True)

# Rodapé fixo
st.markdown('<div class="footer">Desenvolvido para uso profissional do ACS</div>', unsafe_allow_html=True)
