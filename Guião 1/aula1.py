#Exercicio 1.1
def comprimento(lista):

    if not lista:
        return 0
    # Caso recursivo: Remove o primeiro elemento e chama a função recursivamente
    # para a lista restante, somando 1 ao resultado.
    else:
        return 1 + comprimento(lista[1:]) 

#Exercicio 1.2
def soma(lista):
	if not lista:
		return 0	
	else:
		return lista[0] + soma(lista[1:])

#Exercicio 1.3
def existe(lista, elem):

	if not lista:	
		return False
	else:
		return lista[0] == elem or existe(lista[1:], elem)

#Exercicio 1.4
def concat(l1, l2):
    # Caso base: se uma das listas estiver vazia, retornar a outra lista
    if not l1:
        return l2
    if not l2:
        return l1
    # Caso recursivo: remover o primeiro elemento de l1 e concatenar com o resultado da chamada recursiva
    return [l1[0]] + concat(l1[1:], l2)

#Exercicio 1.5
def inverte(lista):
	if not lista:
		return []
	return [lista[-1]]+inverte(lista[:-1])

#Exercicio 1.6
def capicua(lista):
	if len(lista) <= 1:
		return True
	if lista[-1] == lista[0]:
		return capicua(lista[1:-1])
	else:
		return False

#Exercicio 1.7
def concat_listas(lista):
	if not lista:
		return []
	else:
		return concat(lista[0], concat_listas(lista[1:]))
	

#Exercicio 1.8
def substitui(lista, original, novo):
	if not lista:
		return []
	elif lista[0] == original:
		return [novo] + substitui(lista[1:],original,novo)
	else:
		return [lista[0]] + substitui(lista[1:],original,novo)

#Exercicio 1.9
def fusao_ordenada(lista1, lista2):
	if not lista1 or not lista2:
		return concat(lista1, lista2)
	elif lista1[0] < lista2[0]:
		return concat([lista1[0]], fusao_ordenada(lista1[1:], lista2))
	else:
		return concat([lista2[0]], fusao_ordenada(lista1, lista2[1:]))


#Exercicio 1.10
def lista_subconjuntos(lista):
	if not lista:
		return [[]]
	else:
		elemento = lista[0]
		subconjuntos = lista_subconjuntos(lista[1:])
		return concat(subconjuntos, [[elemento] + subset for subset in subconjuntos])


#Exercicio 2.1
def separar(lista):
	pass

#Exercicio 2.2
def remove_e_conta(lista, elem):
	pass

#Exercicio 3.1
def cabeca(lista):
	pass

#Exercicio 3.2
def cauda(lista):
	pass

#Exercicio 3.3
def juntar(l1, l2):
    pass

#Exercicio 3.4
def menor(lista):
	pass

#Exercicio 3.6
def max_min(lista):
	pass
