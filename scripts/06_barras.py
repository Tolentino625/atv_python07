"""Barras agrupadas: vendas médias por categoria e região."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_barras.csv")

regioes = ["Norte", "Sul", "Leste", "Oeste"]
cores = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]  # ordem fixa por região

tabela = df.pivot(index="categoria", columns="regiao", values="vendas_medias")[regioes]
categorias = tabela.index.tolist()

x = np.arange(len(categorias))
largura = 0.2

fig, ax = plt.subplots(figsize=(10, 5.5))
for i, (regiao, cor) in enumerate(zip(regioes, cores)):
    ax.bar(x + (i - 1.5) * largura, tabela[regiao], width=largura * 0.9, label=regiao, color=cor)

ax.set_title("Vendas médias por categoria e região", fontsize=13, loc="left")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas médias (R$)")
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend(title="Região", frameon=False, ncol=4, loc="upper center", bbox_to_anchor=(0.5, -0.12))
ax.spines[["top", "right"]].set_visible(False)
ax.yaxis.grid(True, alpha=0.25)
ax.set_axisbelow(True)

fig.tight_layout()
saida = RAIZ / "graficos" / "06_barras.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
