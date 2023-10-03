import streamlit as st
import pandas as pd

st.set_page_config(page_title='Aplicação')

with st.container():
    st.subheader('Grupos de Raparigas na Comunidade')
    st.title('Dashboard de Grupos')
    st.write('Fonte de dados: [kompilador](https://kompilador.com/impacto/dashboard/)')

@st.cache_data
def loadData():
    dados = pd.read_csv('dados.csv')
    return dados

with st.container():
    st.write('---')
    
    dias = st.selectbox('Selecione o período', ['7D','15D','21D', '30D'])
    num_dias = int(dias.replace('D', ''))

    dados = loadData()
    dados = dados[-num_dias:]
    st.bar_chart(dados, x='Data Inicio', y='M15')