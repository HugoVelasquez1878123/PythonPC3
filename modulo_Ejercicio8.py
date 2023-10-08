import random

def generar_numeros_aleatorios():
    numeros_aleatorios = [random.randint(0, 100) for _ in range(20)]
    return numeros_aleatorios

def mostrar_lista(lista):
    print("La lista de números es la siguiente:")
    for numero in lista:
        print(numero, end=' ')
    print()

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada