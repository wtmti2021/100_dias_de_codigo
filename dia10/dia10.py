# Importando as bibliotecas numpy e pandas
import numpy as np
import pandas as pd

# Definindo os dados dos funcionários por nome, departamento e salário
data = {'nome': ['Ana', 'Joao', 'Pedro', 'Francisco', 'Tatiana', 'Stella'], 'departamento': ['financeiro', 'Marketing', 'TI', 'TI', 'contabilidade', 'TI'], 'salario': [3000, 2500,4500, 4500, 2600, 7000]}

# Criando DataFrame
df = pd.DataFrame(data)

# Filtragem dos fuuncionários de TI
funcionarios_ti = df[df['departamento'] == 'TI']

# Média salarial
media_salarial = funcionarios_ti['salario'].mean()

# Exibindo resultados
print(f"Média salarial dos funcionários de TI: {media_salarial}")