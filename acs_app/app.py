import streamlit as st

st.set_page_config(page_title="ACS Micro Área", layout="wide")

# Estilo e JS para botão hambúrguer
st.markdown("""
    <style>
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
        .main {margin-top: 70px;}
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
        function abrirMenuLateral() {
            let menuButton = window.parent.document.querySelector('button[kind="header"]');
            if (menuButton) {
                menuButton.click();
            }
        }
    </script>
""", unsafe_allow_html=True)

st.markdown('<button id="openSidebar" onclick="abrirMenuLateral()">☰</button>', unsafe_allow_html=True)
st.markdown('<div class="header">ACS Micro Área</div>', unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown("## Bem-vindo, Ataide!")
st.markdown("### Cadastros")

# Botões com links manuais
def botao_link(nome, emoji, destino):
    st.markdown(f'<a href="/{destino}" class="botao">{emoji} {nome}</a>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    botao_link("Domicílios", "🏠", "Domicílios")
    botao_link("Famílias", "👨‍👩‍👧", "Famílias")
    botao_link("Cidadãos", "🧑‍⚕️", "Cidadãos")

st.markdown("### Análises e Relatórios")
with col2:
    botao_link("Relatórios", "📊", "Relatórios")
    botao_link("Resumo de Produção", "✅", "Resumo de Produção")
    botao_link("Nascimentos e Óbitos", "👶", "Nascimentos e Óbitos")
    botao_link("Cartões Espelho", "🪪", "Cartões Espelho")
    botao_link("Laudos e Receitas", "📄", "Laudos e Receitas")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown('<div class="footer">Desenvolvido para uso profissional do ACS</div>', unsafe_allow_html=True)
