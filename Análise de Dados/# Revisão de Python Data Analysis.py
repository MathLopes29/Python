# Revisão de Python Data Analysis
# @author Matheus Lopes

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as srn
import statistics as sts

df = pd.read_csv("", sep=";", parse_dates=['Data'])
df.describe()
df.into()
df.head()
df.tail()
df.shape
df.isnull().sum()

df.loc[:,['Data']]
df['Data'] = pd.to_datetime(df['Data'])

df.set_index('Data', inplace=True)
df

print(df.index)

df['Categoria'].value_counts()

x = df['Total de vendas brutas']
print("Média",round(float(sts.mean(x))))
print("Mediana", float(sts.median(x)))
print("Moda", float(sts.mode(x)))
print("Desvio Padrão", round(float(sts.stdev(x))))
print("Variância",round(float(sts.variance(x))))
print("Amplitude",round(float(sts.pvariance(x))))


valor = input("Digite um valor: ")
print(f"Valor é ", {valor})
df_filtro = df[df["Quantidade"] > valor] # Filtro de Condição de coluna
if (df_filtro > 0):
    print("Quantidade Superior")
    pass
else:
    print("Quantidade Inferior")    


df.groupby('Produtos').mean() # Agrupa os dados
df.dropna(inplace=True) # Remove as colunas
df['Valor'].fillna('Média / Moda / Mediana', inplace=True) # Substitui os valores nulos

y = sts.median(df['']).size()


########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################



df.plot.bar(figsize=(15,5), rot=0, color='purple', grid=True)
plt.title("")
plt.xlabel("")
plt.ylabel("")
plt.show("")


medianaUmidade = sts.median(df["Umidade"])
df.loc[df["Umidade"]>100] = medianaUmidade

df["Umidade"].fillna(medianaUmidade, inplace=True)
df['Umidade'].plot(style='-o', linewidth=2.5, color='', figsize=(10,5), grid=True)
plt.title("")
plt.xlabel("")
plt.ylabel("")
plt.show("")

srn.boxplot(df["Temperatura"]).set_title("")
srn.boxplot(data=df)