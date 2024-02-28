import pandas as pd

df = pd.read_csv('arquivo_limpo.csv', header=None)

qtd_apps_mature = df.iloc[:, 8].str.contains("Mature 17+").sum()


print("Quantidade de Apps com 'Mature 17+':", qtd_apps_mature)