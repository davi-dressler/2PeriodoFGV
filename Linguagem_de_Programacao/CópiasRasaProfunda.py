import copy

lista = [[1], [1, 2], [1, 3], [1, 2, 4], [1, 5], [1, 2, 3, 6], [1, 7]]

lista_copiada = lista[:4]
print(lista_copiada)

lista_copiada_1 = copy.copy(lista)
print(lista_copiada_1)

lista_copiada_profunda = copy.deepcopy(lista)
print(lista_copiada_profunda)
