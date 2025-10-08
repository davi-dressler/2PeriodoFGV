# Introdução ao Pandas
## Importando a Biblioteca

`import pandas as pd`

## Como abrir um arquivo

Primeiro, confira se o seu arquivo .csv está no mesmo diretório que o arquivo utilizado para o seu projeto. Tendo, então, um arquivo `patrocinios.csv`.

```python
pd.read_csv("patroinios.csv")
```
Para não ter que escrever sempre a função `pd.read_csv`, podemos atribuir o valor da função a uma variável.

```python
patrocinios = pd.read_csv("patroinios.csv")
```

O pandas cria um índice próprio para as colunas ao criar um DataFrame. Para selecionar uma coluna da tabela como o índice das linhas podemos usar o parâmetro `index_column = numero_da_coluna`.

## Diferença entre DataFrame e Series

1. DataFrame: Um DataFrame é uma tabela. Para gerar um DataFrame podemos usar `pd.DataFrame()`
  
2. Series: Uma série é uma sequência de valores. Se um DataFrame é uma tabela, uma Series seri uma lista, uma coluna únida do DataFrame. Você pode atribuir rótulos de linhas usando o parâmetro `index`.

```python
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
```


## Métodos Head and Tail

1. `.head()`: ao usarmos esse método em um dataframe, ele nos retorna as 5 primeiras linhas por padrão. Se colocarmos um número como argumento dentro dos parenteses, como `patrocinios.head(n)`,  ele nos retorna as n primeiras linhas do arquivo.
   
2. `.tail()`: Mesma coisa, mas para as últimas linhas do dataframe.

## Acessando o conteúdo da tabela

Há duas maneiras de acessar uma Series específica de um DataFrame:

1. `DataFrame.nome_da_coluna`

2. Parecido com um dicionário de python: `DataFrame["nome_da_coluna"]`. Se quisermos ainda retornar o valor específico do índice n em uma Series, podemos usar `DataFrame["nome_da_coluna"][n]`.

## Acessando o data type de cada coluna

1. Método `dtypes`

```python
df = pd.read_csv("nome_do_arquivo.csv")
df.dtypes
```

## Indexação

Para saber os índices das linhas podemos usar `.index` e para saber os rótulos das colunas podemos usar `.columns`:

```python
df = pd.read_csv("nome_do_arquivo.csv")
df.index

df.columns
```

## Apresentando uma visão geral estatística de cada coluna

`.describe()` retorna algumas estatísticas de cada coluna.

## Transpondo os dados

Assim como no numpy, nós podemos fazer utilizando o método `.T`:

```python
df = pd.read_csv("nome_do_arquivo.csv")
df.T #Linhas viram colunas e colunas viram linhas
```

## Ordenando os dados pelo índice

Podemos fazer isso através do método `.sort_index()`, que ordena pelos índices, ou das colunas, ou das linhas:

```python
df = pd.read_csv("nome_do_arquivo.csv")
df_ordenado_pelas_linhas = df.sort_index() #Ordenado pelo índice das linhas (Crescente por padrão)

df_ordenado_pelas_linhas_decrescente = df.sort_index(ascending= False) #Ordenado pelo índice das linhas (Decrescente)

df_ordenado_pelas_colunas = df.sort_index(axis= 1) #Ordenado pelo índice das colunas (Crescente por padrão)

df_ordendado_pelas_colunas_decrescente = df.sort_index(axis= 1, ascending= False) #Ordenado pelo índice das colunas (Decrescente)
```

É possível também usar o parâmetro `inplace`, por padrão esse parâmetro recebe `False`, o que quer que o `.sort_index()` não altera o DataFrame original, mas cria um novo com a ordenação aplicada. Caso `inplace` seja definido como `True`, então o DataFrame original será alterado e o `.sort_index()` retornará `None`.

```python
df = pd.read_csv("nome_do_arquivo.csv")
df.sort_index(inplace= True) #O DataFrame original foi ordenado pelo índice das linhas (Crescente por padrão)
```

Parâmetros facultativos:

1. `axis` : Altera o eixo da ordenação. Recebe 0 por padrão (linhas), Pode receber 1 (colunas).
2. `ascending` : Define se é crescente ou não. Recebe True por padrão (crescente), pode receber False (decrescente).
3. `inplace` : Define se um novo DataFrame ordenado será criado, ou se o DataFrame original que vai ser modificado. Recebe False por padrão, pode receber True.


