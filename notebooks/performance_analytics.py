import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

os.makedirs('reports', exist_ok=True)
print("Starting Fund Performance Analytics Script...")

# 1. Generate Dummy Data for 40 Schemes over 3 Years (~756 trading days)
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=756, freq='B')
funds = [f'Fund_{i+1:02d}' for i in range(40)]

# Generate Metrics for 40 Funds
scorecard_data = []
alpha_beta_data = []

for i, fund in enumerate(funds):
    cagr_1yr = np.random.uniform(0.08, 0.25)
    cagr_3yr = np.random.uniform(0.10, 0.22)
    cagr_5yr = np.random.uniform(0.12, 0.20)
    
    sharpe = np.random.uniform(0.8, 2.5)
    sortino = np.random.uniform(1.1, 3.2)
    alpha = np.random.uniform(-0.02, 0.08)
    beta = np.random.uniform(0.7, 1.3)
    max_dd = np.random.uniform(-0.25, -0.05)
    expense_ratio = np.random.uniform(0.005, 0.022)
    
    scorecard_data.append({
        'fund_name': fund,
        'cagr_1yr': round(cagr_1yr, 4),
        'cagr_3yr': round(cagr_3yr, 4),
        'cagr_5yr': round(cagr_5yr, 4),
        'sharpe_ratio': round(sharpe, 2),
        'sortino_ratio': round(sortino, 2),
        'alpha': round(alpha, 4),
        'beta': round(beta, 2),
        'max_drawdown': round(max_dd, 4),
        'expense_ratio': round(expense_ratio, 4)
    })
    
    alpha_beta_data.append({
        'fund_name': fund,
        'alpha': round(alpha, 4),
        'beta': round(beta, 2),
        'r_squared': round(np.random.uniform(0.75, 0.98), 2)
    })

df_scorecard = pd.DataFrame(scorecard_data)
df_alpha_beta = pd.DataFrame(alpha_beta_data)

# Calculate Composite Score (0-100)
# 30% 3yr return rank + 25% Sharpe + 20% Alpha + 15% Expense (inverse) + 10% Max DD (inverse)
df_scorecard['score'] = (
    df_scorecard['cagr_3yr'].rank(pct=True) * 30 +
    df_scorecard['sharpe_ratio'].rank(pct=True) * 25 +
    df_scorecard['alpha'].rank(pct=True) * 20 +
    (1 - df_scorecard['expense_ratio'].rank(pct=True)) * 15 +
    (1 - df_scorecard['max_drawdown'].rank(pct=True, ascending=False)) * 10
).round(2)

# Save CSV Files
df_scorecard.to_csv('reports/fund_scorecard.csv', index=False)
df_alpha_beta.to_csv('reports/alpha_beta.csv', index=False)
print("✓ fund_scorecard.csv & alpha_beta.csv saved successfully!")

# Benchmark Comparison Chart PNG
plt.figure(figsize=(10, 5))
days = np.arange(1, 100)
plt.plot(days, np.cumprod(1 + np.random.normal(0.0008, 0.01, 99)), label='Top 5 Funds Avg', color='green', linewidth=2)
plt.plot(days, np.cumprod(1 + np.random.normal(0.0005, 0.009, 99)), label='Nifty 50', color='blue', linestyle='--')
plt.plot(days, np.cumprod(1 + np.random.normal(0.0006, 0.0095, 99)), label='Nifty 100', color='orange', linestyle=':')
plt.title('Benchmark Comparison: Top 5 Funds vs Nifty 50 & Nifty 100 (3 Years)')
plt.xlabel('Trading Days')
plt.ylabel('Cumulative Growth Factor')
plt.legend()
plt.grid(True)
plt.savefig('reports/benchmark_comparison_chart.png')
plt.close()

print("✓ benchmark_comparison_chart.png saved successfully!")