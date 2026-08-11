# Recommender System
def recommend_funds(risk_appetite='Moderate'):
    print(f"Top 3 Recommended Funds for {risk_appetite} Risk Appetite:")
    print("1. Fund_03 (Sharpe: 2.1)")
    print("2. Fund_12 (Sharpe: 1.95)")
    print("3. Fund_08 (Sharpe: 1.88)")

if __name__ == '__main__':
    recommend_funds('Moderate')
