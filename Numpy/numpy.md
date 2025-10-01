# Biblioteca Numpy

```python
import numpy as np
```

## Arrays
Em programação, um array é uma estrutura para armazenar e recuperar dados. O NumPy se destaca quando há grandes quantidades de dados "homogêneos" (do mesmo tipo) a serem processados ​​na CPU.

### Restrições
1. Todos os elementos da matriz devem ser do mesmo tipo de dados.
2. Uma vez criado, o tamanho total do array não pode ser alterado.
3. O formato deve ser “retangular”, não “irregular”; por exemplo, cada linha de uma matriz bidimensional deve ter o mesmo número de colunas.

## Fundamentos de Arrays

```python
>>>a = np.array([1, 2, 3, 4, 5, 6])
>>>a
arrray([1, 2, 3, 4, 5, 6])
```

É possivel acessar arrays quase da mesma forma que acessamos listas.

```python
>>>a[0] #Podemos usar a indexação
1
>>>a[0] = 10 #ndarrays são mutáveis
>>>a
array([10, 2, 3, 4, 5, 6])
>>>a[:3] #O slice funciona
array([10, 2, 3])
```

Uma grande diferença é que a indexação por fatias de uma lista copia os elementos para uma nova lista, mas fatiar um array retorna uma view : um objeto que se refere aos dados do array original. O array original pode ser modificado usando a view.

```python
>>>b = a[3:]
>>>b
array([4, 5, 6])
>>>b[0] = 40
>>>a
array([ 10,  2,  3, 40,  5,  6])
```

Matrizes bidimensionais e de dimensões superiores podem ser inicializadas a partir de sequências Python aninhadas:

```python
>>>a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
>>>a
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
```

Outra diferença entre um array e uma lista de listas é que um elemento do array pode ser acessado especificando o índice ao longo de cada eixo dentro de um único conjunto de colchetes, separados por vírgulas. Por exemplo, o elemento 8 está na linha 1 e coluna 3:

```python
>>>a[1, 3]
8
```

## Atributos de uma matriz

O número de dimensões de uma matriz está contido no `ndim`. O formato (shape) de uma matriz é uma tupla de números inteiros não negativos que especificam o número de elementos ao longo de cada dimensão.

```python
>>>a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
>>>a.ndim
2

>>>a.shape
(3, 4)
>>>len(a.shape) == a.ndim
True
```

O número total fixo de elementos na matriz está contido no atributo `size`.

```python
>>>a.size
12
```

Arrays são tipicamente "homogêneos", o que significa que contêm elementos de apenas um "tipo de dado". O tipo de dado é registrado no dtypeatributo.

```python
>>>a.dtype
dtype('int64')  # "int" for integer, "64" for 64-bit
```

## Criando arrays básicos

`np.zeros()` , `np.ones()`, `np.empty()`, `np.arange()`, `np.linspace()`

Além de criar um array a partir de uma sequência de elementos, você pode facilmente criar um array preenchido com 0's:
```python
>>>np.zeros(2)
array([0., 0.])
```

Ou uma matriz preenchida com 1's:
```python
>>>np.ones(2)
array([1., 1.])
```

Você pode criar uma matriz com um intervalo de elementos:
```python
>>>np.arange(4)
array([0, 1, 2, 3])
```

E até mesmo uma matriz que contém um intervalo de intervalos uniformemente espaçados. Para fazer isso, você especificará o primeiro número , o último número e o tamanho do passo .
```python
>>>np.arange(2, 9, 2)
array([2, 4, 6, 8])
```

Você também pode usar `np.linspace()` para criar uma matriz com valores espaçados linearmente em um intervalo especificado:
```python
>>>np.linspace(0, 10, num=5)
array([ 0. ,  2.5,  5. ,  7.5, 10. ])
```

Podemos criar matrizes cheias usando:
```python
>>>x = np.full((5,5), 42) #Cria um array (5,5) com todas as entradas como 42
>>>x
```

### Especificando seu tipo de dados

Embora o tipo de dado padrão seja ponto flutuante ( np.float64), você pode especificar explicitamente qual tipo de dado deseja usando a dtypepalavra-chave.
```python
>>>x = np.ones(2, dtype=np.int64)
>>>x
array([1, 1])
```

