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
	
	if not l1:
		return l2
	elif not l2:
		return l1
	else:
		return l2 + l1[1:]

#Exercicio 1.5
def inverte(lista):
	pass

#Exercicio 1.6
def capicua(lista):
	pass

#Exercicio 1.7
def concat_listas(lista):
	pass

#Exercicio 1.8
def substitui(lista, original, novo):
	pass

#Exercicio 1.9
def fusao_ordenada(lista1, lista2):
	pass

#Exercicio 1.10
def lista_subconjuntos(lista):
	pass


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
