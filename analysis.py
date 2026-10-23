import pandas as pd 
prices = pd.Series([100.0, 101.5, 100.8, 102.3, 103.1]) 
returns = prices.pct_change().dropna() 
print(returns) 
