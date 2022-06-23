# Autor: Fabiana Bezerra Mangili
# Date: 23/05/2022

import pandas as pd
import pymannkendall as mk
import os

os.chdir('indices_org/rx5day/')
lista_trends = []

for i in os.listdir(os.path.join(os.getcwd(), 'data')):
    nome = i.split('_')
    nome_arquivo = nome[1]
    df = pd.read_csv(os.path.join(os.getcwd(), 'data', i), sep=',')
    result = mk.original_test(df.iloc[:, 1])

    arquivo = [nome_arquivo, result.z, result.slope, 'Postivo' if result.slope >= 0 else 'Negativo', 'Significativo' if
    (result.z <= 1.96 and result.z >= -1.96) else 'Não Significativo']
    lista_trends.append(arquivo)

tendencias_df = pd.DataFrame(lista_trends,
                             columns=['Codigo', 'MK_z', 'Slope', 'MK_slope', 'Sig_slope'])
print(tendencias_df.to_string())
#tendencias_df.to_csv(os.getcwd()+'_trends.csv', sep=';', index=False)
