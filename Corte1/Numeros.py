import random

def generar_numeros(cantidad):
    numeros = []
    for _ in range(cantidad):
        numeros.append(random.random())
    return numeros

cantidad_numeros = int(input("¿Cuántos números deseas generar?: "))

numeros_generados = generar_numeros(cantidad_numeros)

for numero in numeros_generados:
    print(f"{numero:.2f}")
    
