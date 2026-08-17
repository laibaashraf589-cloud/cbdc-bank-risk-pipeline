import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

# 1. Load Macro Time Series Data
df = pd.read_csv("data/raw_macro_ts.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

print("="*40)
print(" MODULE 1: MACRO TIME SERIES ANALYSIS ")
print("="*40)

# 2. ADF Test for Stationarity
adf_result = adfuller(df['deposit_growth'])
print(f"\n[ADF Stationarity Test]")
print(f"ADF Statistic : {adf_result[0]:.4f}")
print(f"p-value       : {adf_result[1]:.4f}")

# 3. Chow Test for Structural Break
break_date = "2022-06-01"
sub1 = df[df.index < break_date]['deposit_growth']
sub2 = df[df.index >= break_date]['deposit_growth']

rss_full = np.sum((df['deposit_growth'] - df['deposit_growth'].mean()) ** 2)
rss1 = np.sum((sub1 - sub1.mean()) ** 2)
rss2 = np.sum((sub2 - sub2.mean()) ** 2)

k = 1
N1, N2 = len(sub1), len(sub2)
f_stat = ((rss_full - (rss1 + rss2)) / k) / ((rss1 + rss2) / (N1 + N2 - 2 * k))
p_val = 1 - stats.f.cdf(f_stat, k, N1 + N2 - 2 * k)

print(f"\n[Chow Structural Break Test]")
print(f"F-Statistic   : {f_stat:.4f}")
print(f"p-value       : {p_val:.4f}")
if p_val < 0.05:
    print("Result        : Significant structural break detected at CBDC Announcement Date!")

# 4. Pre-Break ARIMA Model & Forecast
model = ARIMA(sub1, order=(1, 0, 1)).fit()
forecast = model.forecast(steps=len(sub2))

# 5. Plotting & Saving Chart
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['deposit_growth'], label='Actual Deposit Growth', color='#1f77b4', linewidth=2)
plt.plot(sub2.index, forecast, label='Baseline Forecast (No Shock)', color='#d62728', linestyle='--', linewidth=2)
plt.axvline(pd.Timestamp(break_date), color='black', linestyle=':', label='CBDC Announcement Date')
plt.title("Macro Deposit Growth: Pre- vs Post-CBDC Announcement Shock")
plt.xlabel("Date")
plt.ylabel("Deposit Growth Rate")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("outputs/figures/m1_time_series_break.png", dpi=300)

print(f"\n[Output Saved]")
print("Plot saved to: outputs/figures/m1_time_series_break.png")