Também podemos fazer isso através do método `.sort_values()`, que ordena pelos valores das colunas:

Parâmetros obrigatórios:

1. `by`: É preciso especificar a coluna base pela qual a ordenação dos valores será feita.

```python
dados = {
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Ana'],
    'Idade': [22, 35, 29, 41, 25],
    'Pontuação': [88, 95, 74, 91, 95]
}
df = pd.DataFrame(dados)

df_ordenado_pela_coluna_pontuacao = df.sort_values(by= "Pontuação") #Crescente por padrão

```

É possível usar o `by` com múltiplas colunas:

```python

df_ordenado_pela_coluna_pontuacao_e_nome = df.sort_values(by= ["Pontuação", "Nome"]) #Crescente por padrão

```

Passando uma lista de colunas para o parâmetro by, o Pandas usará a primeira coluna da lista como base para a ordenação e em caso de empate (ex: valores iguais), será usada a segunda coluna como abse para desempatar a ordenação.

Parâmetros facultativos:

2. `ascending`: Define se a ordenação é crescente ou não. É possível passar apenas um valor booleano, ou no caso de uma lista como parâmetro by, uma lista de valores booleanos cada um sendo correspondente a uma coluna do parâmetro by.
3. `inplace`: False por padrão, retorna um novo DataFrame com a ordenação aplicada. Caso True, o DataFrame original é modificado e retorna None.
4. `na_position`: contola onde NaN será colocados. O padrão é `last` (colocados no final), mas se definirmos como `first` serão colocados no início.

## Seleção

### Getitem([ ])

```python
>>>dates = pd.date_range("20130101", periods=6)

>>>dates
 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

>>>df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

>>>df

                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
```
Para um dataframe, se passarmos um único rótulo de coluna, será retornado uma Series correspondente a coluna selecionada.

```python

df["A"] #Retorna a serie correspondente a coluna A (mesma coisa que fazer df.A)

```

Ao fazermos um silce, o que será retornado serão as linhas correspodentes aos índices estabelecidos.

```python

df[0:3] #Retorna as linhas de 0 a 3, exclusive.

df["20130102":"20130104"] #Retorna as linhas com rótulo 20130102 a 20130104, inclusive.

```

### Seleção por rótulo
Usando `DataFrame.loc` e `DataFrame.at()`.

```python

df.loc["2013-01-01"] #Retorna a linha correspondente ao rótulo

```

Podemos selecionar tmbém todas as linhas com algumas colunas estabelecidas:

```python
df.loc[:, ["A", "B"]] #Retorna todas as linhas das colunas A e B
```
É possível fazer o slice nas linhas aqui também.

Selecionar uma linha única e uma coluna única retorna a entrada na linha e coluna especificadas:

```python
>>> df.loc["2013-01-01", "B"] 

-0.282863
```

Para acessar a entrada de forma mais rápida usamos o método `.at`:

```python
>>> df.at["2013-01-01", "B"] 

-0.282863
```

### Seleção por posição
Usando `DataFrame.iloc` e `DataFrame.iat()`.

Selecinando através de índices numéricos:

```python 
df.iloc[3] #Retorna a quarta coluna. (índices começando em 0)

df.iloc[3:5, 0:2] #Retorna a 4º e 5º linhas da 1º e 2º coluna (de 3 a 5, exclusive e de 0 a 2, exclusive) OBS: Note o padrão da lei de lico, primeiro linhas, depois colunas.

df.iloc[[1,2,4], [0,2]] #Ao ser dado uma lista de inteiros ele retorna as linhas e colunas dos índices dados.

df.iloc[1:3, :] #Retorna todas as colunas das 2º e 3º linhas. OBS: É possível fazer a mesma coisa com as colunas.

df.iloc[1, 1] #Para buscar uma entrada específica.

df.iat[1, 1] #Retorna a mesma coisa, mas o rocesso é masi rápido.

```

## Indexação Boolenana

Selecionar as linhas onde a entradas da coluna "A" são maiores do que 0:

```python
df[df["A"] > 0]
```

Selecionar os valores do DataFrame inteiro que são maiores do que zero:

```python
df[df > 0]
```

Filtrando usando `.isin`:

```python
df[df["A"].isin([1,2,3])] #Retorna todas as linhas cujas entradas estão na lista dada.
```














