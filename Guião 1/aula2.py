from math import atan2, sqrt

#Exercicio 4.1
impar = lambda number : number % 2 !=0

#Exercicio 4.2
positivo = lambda number : number > 0

#Exercicio 4.3
comparar_modulo = lambda number_x, number_y : abs(number_x) < abs(number_y)

#Exercicio 4.4
cart2pol = lambda number_x, number_y : (sqrt(number_x**2 + number_y**2),atan2(number_y,number_x))

#Exercicio 4.5
ex5 = lambda f, g, h : lambda x, y, z : h(f(x,y),g(y,z))

#Exercicio 4.6
def quantificador_universal(lista, f):
    if not lista:
        return True
    else:
        return quantificador_universal(lista[1:],f) and f(lista[0])

#Exercicio 4.8
def subconjunto(lista1, lista2):
    if not lista1 or not lista2:
        return True
    else:
        set1 = set(lista1)
        set2 = set(lista2)
        return set1.issubset(set2)
        

#Exercicio 4.9
def menor_ordem(lista, f):
    if not lista:
        return None
    elif len(lista) == 1:
        return lista[0]
    else:
        menor = menor_ordem(lista[1:],f)
        return lista[0] if f(lista[0], menor) else menor

#Exercicio 4.10
def menor_e_resto_ordem(lista, f):
    if not lista:
        return None
    elif len(lista) == 1:
        return lista[0]
    else:
        menor = menor_ordem(lista[1:],f)
        if f(lista[0], menor):
            menor = lista[0]
        lista.pop(lista.index(menor))
        return (menor, lista)

#Exercicio 5.2
def ordenar_seleccao(lista, ordem):
    pass
