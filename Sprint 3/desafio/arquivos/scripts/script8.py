import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('arquivo_limpo.csv', header=None)

rating_counts = df[2].value_counts(normalize=True) * 100  


rating_counts_filtrado = rating_counts[rating_counts >= 1]


df_plot = pd.DataFrame({'Rating': rating_counts_filtrado.index, 'Porcentagem de Apps (%)': rating_counts_filtrado.values})


plt.figure(figsize=(10, 6))
plt.scatter(df_plot['Rating'], df_plot['Porcentagem de Apps (%)'], marker='o')
plt.title('Rating dos Apps')
plt.xlabel('Rating')
plt.ylabel('Porcentagem de Apps (%)')
plt.grid(True)
plt.show()