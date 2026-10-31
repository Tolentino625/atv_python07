"""Boxplot: distribuição salarial por departamento (com outliers)."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_boxplot.csv")

# Ordena os departamentos pela mediana salarial (maior primeiro)
ordem = df.groupby("departamento")["salario"].median().sort_values(ascending=False).index.tolist()
dados = [df.loc[df["departamento"] == d, "salario"] for d in ordem]

fig, ax = plt.subplots(figsize=(8, 5.5))
caixas = ax.boxplot(
    dados,
    tick_labels=ordem,
    patch_artist=True,
    widths=0.55,
    medianprops={"color": "#0b0b0b", "linewidth": 2},
    flierprops={"marker": "o", "markerfacecolor": "#eb6834", "markeredgecolor": "white", "markersize": 7},
)
for caixa in caixas["boxes"]:
    caixa.set_facecolor("#2a78d6")
    caixa.set_alpha(0.7)

ax.set_title("Distribuição salarial por departamento", fontsize=13, loc="left")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário (R$)")
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", ".")))
ax.spines[["top", "right"]].set_visible(False)
ax.yaxis.grid(True, alpha=0.25)
ax.set_axisbelow(True)

ax.text(
    0.99, 0.97, "● pontos laranja = valores atípicos (outliers)",
    transform=ax.transAxes, ha="right", va="top", fontsize=9, color="#52514e",
)

fig.tight_layout()
saida = RAIZ / "graficos" / "04_boxplot.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
