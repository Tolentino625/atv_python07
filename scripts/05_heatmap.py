"""Mapa de calor: movimento de clientes por dia da semana e horário."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_heatmap.csv")

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
matriz = (
    df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
    .reindex(dias)
)

fig, ax = plt.subplots(figsize=(9, 5.5))
sns.heatmap(
    matriz,
    annot=True,
    fmt="d",
    cmap="Blues",  # sequencial de uma só cor: claro = pouco, escuro = muito
    linewidths=2,
    linecolor="white",
    cbar_kws={"label": "Movimento de clientes"},
    ax=ax,
)

ax.set_title("Movimento de clientes por dia e horário", fontsize=13, loc="left")
ax.set_xlabel("Horário")
ax.set_ylabel("Dia da semana")
ax.tick_params(axis="y", rotation=0)

fig.tight_layout()
saida = RAIZ / "graficos" / "05_heatmap.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
