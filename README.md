# Análise de Evasão Escolar no Brasil

Este projeto foi desenvolvido para a Avaliação G2 da disciplina **Linguagem de Programação - Análise e Visualização de Dados com Python**. O objetivo é realizar uma análise completa sobre evasão escolar no Brasil, utilizando Python para tratamento, exploração e visualização dos dados, além de um dashboard interativo publicado com Streamlit.

## Objetivo do Projeto

A evasão escolar é um problema relevante para o desenvolvimento social e educacional do país. A proposta deste projeto é analisar um conjunto de dados simulado sobre evasão escolar no Brasil, identificando padrões relacionados à rede de ensino, região, período, desempenho, renda familiar, acesso à internet e nível de risco.

Com isso, o projeto busca responder perguntas como:

- Qual é a taxa média de evasão no conjunto de dados?
- A evasão é maior na rede pública ou privada?
- Existem diferenças relevantes entre regiões?
- Como a evasão varia ao longo dos anos?
- Quais indicadores podem apoiar ações de prevenção?

## Base de Dados

A base utilizada é o arquivo `simulacao_evasao_escolar_brasil.csv`, contendo registros simulados sobre evasão escolar no Brasil entre 2015 e 2024.

Principais variáveis da base:

- `ano`: ano de referência do registro.
- `semestre`: semestre analisado.
- `data`: data associada ao período.
- `regiao`: região brasileira.
- `uf`: unidade federativa.
- `municipio`: município.
- `rede_ensino`: rede pública ou privada.
- `serie`: série escolar.
- `matriculados`: quantidade de alunos matriculados.
- `evasoes`: quantidade de evasões registradas.
- `taxa_evasao`: percentual de evasão.
- `renda_media_familiar`: renda média familiar associada ao registro.
- `indice_desempenho`: indicador de desempenho escolar.
- `acesso_internet`: percentual de acesso à internet.
- `nivel_risco`: classificação de risco de evasão.

## Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- GitHub
- GitHub Pages

## Funcionalidades do Projeto

O projeto contempla as principais etapas de um fluxo profissional de análise de dados:

- Leitura e compreensão da base.
- Limpeza e preparação dos dados.
- Conversão de datas e verificação de inconsistências.
- Engenharia de atributos, com criação de colunas como mês, trimestre, interação entre renda e desempenho e indicador de alto risco.
- Análise exploratória de dados.
- Criação de KPIs.
- Visualizações com Matplotlib e Seaborn.
- Dashboard interativo com Streamlit.
- Organização em páginas e seções.
- Publicação online via GitHub Pages e Streamlit Community Cloud.

## Principais KPIs

- Total de registros analisados: **1.480**
- Período analisado: **2015 a 2024**
- Taxa média geral de evasão: **7,26%**
- Taxa média de evasão na rede pública: **10,40%**
- Taxa média de evasão na rede privada: **4,13%**

## Principais Insights

A análise mostrou que a rede de ensino é um dos fatores mais relevantes para explicar diferenças na evasão escolar. A rede pública apresentou taxa média de evasão significativamente superior à rede privada, indicando maior vulnerabilidade e necessidade de ações direcionadas.

As diferenças regionais foram mais moderadas, com taxas médias próximas entre as regiões analisadas. A análise temporal mostrou oscilações entre 2015 e 2024, com 2016 entre os anos de maior evasão média e 2019 entre os menores.

Também foram consideradas variáveis como renda média familiar, índice de desempenho, acesso à internet e nível de risco. Esses indicadores ajudam a compreender melhor o contexto da evasão e podem apoiar estratégias de prevenção e permanência escolar.

## Estrutura do Projeto

```text
projeto-g2/
|
|-- app.py
|-- requirements.txt
|-- README.md
|-- index.html
|-- dados/
|-- notebooks/
|-- pages/
```

## Como Executar o Projeto

1. Clone o repositório:

```bash
git clone LINK_DO_REPOSITORIO
```

2. Acesse a pasta do projeto:

```bash
cd projeto-g2
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o dashboard:

```bash
streamlit run app.py
```

## Links do Projeto

- Repositório GitHub: `[INSERIR_LINK_DO_GITHUB](https://github.com/GuilhermeTMartins/projetog2)`
- Página GitHub Pages: `INSERIR_LINK_DO_GITHUB_PAGES`
- Dashboard Streamlit: `[INSERIR_LINK_DO_STREAMLIT](https://projetog2-attudk2i3gwgk4fn7tfdcp.streamlit.app/)`
- Notebook de análise: `notebooks/G2LingProg.ipynb`

## Conclusão

O projeto demonstra como a análise de dados pode apoiar a compreensão da evasão escolar. A partir dos indicadores calculados e das visualizações desenvolvidas, foi possível identificar que a rede pública concentra maior taxa média de evasão, tornando-se um ponto prioritário para ações de acompanhamento, suporte pedagógico e políticas de permanência.

Embora o dataset seja simulado, a estrutura da análise representa um fluxo real de trabalho com dados: preparação da base, criação de indicadores, exploração visual, interpretação dos resultados e comunicação por meio de dashboard interativo.
