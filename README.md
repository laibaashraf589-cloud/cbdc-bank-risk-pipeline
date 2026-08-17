# CBDC Announcement Impact on Bank Risk: Empirical Pipeline

An end-to-end econometric research pipeline built in Python to evaluate the causal impact of Central Bank Digital Currency (CBDC) announcements on commercial bank-level liquidity risk.
## 📌 Features & Methodology
- **Module 1 (Macro Time-Series):** Structural break analysis via Chow Test & ADF stationarity testing.
- **Module 2 (Micro Panel DiD):** Difference-in-Differences baseline regression with clustered standard errors.
- **Module 3 (Dynamic Event Study):** Two-Way Fixed Effects (TWFE) dynamic model verifying parallel trends.
- **Module 4 (Triple Differences - DDD):** Bank-level size heterogeneity analysis.
- ## 🛠️ Project Structure
```text
cbdc_project/
├── data/              # Raw macro time-series & bank panel datasets
├── modules/           # Econometric modeling scripts (M1 to M4)
├── outputs/           # High-res figures & regression text tables
├── main.py            # Master pipeline execution script
├── requirements.txt   # Dependencies
└── README.md
## 🚀 How to Run
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Execute full empirical pipeline
python main.py
## 📊 Key Figures
- **Dynamic Event Study Output:** `outputs/figures/m3_event_study.png`
- **Time Series Structural Break:** `outputs/figures/m1_time_series_break.png`
