import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('arquivo_limpo.csv', header=None)


rating_counts = df[8].value_counts(normalize=True) * 100  

rating_counts_filtrado = rating_counts[rating_counts >= 1]

plt.figure(figsize=(10, 6))
rating_counts_filtrado.plot(kind='line', marker='o', linestyle='-')
plt.title('Classificacao dos Apps')
plt.xlabel('Classificacao')
plt.ylabel('Porcentagem de Apps (%)')
plt.grid(True)
plt.show()