
import streamlit as st

st.set_page_config(page_title="ACS Micro Área", layout="wide")

# Estilos CSS
st.markdown(
    '''
    <style>
        .header {
            background-color: #0056b3;
            color: white;
            padding: 10px 20px;
            font-size: 20px;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 999;
        }
        .header-title {
            margin-left: 10px;
        }
        .menu-button {
            background-color: #003d80;
            border: none;
            border-radius: 5px;
            padding: 5px 10px;
            color: white;
            font-size: 18px;
            cursor: pointer;
        }
        .menu-content {
            position: absolute;
            top: 50px;
            left: 10px;
            background-color: #f9f9f9;
            min-width: 200px;
            border: 1px solid #ccc;
            border-radius: 5px;
            z-index: 1000;
            box-shadow: 0px 8px 16px rgba(0,0,0,0.2);
        }
        .content {
            margin-top: 70px;
            margin-bottom: 50px;
        }
        .custom-button {
            display: block;
            width: 100%;
            padding: 15px;
            text-align: left;
            border: 2px solid #ccc;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
            background-color: white;
            transition: 0.3s;
        }
        .custom-button:hover {
            background-color: #f0f0f0;
        }
        .footer {
            background-color: #0056b3;
            color: white;
            padding: 10px;
            text-align: center;
            font-size: 14px;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            z-index: 999;
        }
    </style>
    ''',
    unsafe_allow_html=True
)

# Cabeçalho
st.markdown('''
<div class="header">
    <div class="header-title">ACS Micro Área</div>
    <div class="menu-button" onclick="document.getElementById('menu-content').style.display='block'">☰</div>
</div>
<div id="menu-content" class="menu-content" style="display:none;">
    <a href="/pages/7_Cartoes_Espelho" target="_self">🪪 Cartões Espelho</a><br>
    <a href="/pages/8_Laudos_Receitas" target="_self">📄 Laudos e Receitas</a>
</div>
<script>
    const button = window.parent.document.querySelector('.menu-button');
    button?.addEventListener('click', () => {
        const menu = window.parent.document.getElementById('menu-content');
        if (menu.style.display === 'block') {
            menu.style.display = 'none';
        } else {
            menu.style.display = 'block';
        }
    });
</script>
''', unsafe_allow_html=True)

# Conteúdo principal
st.markdown('<div class="content">', unsafe_allow_html=True)
st.title("Bem-vindo, Ataide!")
st.subheader("Cadastros")
st.page_link("pages/1_Domicilios.py", label="🏡 Domicílios")
st.page_link("pages/2_Familias.py", label="👨‍👩‍👧‍👦 Famílias")
st.page_link("pages/3_Cidadaos.py", label="🧑 Cidadãos")

st.subheader("Análises e Relatórios")
st.page_link("pages/4_Relatorios.py", label="📊 Relatórios")
st.page_link("pages/5_Resumo_Producao.py", label="📈 Resumo de Produção")
st.page_link("pages/6_Nascimentos_Obitos.py", label="👶⚰️ Nascimentos e Óbitos")

# Rodapé
st.markdown('<div class="footer">Desenvolvido para ACS</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
