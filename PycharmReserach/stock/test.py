import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel(r'C:/Users/Acer/Desktop/Research/Market indices Daily.xlsx', header = 0)
print(df.head(10))

print(df.dtypes)
df[['Date','ASPI']].plot('Date', figsize=(15,8))
plt.show()


