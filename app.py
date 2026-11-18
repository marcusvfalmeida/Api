import streamlit as st
import requests

st.title('Jogos')
tab1, tab2 = st.tabs(['Visualizar jogos','Cadastrar jogos'], on_change='rerun')

with tab1:
    url = 'http://127.0.0.1:5000/jogos'
    response = requests.get(url)
    if response.status_code == 200:
        df = response.json()
        st.dataframe(df)
    else:
        st.error('Não foi possível exibir os jogos')
with tab2:
    with st.form('Cadastrar-jogo', clear_on_submit=True):
        nome = st.text_input('Nome do Jogo')
        ano = st.number_input('Ano do Jogo', min_value=1970)
        enviar = st.form_submit_button('Cadastrar')
        if nome and ano:
            url = 'http://127.0.0.1:5000/cadastrar'
            response = requests.post(url,json={'nome':nome, 'ano':ano})
            if response.status_code == 200:
                st.success('Cadastrado')
            else:
                st.error(f'Erro ao cadastrar\n {response.text}')