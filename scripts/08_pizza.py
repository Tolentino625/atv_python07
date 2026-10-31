"""Gráfico de pizza: participação de cada canal de venda no faturamento."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_pizza.csv").sort_values("faturamento", ascending=False)

cores = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]
total = df["faturamento"].sum()

fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(
    df["faturamento"],
    labels=df["canal_venda"],
    colors=cores,
    startangle=90,
    counterclock=False,
    autopct=lambda p: f"{p:.1f}%\nR$ {p * total / 100:,.0f}".replace(",", "."),
    pctdistance=0.72,
    wedgeprops={"edgecolor": "white", "linewidth": 2},
    textprops={"fontsize": 10},
)

ax.set_title("Faturamento por canal de venda", fontsize=13, loc="left")
ax.text(0, -1.3, f"Faturamento total: R$ {total:,.0f}".replace(",", "."), ha="center", fontsize=10, color="#52514e")

fig.tight_layout()
saida = RAIZ / "graficos" / "08_pizza.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
