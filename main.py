from operaciones.suma import suma
from operaciones.resta import resta
from operaciones.multiplicacion import multiplicacion
from operaciones.division import division

def menu():
    print("Calculadora Modular - Python")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    return input("Selecciona una opción (1-4): ")

def pedir_numeros():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    return a, b

if __name__ == "__main__":
    opcion = menu()
    a, b = pedir_numeros()

    if opcion == '1':
        print("Resultado:", suma(a, b))
    elif opcion == '2':
        print("Resultado:", resta(a, b))
    elif opcion == '3':
        print("Resultado:", multiplicacion(a, b))

    elif opcion == '4':
        print("Resultado:", division(a, b))
    else:
        print("Opción inválida.")