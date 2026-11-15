"""Summary chart for the README. Numbers are copied from the saved notebook outputs."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sets = ["2019 test set\n(same crawl as training)", "2024 dataset\n(different team)", "Live sites\n(Nov 2026)"]
keyword = [0.777, 0.556, 0.568]
model_2019 = [0.947, 0.587, 0.693]
model_plus = [np.nan, 0.858, 0.764]  # + 2024 data; not measured on the 2019 test set

x = np.arange(len(sets)); w = 0.26
fig, ax = plt.subplots(figsize=(8, 4.2), dpi=150)
bars = [
    ax.bar(x - w, keyword, w, label="Keyword rule (baseline)", color="#b0b0b0"),
    ax.bar(x, model_2019, w, label="Our model, trained on 2019 data", color="#4c72b0"),
    ax.bar(x + w, model_plus, w, label="Our model + 2024 data", color="#dd8452"),
]
for group in bars:
    for b in group:
        h = b.get_height()
        if not np.isnan(h):
            ax.text(b.get_x() + b.get_width() / 2, h + 0.01, f"{h:.2f}", ha="center", fontsize=8)
ax.axhline(0.5, color="black", lw=0.8, ls="--")
ax.text(2.45, 0.51, "guessing", fontsize=8, ha="right")
ax.set_xticks(x, sets)
ax.set_ylim(0.4, 1.0)
ax.set_ylabel("Balanced accuracy")
ax.set_title("A detector that looks great on 2019 data falls apart later; newer data helps")
ax.legend(fontsize=8, loc="upper right")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("figures/summary.png")
