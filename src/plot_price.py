import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("data/QQQ_daily.csv", index_col="Date", parse_dates=True)

fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(df.index, df["Close"])
ax.set_title("QQQ - preu de tancament ajustat (15 anys)")
ax.set_ylabel("USD")
ax.grid(alpha=0.3)

Path("results").mkdir(exist_ok=True)
fig.savefig("results/qqq_price.png", dpi=150)
plt.show()