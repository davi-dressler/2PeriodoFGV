# Introdução ao Pandas

## Como abrir um arquivo

Primeiro, confira se o seu arquivo .csv está no mesmo diretório que o arquivo utilizado para o seu projeto. Tendo, então, um arquivo `patrocinios.csv`.

```python
pd.read_csv("patroinios.csv")
```
Para não ter que escrever sempre a função `pd.read_csv`, podemos atribuir o valor da função a uma variável.

```python
patrocinios = pd.read_csv("patroinios.csv")
```

## Métodos Head and Tail

`.head()`: ao usarmos esse método em um dataframe podemos 
