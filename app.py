import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard Evasão Escolar",
    layout="wide"
)

st.title("Dashboard Executivo de Evasão Escolar no Brasil")

st.write("""
Este dashboard apresenta uma análise executiva sobre evasão escolar no Brasil,
permitindo identificar padrões regionais, desempenho escolar e fatores associados ao risco de evasão.
""")

# leitura dos dados
df = pd.read_csv("dados/simulacao_evasao_escolar_brasil.csv")

st.subheader("Visualização dos Dados")

st.dataframe(df.head())

st.subheader("Informações Gerais")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total de Registros",
    len(df)
)

col2.metric(
    "Total de Evasões",
    int(df["evasoes"].sum())
)

col3.metric(
    "Taxa Média de Evasão",
    f"{df['taxa_evasao'].mean():.2f}%"
)
