import random

palos = ["o", "c", "e", "b"]
numeros = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]


def crearBaraja():
    baraja = []
    for numero in numeros:    
            for palo in palos:
                baraja.append(numero+palo)
    return baraja


def barajar(lista_de_naipes):
    for i in range(len(lista_de_naipes)):
        nueva_pos = random.randrange(len(lista_de_naipes))
        aux = lista_de_naipes[nueva_pos]
        lista_de_naipes[nueva_pos] = lista_de_naipes[i]
        lista_de_naipes[i] = aux
    return lista_de_naipes

print (barajar(crearBaraja()))