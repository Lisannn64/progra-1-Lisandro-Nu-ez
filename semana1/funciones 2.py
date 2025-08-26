#2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma, 
#resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la 
#función.

def operaciones(num1, num2):
    print("Suma:", num1 + num2)
    print("Resta:", num1 - num2)
    print("Multiplicación:", num1 * num2)


num1 = float(input("Por favor ingrese el primer número a operar: "))
num2 = float(input("Ahora ingrese el segundo número a operar: "))

operaciones(num1, num2)