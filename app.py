from pathlib import Path

import streamlit as st

RAIZ = Path(__file__).resolve().parent
PASTA_GRAFICOS = RAIZ / "graficos"

st.set_page_config(
    page_title="Dashboard de Gráficos",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.header("Informações do aluno")
    st.markdown("**Nome:** Lucas Tolentino")
    st.markdown("**Nº:** 29")
    st.markdown("**Turma:** 3E2")
    st.divider()
    st.caption(
        "Atividade 06 · Gráficos em Python (matplotlib, seaborn e pandas), "
        "exibidos em um dashboard Streamlit."
    )

GRAFICOS = [
    (
        "01_frequencia.png",
        "1. Frequência de chamados",
        "Dos 300 chamados, **Dúvida** é o tipo mais comum (116, ou 38,7%), seguido de "
        "**Reclamação** (73, 24,3%). Bug, Cancelamento e Elogio somam os 37% restantes. "
        "Dúvidas e reclamações juntas passam de 60% da demanda, o que sugere investir em "
        "documentação e em melhorias no atendimento.",
    ),
    (
        "02_distribuicao.png",
        "2. Distribuição da idade dos clientes",
        "As idades vão de 18 a 69 anos, com média de 33,6 e mediana de 29. Como a média "
        "fica acima da mediana, a distribuição é assimétrica à direita: a maior parte dos "
        "clientes é jovem e há uma cauda de clientes mais velhos puxando a média para cima.",
    ),
    (
        "03_dispersao.png",
        "3. Relação entre altura e peso",
        "Há uma correlação positiva forte (r ≈ 0,85): quanto maior a altura, maior tende a "
        "ser o peso. Os dois sexos (75 pessoas cada) se sobrepõem quase por completo, com "
        "altura média de ~170 cm e peso médio de ~62–63 kg, e a relação é praticamente a "
        "mesma nos dois grupos.",
    ),
    (
        "04_boxplot.png",
        "4. Distribuição salarial por departamento",
        "**Vendas** e **TI** têm as maiores medianas (cerca de R$ 7.100 e R$ 6.600) e a maior "
        "dispersão; Marketing e RH ficam em torno de R$ 4.200. Todos os departamentos têm "
        "outliers (pontos laranja): R$ 12.000 em Marketing e RH e R$ 21.000 em TI e Vendas, "
        "valores bem acima do restante do grupo.",
    ),
    (
        "05_heatmap.png",
        "5. Movimento de clientes por dia e horário",
        "O fim de semana concentra o movimento: **Domingo** (média de ~119 clientes por "
        "horário) e **Sábado** (~111) superam muito os dias úteis. O pico é domingo às "
        "12:00 (199) e o menor movimento é quinta às 16:00 (22). Quinta é o dia mais "
        "fraco, com média de ~44.",
    ),
    (
        "06_barras.png",
        "6. Vendas médias por categoria e região",
        "A região **Oeste** lidera (média de ~R$ 225) e a **Norte** é a mais fraca (~R$ 103). "
        "A maior venda média é Livros no Oeste (R$ 284,18) e a menor é Alimentos no Norte "
        "(R$ 54,15). Livros é a categoria mais forte no geral; em Eletrônicos o Leste vai "
        "bem e o Sul fica atrás.",
    ),
    (
        "07_regressao.png",
        "7. Regressão: gasto mensal x renda mensal",
        "A reta ajustada, y ≈ 0,57x + 421, tem R² ≈ 0,98: a renda explica cerca de 98% da "
        "variação do gasto. Em média, cada R$ 1,00 a mais de renda traz cerca de R$ 0,57 a "
        "mais de gasto, e o ajuste é muito bom em toda a faixa observada, de ~R$ 2,6 mil "
        "a ~R$ 15 mil.",
    ),
    (
        "08_pizza.png",
        "8. Faturamento por canal de venda",
        "O faturamento total é de R$ 120.000. O **Site** responde por 37,5% e a **Loja Física** "
        "por 26,7%; juntos passam de 64%. O Aplicativo vem em seguida (17,5%), e Parceiros "
        "(11,7%) e Telefone (6,7%) têm participação pequena.",
    ),
    (
        "09_linhas.png",
        "9. Evolução das vendas por loja",
        "Entre janeiro e março de 2026 as vendas crescem de forma contínua nas duas lojas: a "
        "média mensal passa de ~R$ 122 em janeiro para ~R$ 173 em fevereiro e ~R$ 225 em "
        "março. As Lojas A e B têm desempenho muito parecido (médias de ~168 e ~179) e o "
        "maior valor é da Loja A, em 24/03 (260,37).",
    ),
]

st.title("Dashboard de Gráficos")
st.caption("Visualização dos nove gráficos gerados na atividade 06, três a três, cada um com sua análise.")

POR_LINHA = 3
for inicio in range(0, len(GRAFICOS), POR_LINHA):
    colunas = st.columns(POR_LINHA, gap="large")
    for coluna, (arquivo, titulo, analise) in zip(colunas, GRAFICOS[inicio : inicio + POR_LINHA]):
        with coluna:
            st.subheader(titulo)
            caminho = PASTA_GRAFICOS / arquivo
            if caminho.exists():
                st.image(str(caminho), use_container_width=True)
            else:
                st.warning(f"Imagem não encontrada: graficos/{arquivo}. Rode o script correspondente em scripts/.")
            st.markdown(f"**Análise:** {analise}")
    st.divider()
