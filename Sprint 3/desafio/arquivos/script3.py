import pandas as pd

df = pd.read_csv('arquivo_limpo.csv', header=None)

df.iloc[:, 7] = df.iloc[:, 7].replace('[\$,]', '', regex=True).astype(float)

app_mais_caro = df.iloc[df.iloc[:, 7].idxmax()]


print("Aplicativo Mais Caro:")
print("Nome:", app_mais_caro[0])
print("Valor (em dólares):", app_mais_caro[7])