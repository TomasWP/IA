lista = [[1,2], [3,4], [5]]


def concat_listas(lista):
	if not lista:
		return []
	else:
		return [lista[0]] + concat_listas(lista[1:])

print(concat_listas(lista))