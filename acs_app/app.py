import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ACS Micro Área", layout="wide")

# CSS customizado para cabeçalho, rodapé e botões
st.markdown("""
    <style>
        /* Cabeçalho azul fixo */
        .header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #1f77b4;
            color: white;
            padding: 10px 16px;
            font-size: 20px;
            z-index: 1000;
        }

        /* Rodapé azul fixo */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #1f77b4;
            color: white;
            text-align: center;
            padding: 8px;
            font-size: 14px;
            z-index: 1000;
        }

        /* Espaçamento para conteúdo não ficar atrás do header/rodapé */
        .main {
            margin-top: 60px;
            margin-bottom: 50px;
        }

        /* Estilo dos botões principais */
        .button {
            background-color: white;
            color: black;
            padding: 12px;
            border-radius: 15px;
            font-weight: bold;
            font-size: 18px;
            text-align: left;
            width: 100%;
            border: none;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho fixo
st.markdown('<div class="header">ACS Micro Área</div>', unsafe_allow_html=True)

# Botão hambúrguer funcional no canto superior esquerdo
components.html("""
    <div style="position: fixed; top: 10px; left: 10px; z-index: 1001;">
        <button onclick="openSidebar()" style="
            background-color: transparent;
            border: none;
            font-size: 28px;
            color: white;
            cursor: pointer;
        ">☰</button>
    </div>
    <script>
        function openSidebar() {
            const iframe = window.parent.document;
            const buttons = iframe.querySelectorAll('button');
            buttons.forEach(btn => {
                if (btn.innerText.includes('☰') || btn.getAttribute('aria-label') === 'menu') {
                    btn.click();
                }
            });
        }
    </script>
""", height=0)

# Conteúdo principal com espaçamento
st.markdown('<div class="main">', unsafe_allow_html=True)

st.markdown("## Bem-vindo, Ataide!")
st.markdown("### Cadastros")

# Botões para as páginas
col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Domicílios", use_container_width=True):
        st.switch_page("pages/Domicílios.py")

    if st.button("👨‍👩‍👧 Famílias", use_container_width=True):
        st.switch_page("pages/Famílias.py")

    if st.button("🧒 Cidadãos", use_container_width=True):
        st.switch_page("pages/Cidadãos.py")

with col2:
    if st.button("📊 Relatórios", use_container_width=True):
        st.switch_page("pages/Relatórios.py")

    if st.button("✅ Resumo de Produção", use_container_width=True):
        st.switch_page("pages/Resumo de Produção.py")

st.markdown('</div>', unsafe_allow_html=True)

# Rodapé fixo
st.markdown('<div class="footer">Desenvolvido para uso profissional</div>', unsafe_allow_html=True)
