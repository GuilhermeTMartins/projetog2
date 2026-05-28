import streamlit as st
import pandas as pd

df = pd.read_csv("dados/simulacao_evasao_escolar_brasil.csv")

st.title("KPIs")

# filtros
regiao = st.sidebar.multiselect(
    "Região",
    df["regiao"].unique(),
    default=df["regiao"].unique()
)

rede = st.sidebar.multiselect(
    "Rede de Ensino",
    df["rede_ensino"].unique(),
    default=df["rede_ensino"].unique()
)

ano = st.sidebar.multiselect(
    "Ano",
    df["ano"].unique(),
    default=df["ano"].unique()
)

# dataframe filtrado
df_filtrado = df[
    (df["regiao"].isin(regiao)) &
    (df["rede_ensino"].isin(rede)) &
    (df["ano"].isin(ano))
]

# KPIs
total_matriculados = df_filtrado["matriculados"].sum()
total_evasoes = df_filtrado["evasoes"].sum()
media_evasao = df_filtrado["taxa_evasao"].mean()
media_desempenho = df_filtrado["indice_desempenho"].mean()

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

col1.metric(
    "Total de Matriculados",
    f"{total_matriculados:,}"
)

col2.metric(
    "Total de Evasões",
    f"{total_evasoes:,}"
)

col3.metric(
    "Taxa Média de Evasão",
    f"{media_evasao:.2f}%"
)

col4.metric(
    "Média de Desempenho",
    f"{media_desempenho:.2f}"
)

st.subheader("Tabela de Dados")

st.dataframe(df_filtrado)