# Adicionar, remover e classificar elementos

`np.sort()` ,`np.concatenate()`

Classificar um array é simples com np.sort(). Você pode especificar o eixo, o tipo e a ordem ao chamar a função. Se você começar com esta matriz:
```python
>>>arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
```

Você pode classificar rapidamente os números em ordem crescente com:
```python
>>>np.sort(arr)
array([1, 2, 3, 4, 5, 6, 7, 8])
```
Se você começar com essas matrizes:
```python
>>>a = np.array([1, 2, 3, 4])
>>>b = np.array([5, 6, 7, 8])
```

Você pode concatená-los com np.concatenate().
```python
>>>np.concatenate((a, b))
array([1, 2, 3, 4, 5, 6, 7, 8])
```

Ou, se você começar com essas matrizes:
```python
>>>x = np.array([[1, 2], [3, 4]])
>>>y = np.array([[5, 6]])
```

Você pode concatená-los com:
```python
>>>np.concatenate((x, y), axis=0)
array([[1, 2],
       [3, 4],
       [5, 6]])
```

Para remover elementos de um array, podemos usar a indexação para selecionar os elementos que desejamos manter.

# Remodelando um array

`arr.reshape()`

Usar `arr.reshape()` dará um novo formato a um array sem alterar os dados. Lembre-se de que, ao usar o método reshape, o array que você deseja produzir precisa ter o mesmo número de elementos que o array original. Se você começar com um array com 12 elementos, precisará garantir que o novo array também tenha um total de 12 elementos.

Se você começar com esta matriz:
```python
>>>a = np.arange(6)
>>>print(a)
[0 1 2 3 4 5]
```

Você pode usar `reshape()` para remodelar sua matriz. Por exemplo, você pode remodelar esta matriz para uma matriz com três linhas e duas colunas:
```python
>>>b = a.reshape(3, 2)
>>>print(b)
[[0 1]
 [2 3]
 [4 5]]
```

# Indexação e fatiamento 

Você pode indexar e fatiar matrizes NumPy da mesma forma que pode fatiar listas Python.
```python
>>>data = np.array([1, 2, 3])

>>>data[1]
2

>>>data[0:2]
array([1, 2])

>>>data[1:]
array([2, 3])

>>>data[-2:]
array([2, 3])
```

# Indexação Condional
Se você quiser selecionar valores do seu array que atendam a certas condições, isso é simples com o NumPy.

Por exemplo, se você começar com esta matriz:
```python
>>>a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
```

Você pode imprimir  todos os valores na matriz que são menores que 5.
```python
>>>print(a[a < 5])
[1 2 3 4]
```

Você também pode selecionar, por exemplo, números iguais ou maiores que 5 e usar essa condição para indexar uma matriz.
```python
>>>five_up = (a >= 5)
>>>print(a[five_up])
[ 5  6  7  8  9 10 11 12]
```

Você pode selecionar elementos que são divisíveis por 2:
```python
>>>divisible_by_2 = a[a%2==0]
>>>print(divisible_by_2)
[ 2  4  6  8 10 12]
```

Ou você pode selecionar elementos que satisfaçam duas condições usando os operadores & and :|
```python
>>>c = a[(a > 2) & (a < 11)]
>>>print(c)
[ 3  4  5  6  7  8  9 10]
```
### Indexação Booleana Condicional
Você também pode usar os operadores lógicos & e | para retornar valores booleanos que especificam se os valores em uma matriz atendem ou não a uma determinada condição. Isso pode ser útil com matrizes que contêm nomes ou outros valores categóricos.

```python
>>>array_ = np.array([10,15,20,25,30,40])

>>>print("Valores maiores que 20:", array_[array_ > 20])
Valores maiores que 20: [25 30 40]

>>>print("Valores maiores que 20:", array_ > 20)
Valores maiores que 20: [False False False  True  True  True]

>>>five_up = (a > 5) | (a == 5)
>>>print(five_up)
[[False False False False]
 [ True  True  True  True]
 [ True  True  True True]]
```


