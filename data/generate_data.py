import numpy as np
import pandas as pd

np.random.seed(42)

# 1. Macro Time Series (Module 1)
dates = pd.date_range(start="2018-01-01", end="2025-12-31", freq="ME")
t_break = "2022-06-01"

macro_df = pd.DataFrame({"date": dates})
macro_df["post_announcement"] = (macro_df["date"] >= t_break).astype(int)

base_growth = np.random.normal(loc=0.005, scale=0.002, size=len(dates))
shock = macro_df["post_announcement"] * -0.008
macro_df["deposit_growth"] = base_growth + shock
macro_df["interest_rate"] = np.random.normal(loc=0.03, scale=0.005, size=len(dates))

macro_df.to_csv("data/raw_macro_ts.csv", index=False)
print("Saved: data/raw_macro_ts.csv")

# 2. Bank-Level Panel Dataset (Module 2, 3, 4)
n_banks = 40
quarters = pd.date_range(start="2018-01-01", end="2025-12-31", freq="QE")

bank_ids = [f"BANK_{i:02d}" for i in range(1, n_banks + 1)]
treatment_banks = bank_ids[:20]

records = []
for b in bank_ids:
    is_treated = 1 if b in treatment_banks else 0
    bank_size = np.random.uniform(10, 15)

    for q in quarters:
        is_post = 1 if q >= pd.Timestamp("2022-06-01") else 0
        did_effect = -0.03 * (is_treated * is_post)
        unobserved_fixed_effect = (int(b.split("_")[1]) % 5) * 0.01

        liquidity_ratio = (
            0.15
            + did_effect
            + unobserved_fixed_effect
            + np.random.normal(0, 0.01)
        )

        records.append(
            {
                "bank_id": b,
                "quarter": q,
                "is_treated": is_treated,
                "is_post": is_post,
                "did_interaction": is_treated * is_post,
                "bank_size": bank_size,
                "capital_ratio": np.random.uniform(0.08, 0.14),
                "liquidity_ratio": liquidity_ratio,
            }
        )

panel_df = pd.DataFrame(records)
panel_df.to_csv("data/bank_panel_data.csv", index=False)
print("Saved: data/bank_panel_data.csv")