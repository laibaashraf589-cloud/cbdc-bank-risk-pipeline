import subprocess
import os

print("="*60)
print("  CBDC ANNOUNCEMENT EFFECTS ON BANK RISK: EMPIRICAL PIPELINE  ")
print("="*60)

scripts = [
    ("1. Data Generation", "data/generate_data.py"),
    ("2. Time Series Analysis (Module 1)", "modules/m1_timeseries.py"),
    ("3. Baseline DiD Regression (Module 2)", "modules/m2_did_model.py"),
    ("4. Dynamic Event Study (Module 3)", "modules/m3_event_study.py"),
    ("5. Triple Differences Model (Module 4)", "modules/m4_ddd_analysis.py")
]

for title, script in scripts:
    print(f"\n---> Running: {title} ...")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"SUCCESS: {script}")
    else:
        print(f"ERROR in {script}:")
        print(result.stderr)

print("\n" + "="*60)
print(" PIPELINE EXECUTION COMPLETE! ")
print(" All outputs are stored in outputs/figures/ and outputs/tables/")
print("="*60)