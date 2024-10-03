def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0"
    else:
        return a / b

def mostrar_menu():
    print("\n--- Calculadora ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '5':
            print("Saliendo de la calculadora...")
            break

        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Error: Entrada inválida, por favor ingresa números válidos.")
                continue

            if opcion == '1':
                print(f"Resultado: {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {restar(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif opcion == '4':
                print(f"Resultado: {dividir(num1, num2)}")
        else:
            print("Opción no válida, por favor elige una opción del menú.")

calculadora()
