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

# Closures

Uma closure é uma função que se "lembra" do ambiente em que ela foi criada. Isto significa que ela tem acesso a variáveis de uma função exterior. Uma closure é criada quando uma função aninhada (uma função definida dentro de outra função) faz referência a uma função no escopo de sua função externa.

## Condições para que uma closure exista

1. Função Aninhada: Há uma função definida dentro de outra função.
2. Referência a uma variável externa: A função interna faz referência a uma variável definida na função externa.
3. Retorno da função aninhada: A função externa deve retornar a função interna.

```python
def criar_multiplicador(n):
    """
    Esta é a função externa (fábrica de funções).
    Ela cria e retorna uma nova função (a closure) que multiplica
    um número pelo valor de 'n'.
    """
    def multiplicador(x):
        """
        Esta é a função aninhada. Ela tem acesso à variável 'n'
        do escopo da função externa 'criar_multiplicador'.
        """
        return x * n
    
    return multiplicador

```

Neste exemplo, a função apenas faz referencia a variável "n" externa, se dentro da função interna, você declarar `n = 5`, você estará criando uma variável local no escopo da função multiplicador que também se chama n e multiplicador retornará `x * 5`.

# Global e Nonlocal Estatements

```python
def externa(numero):
    def interna():
        print(numero)
    interna()
    print(numero)
    
externa(9)

>>> 9
>>> 9
```

Nesse exemplo, temos uma closure que faz referência a uma variável `numero` definida na fução externa. Se quisermos mudar seu valor na função interna precisamos usar `nonlocal`.

```python
def externa(numero):
    def interna():
        nonlocal numero
        numero = 5
        print(numero)
    interna()
    print(numero)
    
externa(9)

>>> 5
>>> 9
```

Ao definirmos uma variável no escopo global, podemos também referenciá-la dentro de uma função. Porém, se tentarmos alterar seu valor dentro da função, a função criará uma nova variável dentro do escopo local com o mesmo nome e não irá alterar a global.

```python
X = 88
                       
def func():
    X = 99
                    
func()
print(X)

>>> 88                       
```

Se quisermos alterar a variável global, podemos usar `global` para declará-la dentro da função.

```python
X = 88
                       
def func():
    nonlocal X 
    X = 99
                    
func()
print(X)

>>> 99                       
```

# Bound vs Unbound Methods

. `minha_string.upper` é um bound method porque é acedido através de uma instância (minha_string).

. `str.upper` é um unbound method (uma função simples) porque é acedido através da classe (str). Para usá-lo, terias de passar a instância manualmente: `str.upper(minha_string)`.

# Unittest

## Criando testes unitários para o seu programa 

A biblioteca padrão unitests do python, permite que você faça testes unitários do seu código. Ou seja é possível verificar se cada unidade do código (funções...) está funcionando como deveria.

1. Test Case: Um test case é uma unidade de teste individual. O mesmo verifica uma resposta específica a um determinado conjunto de entradas. O unittest fornece uma classe base, TestCase, que pode ser usada para criar novos casos de teste.

2. Test Suit: Uma test suite é uma coleção de casos de teste, conjuntos de teste ou ambos. O mesmo é usado para agregar testes que devem ser executados juntos.

Um test case é criado ao criar uma subclasse da classe base `unittest.TestCase`. Todos os testes devem começar com `test` (ex: test_upper, test_split...) para que o test runner seja informado de quais métodos são testes.

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

## Tabela de Asserção

|Método| Avalia - se|
|---|---|
|assertEqual(a, b)|a == b|
|assertNotEqual(a, b)| a != b|
|assertTrue(x)| bool(x) is True|
|assertFalse(x)| bool(x) is False|
|assertIs(a, b)| a is b|
|assertIsNot(a, b)| a is not b|
|assertIsNone(x) |x is None|
|assertIsNotNone(x)| x is not None|
|assertIn(a, b)| a in b|
|assertNotIn(a, b)| a not in b|
|assertIsInstance(a, b)| isinstance(a, b)|
|assertNotIsInstance(a, b)| not isinstance(a, b)|
|assertRaises(exc, fun, *args, **kwds)|fun(*args, **kwds) levanta exc|

# Functools
## @wraps

É comum termos o problema de quando criamos um decorador a função decorada perde suas características. Por exemplo, o nome e a documentação da função decorada se tornam os do decorador. Ao usar `@wraps` no decorador as caracterísicas da função continuam as mesmas.

```python
from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

>>> example()
'Calling decorated function'
'Called example function'
>>> example.__name__
'example'
example.__doc__
'Docstring'
```

Sem o @wraps o `example.__name__` retornaria `wrapper`e o `example.__doc__` retornaria `None`.

