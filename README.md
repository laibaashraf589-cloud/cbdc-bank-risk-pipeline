CBDC Announcement Impact on Bank Risk: Empirical Pipeline
An end-to-end econometric research pipeline built in Python to evaluate the causal impact of Central Bank Digital Currency announcements on commercial bank-level liquidity risk.

📌 Features & Methodology

Module 1 (Macro Time-Series): Structural break analysis via Chow Test and ADF stationarity testing.

Module 2 (Micro Panel DiD): Difference-in-Differences baseline regression with clustered standard errors.

Module 3 (Dynamic Event Study): Two-Way Fixed Effects dynamic model verifying parallel trends.

Module 4 (Triple Differences - DDD): Bank-level size heterogeneity analysis.

🛠️ Project Structure

data: Raw macro time-series and bank panel datasets

modules: Econometric modeling scripts (M1 to M4)

outputs: High-resolution figures and regression text tables

main.py: Master pipeline execution script

requirements.txt: Project dependencies

🚀 How to Run

Install dependencies: pip install -r requirements.txt

Execute full empirical pipeline: python main.py

📊 Key Figures

Dynamic Event Study Output: outputs/figures/m3_event_study.png

Time Series Structural Break: outputs/figures/m1_time_series_break.png
