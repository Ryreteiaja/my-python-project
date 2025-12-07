# my-python-project

import numpy as np
import pandas as pd

# =========================
# 定数
# =========================
c = 2.99792458e8
r = 40e-3
L = 40e-3

# =========================
# ベッセル零点
# =========================
x_tm = {
    (0, 1): 2.405, (0, 2): 5.520, (0, 3): 8.654,
    (1, 1): 3.832, (1, 2): 7.016, (1, 3): 10.174,
    (2, 1): 5.135, (2, 2): 8.417, (2, 3): 11.620
}

x_te = {
    (0, 1): 3.832, (0, 2): 7.016, (0, 3): 10.174,
    (1, 1): 1.841, (1, 2): 5.331, (1, 3): 8.536,
    (2, 1): 3.054, (2, 2): 6.706, (2, 3): 9.970
}

# =========================
# 周波数計算
# =========================
rows = []

for mode, x_dict in [("TE", x_te), ("TM", x_tm)]:
    for m in [0, 1, 2]:
        for n in [1, 2, 3]:
            for p in [1, 2]:
                xmn = x_dict[(m, n)]
                f = (c / (2*np.pi)) * np.sqrt(
                    (xmn / r)**2 + (p*np.pi / L)**2
                )
                rows.append({
                    "Type": mode,
                    "Mode": f"{mode}_{m}{n}{p}",
                    "Frequency [GHz]": f / 1e9
                })

df = pd.DataFrame(rows)

# =========================
# TE / TM 分離 & ソート
# =========================
te = df[df["Type"] == "TE"].sort_values("Frequency [GHz]").reset_index(drop=True)
tm = df[df["Type"] == "TM"].sort_values("Frequency [GHz]").reset_index(drop=True)

# =========================
# 横並び表示用 DataFrame
# =========================
max_len = max(len(te), len(tm))

te_col = te.reindex(range(max_len))
tm_col = tm.reindex(range(max_len))

df_side_by_side = pd.DataFrame({
    "TE mode": te_col["Mode"],
    "TE freq [GHz]": te_col["Frequency [GHz]"].map(lambda x: f"{x:.4f}" if pd.notna(x) else ""),
    " | ": ["|"] * max_len,
    "TM mode": tm_col["Mode"],
    "TM freq [GHz]": tm_col["Frequency [GHz]"].map(lambda x: f"{x:.4f}" if pd.notna(x) else "")
})

# =========================
# 出力
# =========================
print(df_side_by_side.to_string(index=False))
