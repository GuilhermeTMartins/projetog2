import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard Evasão Escolar",
    layout="wide"
)

st.title("Dashboard Executivo de Evasão Escolar no Brasil")

st.write("""
Este dashboard apresenta uma análise sobre evasão escolar no Brasil,
permitindo visualizar indicadores, gráficos e padrões relevantes.
""")

# leitura dos dados
df = pd.read_csv("dados/simulacao_evasao_escolar_brasil.csv")

st.subheader("Visualização dos Dados")

st.dataframe(df.head())
