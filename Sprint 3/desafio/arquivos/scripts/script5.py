import pandas as pd

df = pd.read_csv('arquivo_limpo.csv', header=None)


df_valid_reviews = df[df[3].str.isnumeric()]

df_valid_reviews[3] = df_valid_reviews[3].astype(int)


df_valid_reviews = df_valid_reviews[df_valid_reviews[3] > 0]

df_ordenado = df_valid_reviews.sort_values(by=3, ascending=False)


top_10_apps_reviews = df_ordenado.iloc[:10, [0, 3]]

print("Top 10 Apps com Mais Reviews:")
for index, row in top_10_apps_reviews.iterrows():
    print(f"{row[0]} - {row[3]} Reviews")