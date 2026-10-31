# Gráficos a partir de arquivos CSV

Nove gráficos em Python (matplotlib, seaborn e pandas), um script por gráfico, cada um lendo seu próprio arquivo de dados.

| # | Script | Dados | Gráfico | Resultado |
|---|--------|-------|---------|-----------|
| 1 | `scripts/01_frequencia.py` | `dados_frequencia.csv` | Frequência (barras de contagem) | `graficos/01_frequencia.png` |
| 2 | `scripts/02_distribuicao.py` | `dados_distribuicao.csv` | Histograma | `graficos/02_distribuicao.png` |
| 3 | `scripts/03_dispersao.py` | `dados_dispersao.csv` | Dispersão (altura x peso, por sexo) | `graficos/03_dispersao.png` |
| 4 | `scripts/04_boxplot.py` | `dados_boxplot.csv` | Boxplot (salário por departamento) | `graficos/04_boxplot.png` |
| 5 | `scripts/05_heatmap.py` | `dados_heatmap.csv` | Mapa de calor (dia x horário) | `graficos/05_heatmap.png` |
| 6 | `scripts/06_barras.py` | `dados_barras.csv` | Barras agrupadas (categoria x região) | `graficos/06_barras.png` |
| 7 | `scripts/07_regressao.py` | `dados_regressao.csv` | Regressão linear (renda x gasto) | `graficos/07_regressao.png` |
| 8 | `scripts/08_pizza.py` | `dados_pizza.csv` | Pizza (faturamento por canal) | `graficos/08_pizza.png` |
| 9 | `scripts/09_linhas.py` | `dados_linhas.csv` | Linhas (vendas por loja ao longo do tempo) | `graficos/09_linhas.png` |

## Como executar

```bash
pip install -r requirements.txt

# um gráfico
python scripts/01_frequencia.py

# todos os gráficos
for s in scripts/*.py; do python "$s"; done
```

Os scripts usam caminhos relativos à raiz do projeto, então podem ser executados de qualquer pasta. As imagens são gravadas em `graficos/`.

## Estrutura

```
data/        arquivos CSV de entrada
scripts/     um script por gráfico
graficos/    imagens PNG geradas
```

## Observações

- **Regressão:** reta ajustada por mínimos quadrados (`numpy.polyfit`), com R² exibido no gráfico.
- **Boxplot:** os pontos fora dos bigodes são outliers presentes nos dados (dois por departamento).
- **Linhas:** cada dia tem um único registro, de uma das lojas; por isso cada linha liga apenas os dias em que a loja aparece nos dados.
