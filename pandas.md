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
## Diferença entre DataFrame e Series

Um DataFrame é uma tabela. Para gerar um DataFrame podemos usar `pd.DataFrame()`

## Métodos Head and Tail

1. `.head()`: ao usarmos esse método em um dataframe, ele nos retorna as 5 primeiras linhas por padrão. Se colocarmos um número como argumento dentro dos parenteses, como `patrocinios.head(n)`,  ele nos retorna as n primeiras linhas do arquivo.
2. `.tail()`: Mesma coisa, mas para as últimas linhas do dataframe.


