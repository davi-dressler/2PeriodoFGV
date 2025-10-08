import pandas as pd
import numpy as np 

indices = ["Ted Lasso", "Parks & Recreation", "Vikings", "Suits", "Breaking Bad"]
colunas = ["Nota", "Temporadas", "Episódios"]
dados = [[9, 4, 34], [9, 7, 125], [9, 6, 89], [8, 9, 134], [10, 5, 62]]

df = pd.DataFrame(dados, index=indices, columns=colunas)
print (df)
print ('#'*40)

print ("Notas:") #Seleção de uma coluna
print (df["Nota"], "\n")
print ("Temporadas:")
print (df["Temporadas"], "\n")
print ("#"*40)

print ("Notas e Episódios:") #Seleção de duas colunas
print (df[["Nota", "Episódios"]], "\n")
print ("#"*40)

print ("Suits {loc}:")
print (df.loc["Suits"])

print ("Suits {loc}:")
print (df.iloc[3])
print ("#"*40)

print ("Notas de Suits:", df.loc["Suits", "Nota"]) #primeiro parâmetro: linha, segundo: coluna
print ("Notas de Suits:", df.iloc[3,0])
print ("Notas de Suits:", df.at["Suits", "Nota"]) #mais rápido
print ("#"*40)

print ("Ted Lasso e Parks & Recreation, Nota e Temporada")
print (df.loc[["Ted Lasso", "Parks & Recreation"], ["Nota", "Temporadas"]])
print ("Usando slice")
print (df.loc["Parks & Recreation":"Suits", "Temporadas":])
print (df.loc[:, ["Nota", "Temporadas"]])

#Operações
print (df.head(2))
print (df.tail(2))
print ("Valores únicos de nota:\n")
print (df["Nota"].unique())
print ("Número de valores únicos de nota:\n")
print (df["Nota"].nunique())
print ("Contagem:\n")
print (df["Nota"].count())
print ("Contagem de valores:\n")
print (df["Nota"].value_counts())

print ("Nota mínima nos dados:", df["Nota"].min())
print ("Nota máxima nos dados:", df["Nota"].max())
print ("Média das notas nos dados:", df["Nota"].mean())
print ("Mediana das notas nos dados:", df["Nota"].median())

print (df.columns)
print (df.columns.to_list()) #listas
print (df.columns.to_numpy()) #mais moderno. ndarray
print (df.columns.values)

print (df.index)
print (df.index.to_list()) #listas
print (df.index.to_numpy()) #mais moderno. ndarray
print (df.index.values)

df ["Coluna extra"] = df["Nota"]/2 #Nova coluna
print (df)

df.drop ("Coluna extra", axis=1, inplace=True) #apaga a coluna extra
print (df)

df.drop ("Vikings", inplace=True) #apaga a linha escolhida
print (df)