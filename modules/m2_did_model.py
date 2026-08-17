import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# 1. Panel Dataset Load Karein
df = pd.read_csv("data/bank_panel_data.csv")
df['quarter'] = pd.to_datetime(df['quarter'])

print("="*40)
print(" MODULE 2: DIFFERENCE-IN-DIFFERENCES (DiD) ANALYSIS ")
print("="*40)

# 2. Standard Baseline DiD Model: Liquidity_Ratio ~ Treated + Post + (Treated * Post)
model_formula = "liquidity_ratio ~ is_treated + is_post + did_interaction + bank_size + capital_ratio"
did_model = smf.ols(formula=model_formula, data=df).fit(
    cov_type='cluster', 
    cov_kwds={'groups': df['bank_id']}
)

print("\n[Baseline DiD Model Results (Clustered Standard Errors)]")
print(did_model.summary().tables[1])

# Key Coefficient Extraction
did_coef = did_model.params['did_interaction']
did_pval = did_model.pvalues['did_interaction']

print("\n[Causal Impact Summary]")
print(f"DiD Interaction Effect (Treatment x Post): {did_coef:.4f}")
print(f"p-value                                 : {did_pval:.4f}")

if did_pval < 0.05:
    print("Interpretation: CBDC announcement caused a statistically significant drop in bank liquidity for treated banks!")

# 3. Output Table Save Karein
with open("outputs/tables/m2_did_results.txt", "w") as f:
    f.write(did_model.summary().as_text())

print("\n[Output Saved]")
print("Table saved to: outputs/tables/m2_did_results.txt")