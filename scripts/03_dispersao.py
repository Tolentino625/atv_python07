"""Gráfico de dispersão: altura x peso, colorido por sexo."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_dispersao.csv")

cores = {"Feminino": "#2a78d6", "Masculino": "#eb6834"}
marcadores = {"Feminino": "o", "Masculino": "s"}

fig, ax = plt.subplots(figsize=(8, 5.5))
for sexo, grupo in df.groupby("sexo"):
    ax.scatter(
        grupo["altura_cm"],
        grupo["peso_kg"],
        label=f"{sexo} (n={len(grupo)})",
        color=cores[sexo],
        marker=marcadores[sexo],
        s=45,
        alpha=0.75,
        edgecolor="white",
        linewidth=0.8,
    )

ax.set_title("Relação entre altura e peso", fontsize=13, loc="left")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")
ax.legend(frameon=False, title="Sexo")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(True, alpha=0.25)
ax.set_axisbelow(True)

fig.tight_layout()
saida = RAIZ / "graficos" / "03_dispersao.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
