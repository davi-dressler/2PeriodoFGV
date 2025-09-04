# Cópias

## Diferença entre cópia rasa e cópia profunda

As instruções de atribuição em Python não criam objetos, elas apenas criam ligações entre um destino e um objeto.
Para coleções que são mutáveis ou contém itens mutáveis, às vezes é necessária uma cópia para que seja possível alterar uma cópia sem alterar a outra.

Para isso nós temos o módulo `copy` que nos permite trabalhar com cópias rasas e profundas.

```python
import copy
copy.copy(obj) #Retorna uma cópia rasa de obj.
copy.deepcopy(obj[, memo]) #Retorna uma cópia profunda de obj.
```

A diferença entre cópia profunda e cópia rasa só é relevante para objetos compostos (objetos que contém outros objetos, listas de listas, dicionários de dicionários...)

1. Uma cópia rasa constrói um novo objeto composto e então insere nele referências aos objetos encontrados. Ou seja, se você tentar alterar algum dos elemento dentro de seus objetos, você estará alterando o original também.
2. Uma cópia profunda constrói um novo objeto composto e então, insere nele cópias dos objetos encontrados no original.
   
Cópias rasas de dicionários podem ser feitas usando `dict.copy()`, e de listas atribuindo uma fatia de toda a lista, por exemplo, `lista_copiada = lista_original[:]`.

```python
import copy
lista = [[1], [1, 2], [1, 3], [1, 2, 4], [1, 5], [1, 2, 3, 6], [1, 7]]
lista_copiada = lista[:]
print(lista_copiada)

>>>[[1], [1, 2], [1, 3], [1, 2, 4], [1, 5], [1, 2, 3, 6], [1, 7]]

lista_copiada[0][0] = 50
print(lista)
print(lista_copiada)

>>>[[50], [1, 2], [1, 3], [1, 2, 4], [1, 5], [1, 2, 3, 6], [1, 7]]
>>>[[50], [1, 2], [1, 3], [1, 2, 4], [1, 5], [1, 2, 3, 6], [1, 7]]
```
Então, se eu tento mudar algum objeto dentro do objeto copiado por cópia rasa, o original também muda. A mesma coisa acontece se eu mudar o original depois de ter feito a cópia, a cópia será alterada. (Em `lista_copiada = lista_original[:]`, os valores antes e depois dos : dentro dos colchetes são os instervalos de elementos que queremos copiar).

Diferente de quando eu faço uma cópia profunda.

```python
lista_copiada_profunda = copy.deepcopy(lista)
lista_copiada_profunda[0][0] = 50
print(lista_copiada_profunda)
print(lista)

>>>[[50], [1, 2], [1, 3], [1, 2, 4], [1, 5], [1, 2, 3, 6], [1, 7]]
>>>[[1], [1, 2], [1, 3], [1, 2, 4], [1, 5], [1, 2, 3, 6], [1, 7]]
```