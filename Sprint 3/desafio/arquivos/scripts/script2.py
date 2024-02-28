import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('arquivo_limpo.csv')

categorias_contagem = df[df.iloc[:, 1] != '1.9'].iloc[:, 1].value_counts()

total_ocorrencias = categorias_contagem.sum()
categorias_outros = categorias_contagem[categorias_contagem / total_ocorrencias < 0.02]

categorias_contagem['OUTROS'] = categorias_outros.sum()
categorias_contagem = categorias_contagem.drop(categorias_outros.index)

plt.figure(figsize=(8, 8))
plot = categorias_contagem.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Categorias')
plt.ylabel('')
plt.axis('equal')  

for text in plot.texts:
    text.set_fontsize(8)

plt.show()