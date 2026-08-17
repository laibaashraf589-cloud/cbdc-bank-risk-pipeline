import pandas as pd
import statsmodels.formula.api as smf

# 1. Panel Data Load Karein
df = pd.read_csv("data/bank_panel_data.csv")

print("="*40)
print(" MODULE 4: TRIPLE DIFFERENCES (DDD) ANALYSIS ")
print("="*40)

# 2. Bank Size Heterogeneity Variable (High vs Low Size)
df['high_size'] = (df['bank_size'] > df['bank_size'].median()).astype(int)

# 3. Triple Difference Formula: Treated x Post x High_Size
formula = "liquidity_ratio ~ is_treated * is_post * high_size + capital_ratio"
ddd_model = smf.ols(formula=formula, data=df).fit(
    cov_type='cluster', 
    cov_kwds={'groups': df['bank_id']}
)

print("\n[DDD Regression Summary]")
print(ddd_model.summary().tables[1])

# 4. Output Save Karein
with open("outputs/tables/m4_ddd_results.txt", "w") as f:
    f.write(ddd_model.summary().as_text())

print("\n[Output Saved]")
print("Table saved to: outputs/tables/m4_ddd_results.txt")