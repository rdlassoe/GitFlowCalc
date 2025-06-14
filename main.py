from operaciones.suma import suma
from operaciones.resta import resta
from operaciones.multiplicacion import multiplicacion
from operaciones.division import division
from operaciones.potencia import potencia
from operaciones.raiz import raiz

def menu():
    print("Calculadora Modular - Python")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. potencia")
    print("6. raiz")
    return input("Selecciona una opción (1-6): ")

def pedir_numeros():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    return a, b
def pedir_numero():
    a = float(input("Número: "))
    
    return a
if __name__ == "__main__":

    opcion = menu()
if opcion == '1':
    a, b = pedir_numeros()
    print("Resultado:", suma(a, b))
elif opcion == '2':
    a, b = pedir_numeros()
    print("Resultado:", resta(a, b))
elif opcion == '3':
    a, b = pedir_numeros()
    print("Resultado:", multiplicacion(a, b))
elif opcion == '4':
    a, b = pedir_numeros()
    print("Resultado:", division(a, b))
elif opcion == '5':
    a, b = pedir_numeros()
    print("Resultado:", potencia(a, b))
elif opcion == '6':
    a = pedir_numero()
    print("Resultado:", raiz(a))
else:
    print("Opción inválida.")
    