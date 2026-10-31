"""Regressão linear simples: gasto mensal em função da renda mensal."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_regressao.csv")

x = df["renda_mensal"].to_numpy()
y = df["gasto_mensal"].to_numpy()

# Ajuste por mínimos quadrados: y = a*x + b
a, b = np.polyfit(x, y, 1)
y_prev = a * x + b
r2 = 1 - np.sum((y - y_prev) ** 2) / np.sum((y - y.mean()) ** 2)

xs = np.linspace(x.min(), x.max(), 100)

fig, ax = plt.subplots(figsize=(8, 5.5))
ax.scatter(x, y, color="#2a78d6", s=40, alpha=0.7, edgecolor="white", linewidth=0.8, label="Observações")
ax.plot(xs, a * xs + b, color="#eb6834", linewidth=2.5, label=f"Reta ajustada: y = {a:.2f}x + {b:.0f}")

ax.text(
    0.04, 0.95, f"R² = {r2:.3f}",
    transform=ax.transAxes, va="top", fontsize=11,
)

ax.set_title("Regressão: gasto mensal x renda mensal", fontsize=13, loc="left")
ax.set_xlabel("Renda mensal (R$)")
ax.set_ylabel("Gasto mensal (R$)")
ax.legend(frameon=False, loc="lower right")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(True, alpha=0.25)
ax.set_axisbelow(True)

fig.tight_layout()
saida = RAIZ / "graficos" / "07_regressao.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}  (a={a:.4f}, b={b:.2f}, R²={r2:.4f})")
