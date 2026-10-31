"""Gráfico de frequência: quantidade de chamados por tipo de atendimento."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_frequencia.csv")

freq = df["tipo_atendimento"].value_counts()  # já ordenado do maior para o menor
total = freq.sum()

fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.bar(freq.index, freq.values, color="#2a78d6", width=0.6)

for barra, valor in zip(barras, freq.values):
    ax.text(
        barra.get_x() + barra.get_width() / 2,
        valor + total * 0.005,
        f"{valor} ({valor / total:.0%})",
        ha="center",
        va="bottom",
        fontsize=10,
    )

ax.set_title("Frequência de chamados por tipo de atendimento", fontsize=13, loc="left")
ax.set_xlabel("Tipo de atendimento")
ax.set_ylabel("Número de chamados")
ax.set_ylim(0, freq.max() * 1.12)
ax.spines[["top", "right"]].set_visible(False)
ax.yaxis.grid(True, alpha=0.25)
ax.set_axisbelow(True)

fig.tight_layout()
saida = RAIZ / "graficos" / "01_frequencia.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
