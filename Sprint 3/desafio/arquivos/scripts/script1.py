import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('arquivo_limpo.csv')

top_apps = df[df.iloc[:, 5] == '1,000,000,000+'].head(5)


nomes_apps = top_apps.iloc[:, 0]
num_instalacoes = top_apps.iloc[:, 5]

num_instalacoes = num_instalacoes.str.replace('+', '').str.replace(',', '').astype(int)

plt.figure(figsize=(10, 6))
plt.bar(nomes_apps, num_instalacoes, color='skyblue')
plt.xlabel('Apps')
plt.ylabel('Número de Instalações (em bilhões)')
plt.title('Top 5 Apps com Maior Número de Instalações')


plt.xticks(rotation=0, ha='center', fontsize=7)

plt.tight_layout()
plt.show()
