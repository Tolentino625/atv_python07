"""Gráfico de linhas: evolução diária das vendas por loja."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_linhas.csv", parse_dates=["data"]).sort_values("data")

cores = {"Loja A": "#2a78d6", "Loja B": "#eb6834"}

fig, ax = plt.subplots(figsize=(10, 5.5))
for loja, grupo in df.groupby("loja"):
    # Cada loja tem registros apenas em alguns dias; a linha liga os dias registrados.
    ax.plot(
        grupo["data"], grupo["vendas"],
        color=cores[loja], linewidth=2, marker="o", markersize=4,
        markeredgecolor="white", markeredgewidth=0.6,
        label=f"{loja} ({len(grupo)} registros)",
    )

ax.set_title("Evolução das vendas por loja (jan–mar 2026)", fontsize=13, loc="left")
ax.set_xlabel("Data")
ax.set_ylabel("Vendas")
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b/%Y"))
ax.legend(frameon=False, title="Loja")
ax.spines[["top", "right"]].set_visible(False)
ax.yaxis.grid(True, alpha=0.25)
ax.set_axisbelow(True)

fig.tight_layout()
saida = RAIZ / "graficos" / "09_linhas.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
