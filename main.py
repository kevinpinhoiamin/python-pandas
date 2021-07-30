import pandas as pd

# pd.set_option('display.max_rows', 1000)
# pd.set_option('display.max_columns', 1000)


# Estruturas de dados
carros = ['Jetta Variant', 'Passat', 'Crossfox']
print(carros)
print(pd.Series(carros))

# Criando um DataFrame a partir de uma lista de dicionários
dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False,
     'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False,
     'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False,
     'Valor': 72832.16}
]
dataset = pd.DataFrame(dados)
print(dataset)
dataset[['Nome', 'Motor', 'Ano', 'Quilometragem', 'Zero_km', 'Valor']]
print(dataset)

# Criando um DataFrame a partir de um dicionário
dados = {
    'Nome': ['Jetta Variant', 'Passat', 'Crossfox'],
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],
    'Ano': [2003, 1991, 1990],
    'Quilometragem': [44410.0, 5712.0, 37123.0],
    'Zero_km': [False, False, False],
    'Valor': [88078.64, 106161.94, 72832.16]
}
dataset = pd.DataFrame(dados)
print(dataset)

# Criando um DataFrame a partir de um arquivo externo
dataset = pd.read_csv('data/db.csv', sep=';', index_col=0)
print(dataset)
print(dataset.head())

# Seleciona colunas
print(dataset['Valor'])
print(type(dataset['Valor']))
print(dataset[['Valor']])
print(type(dataset[['Valor']]))

# Selecionando linhas
print(dataset[0:3])

# Utilizando .loc para seleções
print(dataset.loc['Passat'])
print(dataset.loc[['Passat', 'DS5']])
print(dataset.loc[['Passat', 'DS5'], ['Motor', 'Valor']])
print(dataset.loc[:, ['Motor', 'Valor']])

# Utilizando .iloc para seleções (com base nos índices numéricos)
print(dataset.iloc[[1]])
print(dataset.iloc[1:4])
print(dataset.iloc[1:4, [0, 5, 2]])
print(dataset.iloc[[1, 42, 22], [0, 5, 2]])
print(dataset.iloc[:, [0, 5, 2]])

# Queries com DataFrames
print(dataset.Motor)
select = dataset.Motor == 'Motor Diesel'
print(select)
print(type(select))
print(dataset[select])
print(dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)])
print((dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True))

# Utilizando o método query
print(dataset.query('Motor == "Motor Diesel" and Zero_km == True'))

# Iterando com DataFrames
for item in dataset:
    print(item)

for index, row in dataset.iterrows():
    if 2019 - row['Ano'] != 0:
        dataset.loc[index, 'Km_media'] = row['Quilometragem'] / (2019 - row['Ano'])
    else:
        dataset.loc[index, 'Km_media'] = 0
print(dataset)

# Tratamento de dados
print(dataset.info())
print(dataset.Quilometragem.isna())
print(dataset[dataset.Quilometragem.isna()])
dataset.fillna(0, inplace=True)
print(dataset.query("Zero_km == True")[['Quilometragem', 'Zero_km']])

dataset = pd.read_csv('data/db.csv', sep=';')
print(dataset)
dataset.dropna(subset=['Quilometragem'], inplace=True)
print(dataset)
