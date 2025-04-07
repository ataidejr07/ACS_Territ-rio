import streamlit as st

# === Oculta o menu padrão e o rodapé do Streamlit ===
hide_st_style = """
    <style>
    #MainMenu, footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# === Estilos personalizados ===
st.markdown("""
    <style>
        /* Cabeçalho fixo azul */
        .custom-header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            background-color: #0056b3;
            padding: 0.8rem 1rem;
            z-index: 100;
            display: flex;
            align-items: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }

        .custom-header h1 {
            color: white;
            font-size: 1.4rem;
            margin-left: 3rem;
        }

        /* Ícone do menu */
        .menu-button {
            background-color: #0056b3;
            border: none;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
            margin-right: 1rem;
            position: absolute;
            left: 1rem;
        }

        /* Estilo do menu lateral */
        .sidebar-menu {
            position: fixed;
            top: 3.5rem;
            left: 0;
            width: 220px;
            background-color: #1a1a1a;
            padding: 1rem;
            box-shadow: 4px 0 6px rgba(0,0,0,0.3);
            z-index: 99;
            display: none;
        }

        .sidebar-menu.show {
            display: block;
        }

        .sidebar-menu a {
            display: block;
            color: white;
            text-decoration: none;
            margin-bottom: 1rem;
            font-size: 1rem;
        }

        /* Espaço para o conteúdo abaixo do cabeçalho */
        .main-content {
            margin-top: 5rem;
        }

        /* Rodapé fixo azul */
        .custom-footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100vw;
            background-color: #0056b3;
            color: white;
            text-align: center;
            padding: 0.6rem;
            font-size: 0.9rem;
            z-index: 100;
        }

        /* Botões das seções */
        .botao-pagina {
            display: block;
            width: 100%;
            background-color: white;
            color: black;
            padding: 0.8rem;
            margin: 0.5rem 0;
            border-radius: 10px;
            font-size: 1.1rem;
            text-align: left;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        }

        .secao-titulo {
            font-size: 1.3rem;
            margin-top: 2rem;
            color: white;
        }
    </style>

    <script>
        function toggleMenu() {
            var menu = document.getElementById("sidebar-menu");
            if (menu.classList.contains("show")) {
                menu.classList.remove("show");
            } else {
                menu.classList.add("show");
            }
        }
    </script>

    <!-- Cabeçalho -->
    <div class="custom-header">
        <button class="menu-button" onclick="toggleMenu()">☰</button>
        <h1>ACS Micro Área</h1>
    </div>

    <!-- Menu Lateral -->
    <div class="sidebar-menu" id="sidebar-menu">
        <a href="/Cartões%20Espelho">Cartões Espelho</a>
        <a href="/Laudos%20e%20Receitas">Laudos e Receitas</a>
    </div>

    <!-- Espaço principal -->
    <div class="main-content">
""", unsafe_allow_html=True)

# === Conteúdo da Página ===
st.markdown("## Bem-vindo, Ataide!")
st.markdown("### Cadastros")
st.markdown('<a href="/Domicílios" class="botao-pagina">🏡 Domicílios</a>', unsafe_allow_html=True)
st.markdown('<a href="/Famílias" class="botao-pagina">👨‍👩‍👧 Famílias</a>', unsafe_allow_html=True)
st.markdown('<a href="/Cidadãos" class="botao-pagina">🧑 Cidadãos</a>', unsafe_allow_html=True)

st.markdown("### Análises e Relatórios")
st.markdown('<a href="/Relatórios" class="botao-pagina">📊 Relatórios</a>', unsafe_allow_html=True)
st.markdown('<a href="/Resumo%20de%20Produção" class="botao-pagina">📈 Resumo de Produção</a>', unsafe_allow_html=True)
st.markdown('<a href="/Nascimentos%20e%20Óbitos" class="botao-pagina">👶⚰️ Nascimentos e Óbitos</a>', unsafe_allow_html=True)

# === Rodapé ===
st.markdown("""
    </div> <!-- Fecha main-content -->

    <div class="custom-footer">
        Desenvolvido para uso profissional em saúde
    </div>
""", unsafe_allow_html=True)
