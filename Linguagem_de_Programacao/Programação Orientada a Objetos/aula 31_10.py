# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 07:48:23 2025

@author: C3007807
"""

class Guerreiro:
    
    def __init__(self, nome: str):
        self._nome = nome
        self._arma = None
        
    def atacar(self):
        if not self._arma:
            print(f"{self._nome} ataca com as mãos e causa 1 de dano.")
        
        if self._arma:
            print(f"{self._nome} ataca com {self._arma} e causa 1 de dano.")
            
class Feiticeiro:
    
    def __init__(self, nome: str):
        self._nome = nome
        self._encantamento = None
        
    def atacar(self):
        if not self._encantamento:
            print(f"{self._nome} ataca com as mãos e causa 1 de dano.")
        
        if self._encantamento:
            print(f"{self._nome} lança seu feitiço {self._arma} e causa 1 de dano.")
            
class Pelotao:
    
    def __init__(self, nome):
        self._nome = nome
        self._guerreiro = None
        self._feiticeiro = None
        
    def __str__(self):
        pass
    
#Driver Code

guerreiro_1 = Guerreiro("Ricardo, Coração de Leão")
guerreiro_1.atacar()

feiticero_1 = Feiticeiro("Gandalf")
feiticero_1.atacar()

guerreiro_1._arma = True
guerreiro_1.atacar()

pelotao_1 = Pelotao("Primeiro Pelotão")


        
    