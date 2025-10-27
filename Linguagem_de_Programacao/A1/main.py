# -*- coding: utf-8 -*-

import funcoes as f
import numpy as np
import unittest


#Questão 1

class TestValidacao(unittest.TestCase):
    
    def test_valido(self):
        self.assertTrue(f.validar_cnpj("40.688.134/0001-61"))
    
    def test_invalido(self):
        self.assertFalse(f.validar_cnpj("52.771.293/0001-12"))
        self.assertFalse(f.validar_cnpj("11.111.111/1111-11"))

#Questão 2

@f.cache_resultados
def multiplicar(a, b):
    return a*b

# print(multiplicar(2, 10)) # Valor armazenado no cache. 20
# print(multiplicar(4, 10)) # Valor armazenado no cache. 40
# print(multiplicar(2, 8)) # Valor armazenado no cache. 16

@f.cache_limitado(2)
def somar(a, b):
    return a+b

print(somar(42,13)) # Valor armazenado no cache. 55
print(somar(42,13)) # Resultado retornado do chache. 55
print(somar(10,13)) # Valor armazenado no cache. 23
print(somar(8,13)) # Último valor removido do cache. Valor atual armazenado no cache. 21

#Questão 3

try:
    
    f.converter_data("22/08/2009")
    
except Exception:
    print("Ocorreu uma exceção.")

try:
    
    f.converter_data("22082009")
    
except ValueError:
    print("Argumento recebido possui formato inválido.")

try:
    
    f.converter_data("54/13/2009")
    
except f.DateError:
    print("Data inválida.")

#Questão 4
arr1 = np.array([1,2,3,10,5,7])
print(f.normalizar(arr1)) # Retorna [0.         0.11111111 0.22222222 1.         0.44444444 0.66666667]

arr = np.array([1,2,3,54,7,8,9,5,35,6,7,64])
print(f.calcular_estatisticas(arr)) # Retorna média, desvio padrão, (16.75, 20.793127871166153)

if __name__ == "__main__":
    unittest.main()