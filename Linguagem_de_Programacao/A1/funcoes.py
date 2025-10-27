# -*- coding: utf-8 -*-
"""Módulo funcões 

Possui todas as funções criadas para a resolução da A1 de Linguagens de Programação.


"""

import numpy as np
import numpy.typing as npt
from typing import Tuple, Dict, List, Callable, Any
import doctest
from functools import wraps


def validar_cnpj(cnpj: str) -> bool:
    """
    Verifica se um CNPJ é válido ou não.

    Parameters
    ----------
    cnpj : str
        CNPJ a ser verificado.

    Returns
    -------
    bool
        True se o CNPJ for válido, False, se não.
    
    Examples
    -------- 
    >>> cnpj = "40.688.134/0001-61"
    >>> validar_cnpj(cnpj)
    True

    >>> cnpj = "52.771.293/0001-12"
    >>> validar_cnpj(cnpj)
    False
    
    >>> cnpj = "11.111.111/1111-11"
    >>> validar_cnpj(cnpj)
    False
    
    """
    caracteres_especiais = "./-"
    
    # Verificações
    for ch in caracteres_especiais:
        cnpj = cnpj.replace(ch, "")
    
    if len(cnpj) != 14:
        return False
    
    # Cria uma lista que recebe True se o próximo caracter é igual ao anterior
    # Se tiver apenas True quer dizer que todos os caracteres são iguais.
    verificador = []
    for idx in range(len(cnpj)-1):
        if cnpj[idx] == cnpj[idx+1]:
            verificador.append(True)
        else:
            verificador.append(False)
    
    if False not in verificador:
        return False
    
    #Cálculo do digito 1
    pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_1 = 0
    
    for idx in range(12):
        soma_1 = soma_1 + int(cnpj[idx])*pesos_1[idx]
    if soma_1%11 < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - (soma_1%11)
    
    #Cálculo do digito 2
    pesos_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_2 = 0
    verificar = cnpj[:12] + str(primeiro_digito)
    for idx in range(13):
        soma_2 = soma_2 + int(verificar[idx])*pesos_2[idx]
        
    if soma_2%11 < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - (soma_2%11)
        
    if primeiro_digito == int(cnpj[12]) and segundo_digito == int(cnpj[13]):
        return True
    else:
        return False
    


def cache_resultados(func) -> Any:
    """
    Decorador que registra os argumentos como chaves e os resultados das funções 
    como valores em um dicionário.

    Parameters
    ----------
    func 
        Função decorada.

    Returns
    -------
    Any
        Retorno da função decorada.

    """
    
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print("Resultado retornado do chache.")
            return cache[args] 
        else: 
            resultado = func(*args)
            cache[args] = resultado
            print("Valor armazenado no cache.")
            print(cache)
            return func(*args)
        
    return wrapper

def cache_limitado(max_tamanho: int) -> Any:
    """
    Decorador que registra os argumentos como chaves e os resultados das funções 
    como valores em um dicionário limitado a max_tamanho.

    Parameters
    ----------
    max_tamanho : int
        Tamanho máximo do dicionário de armazenamento.

    Returns
    -------
    Any
        Retorno da função decorada.

    """
    def decorador(func):
        cache = {}
        chaves = []
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args in cache:
                print("Resultado retornado do chache.")
                print(cache)
                print(chaves)
                return cache[args]
            
            elif len(cache) < max_tamanho:
                resultado = func(*args)
                cache[args] = resultado
                chaves.append(args)
                print(cache)
                print(chaves)
                print("Valor armazenado no cache.")
                return func(*args)
            
            else:
                cache.pop(chaves[0])
                chaves.remove(chaves[0])
                resultado = func(*args)
                cache[args] = resultado
                chaves.append(args)
                print(cache)
                print(chaves)
                print("Último valor removido do cache. Valor atual armazenado no cache.")
                return func(*args)
                
        return wrapper
    return decorador


class DateError(Exception):
    """Ocorre quando há datas inválidas"""
    pass

def converter_data(data: str) -> tuple:
    """
    Coverte uma string representando uma data para um tupla com dia, mês e ano.
    O formato do argumento deve ser "dd/mm/YYYY"
    

    Parameters
    ----------
    data : str
        string contendo a data a ser convertida.

    Raises
    ------
    ValueError
        Se a string tiver um formato inválido.
    DateError
        Se a data for inválida. (ex: 42/08/2025).

    Returns
    -------
    tuple
        Uma tupla no formato (dd, mm, YYYY).

    """
    
    if len(data) != 10 or data[2] != "/" or data[5] != "/":
        raise ValueError("Formato de argumento inválido. Formato correto: \"dd/mm/YYYY\".")
    
    data = data.replace("/", "")
    try:
        dd = int(data[:2])
        mm = int(data[2:4])
        YYYY = int(data[4:])
    except ValueError:
        raise DateError("Data inválida.")
    
    if dd > 31 or dd < 0 or mm > 12 or mm < 0 or YYYY < 0:
        raise DateError("Data inválida.")
    
    return dd, mm, YYYY


def normalizar(arr: npt.NDArray) -> npt.NDArray:
    """
    A função recebe um array 1d e retorna um array 1D correspondente com os 
    valores normalizados para o intervalo [0,1]. 

    Parameters
    ----------
    arr : npt.NDArray
        Um array 1D a ser normalizado.

    Returns
    -------
    npt.NDArray
        Um array 1d com os valores normalizados.

    """
    
    max = np.max(arr)
    min = np.min(arr)
    intervalo = max - min
    
    if intervalo == 0:
        return np.zeros(arr.shape)
    
    arr_normalizado = (arr - min)/intervalo
    
    return arr_normalizado
    


def calcular_estatisticas(arr: npt.NDArray) -> (float, float):
    """
    Calcula a média e o desvio padrão dos elementos de um array 1D.

    Parameters
    ----------
    arr : npt.NDArray
        Um array 1D.

    Returns
    -------
    (float, float): tuple
        Uma tupla contendo Média e Desvio Padrão respectivamente.

    """
    
    media = float(np.nanmean(arr))
    num_elementos = arr.size
    
    # Um array com todos as entradas sendo a variância de cada entrada do array inicial
    arr_var = (arr - media)**2/num_elementos
    
    dp = float((np.sum(arr_var))**(1/2))
    
    return (media, dp)


if __name__ == "__main__":
    doctest.testmod(verbose= True)
    
    
    
    
    
    
    
    
    