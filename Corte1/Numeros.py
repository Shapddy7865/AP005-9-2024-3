import random

# Función para generar números pseudoaleatorios entre 0 y 1
def generar_numeros(cantidad):
    numeros = []
    for _ in range(cantidad):
        numeros.append(random.random())
    return numeros

# Solicitar la cantidad de números a generar
cantidad_numeros = int(input("¿Cuántos números deseas generar?: "))

# Generar los números pseudoaleatorios
numeros_generados = generar_numeros(cantidad_numeros)

# Mostrar los números generados en formato deseado
for numero in numeros_generados:
    print(f"{numero:.2f}")
    
