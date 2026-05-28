import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dados/simulacao_evasao_escolar_brasil.csv")

st.title("Gráficos")

# =========================
# evasão por região
# =========================

st.subheader("Taxa Média de Evasão por Região")

evasao_regiao = (
    df.groupby("regiao")["taxa_evasao"]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(10,5))

sns.barplot(
    data=evasao_regiao,
    x="regiao",
    y="taxa_evasao",
    ax=ax
)

plt.xticks(rotation=45)

st.pyplot(fig)

# =========================
# evasão por rede
# =========================

st.subheader("Evasão por Rede de Ensino")

evasao_rede = (
    df.groupby("rede_ensino")["taxa_evasao"]
    .mean()
    .reset_index()
)

fig2, ax2 = plt.subplots(figsize=(8,5))

sns.barplot(
    data=evasao_rede,
    x="rede_ensino",
    y="taxa_evasao",
    ax=ax2
)

st.pyplot(fig2)

# =========================
# evolução temporal
# =========================

st.subheader("Evolução Temporal da Taxa de Evasão")

evasao_ano = (
    df.groupby("ano")["taxa_evasao"]
    .mean()
    .reset_index()
)

fig3, ax3 = plt.subplots(figsize=(10,5))

sns.lineplot(
    data=evasao_ano,
    x="ano",
    y="taxa_evasao",
    marker="o",
    ax=ax3
)

st.pyplot(fig3)
