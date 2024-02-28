import pandas as pd

df = pd.read_csv('googleplaystore.csv')

df_sem_duplicatas = df.drop_duplicates(subset=df.columns[0])

df_sem_duplicatas.to_csv('arquivo_limpo.csv', index=False, header=False)

df = pd.read_csv('arquivo_limpo.csv')  

def remover_cifrão(valor):
    if pd.isna(valor):
        return valor  
    elif isinstance(valor, str) and valor.startswith('$'):
        return valor[1:]  
    else:
        return '0'  

df.iloc[:, 7] = df.iloc[:, 7].apply(lambda x: remover_cifrão(x)) 

df.to_csv('arquivo_limpo.csv', index=False, header=False)