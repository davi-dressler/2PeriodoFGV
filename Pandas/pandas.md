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

## Indexação






