palos = ["o", "c", "e", "b"]
numeros = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]

baraja = []

def crearBaraja():
    for numero in numeros:    
            for palo in palos:
                baraja.append(numero+palo)
    return baraja

crearBaraja()
print(baraja)
