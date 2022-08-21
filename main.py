import pandas as pd
from ft_linear_regression import ft_linear_regression

lr = ft_linear_regression.linearRegression()
# df = pd.DataFrame(data = {"km": [1, 2,3, 4], "price":[20, 25, 30, 35]})
df = pd.read_csv("data.csv")
lr.train(df)