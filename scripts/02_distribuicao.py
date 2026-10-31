"""Histograma: distribuição da idade dos clientes."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_distribuicao.csv")

media = df["idade"].mean()
mediana = df["idade"].median()

fig, ax = plt.subplots(figsize=(8, 5))
bins = np.arange(df["idade"].min() - 0.5, df["idade"].max() + 5.5, 5)
ax.hist(df["idade"], bins=bins, color="#2a78d6", edgecolor="white", linewidth=1.5)

ax.axvline(media, color="#eb6834", linestyle="--", linewidth=2, label=f"Média: {media:.1f} anos")
ax.axvline(mediana, color="#52514e", linestyle=":", linewidth=2, label=f"Mediana: {mediana:.1f} anos")

ax.set_title("Distribuição da idade dos clientes", fontsize=13, loc="left")
ax.set_xlabel("Idade (anos)")
ax.set_ylabel("Número de clientes")
ax.legend(frameon=False)
ax.spines[["top", "right"]].set_visible(False)
ax.yaxis.grid(True, alpha=0.25)
ax.set_axisbelow(True)

fig.tight_layout()
saida = RAIZ / "graficos" / "02_distribuicao.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
