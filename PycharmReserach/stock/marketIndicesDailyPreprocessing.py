import numpy as np
import pandas as pd
import seaborn as sns
df = pd.read_excel(r'C:/Users/Acer/Desktop/Research/Market indices Daily.xlsx', header =0)

print(df.head(10))
print(df.dtypes)
print(df.describe())