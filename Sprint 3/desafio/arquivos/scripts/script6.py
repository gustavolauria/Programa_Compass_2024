import pandas as pd

df = pd.read_csv('arquivo_limpo.csv', header=None)

df_valid_reviews = df[df[3].str.isnumeric()]

df_valid_reviews[3] = df_valid_reviews[3].astype(int)


df_valid_reviews = df_valid_reviews[df_valid_reviews[3] > 0]

df_ordenado = df_valid_reviews.sort_values(by=3, ascending=False)


top_app_reviews = df_ordenado.iloc[:1, [0, 3]]

print("Top App com Mais Reviews:")
for index, row in top_app_reviews.iterrows():
    print(f"{row[0]} - {row[3]} Reviews")


apps_rating_50 = df[df[2] == 5.0].head(10)


print("\nLista dos 10 Aplicativos com Rating 5.0:")
for index, row in apps_rating_50.iterrows():
    print(f"App: {row[0]}, Rating: {row[2]}")