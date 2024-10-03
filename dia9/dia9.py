# 1º passo: instalar as bibliotecas numpy e pandas pelo TERMINAL (feito)

# 2º passo: Importar as 2 bibliotecas instaladas
import numpy as np
import pandas as pd

# 3º passo:criando Dataframe
data = {'vendas': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]}
df = pd.DataFrame(data)

# 4º passo: criar operações (media, mediana, desvio padrão, máximo e mínimo da coluna numérica "vendas")
media = df['vendas'].mean()
mediana = df["vendas"].median()
desvio_padrao = df['vendas'].std()
maximo = df['vendas'].max()
minimo = df['vendas'].min()
# Resultados
print("Média:", media)
print("Mediana:", mediana)
print("Desvio Padrão:", desvio_padrao) 
print("Máximo:", maximo)
print("Mínimo:", minimo)


