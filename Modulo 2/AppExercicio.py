import numpy as np
import pandas as pd

df = pd.read_csv("https://pycourse.s3.amazonaws.com/bike-sharing.csv")

df.describe
df

print('Qual a média da coluna windspeed: ',df['windspeed'].mean())
print('Qual a média da coluna temp: ',df['temp'].describe())
print('Quantos registros existem para o ano de 2011: \n', df[df['year'] == 0])
print('Quantos registros existem para o ano de 2012:\n',df[df['year'] == 1])
print('Qual a média da coluna windspeed: ', df['windspeed'].mean())

# Verificando Coluna 'Anos'
df = df.set_index('year')
x = df.loc[df.index == 1, ['total_count']].values
z = df.loc[df.index == 0, ['total_count']].values
y = df['total_count'].values

print(f'Total de locações em 2012: {np.sum(x)}')
print(f'Total de locações em 2011: {np.sum(z)}')
print(f'Total geral de locações: {np.sum(y)}')

# Locação
print('Qual estação do ano contém a maior média de locações de bicicletas?')
print('Qual estação do ano contém a menor média de locações de bicicletas?\n')
print(df.groupby(by='season').mean())

print('Qual horário do dia contém a maior média de locações de bicicletas?')
print('Qual horário do dia contém a menor média de locações de bicicletas?\n')
df.groupby(by='hour')
print(df.groupby(by='hour').mean())

print('Que dia da semana contém a maior média de locações de bicicletas?')
print('Que dia da semana contém a menor média de locações de bicicletas?\n')
df.groupby(by='weekday')
print(df.groupby(by='weekday').mean())

print('Às quartas-feiras (weekday = 3), qual o horário do dia contém a maior média de locações de bicicletas?')
df = df.set_index('weekday')
q = df.loc[df.index == 3, ['hour', 'total_count']]
q.groupby(by='hour')
print(q.groupby(by='hour').mean())

print('Aos sábados (weekday = 6), qual o horário do dia contém a maior média de locações de bicicletas?')
s = df.loc[df.index == 6, ['hour', 'total_count']]
s.groupby(by='hour')
print(s.groupby(by='hour').mean())
