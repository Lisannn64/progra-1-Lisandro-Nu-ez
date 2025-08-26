#4. Crear una función buscar_mayor que reciba tres números y devuelva los tres números 
#ordenados de mayor a menor. Luego, el programa debe pedir los números y mostrar los números 
#ordenados. 

def buscar_mayor(numero1, numero2, numero3):
     if numero1 >= numero2 and numero1 >= numero3:
        mayor = numero1
     elif numero2 >= numero1 and numero2 >= numero3:
        mayor = numero2
     else:
        mayor = numero3

     if numero1 <= numero2 and numero1 <= numero3:
        menor = numero1
     elif numero2 <= numero1 and numero2 <= numero3:
        menor = numero2
     else:
        menor = numero3

    # El intermedio es el que no es ni mayor ni menor
     if numero1 != mayor and numero1 != menor:
        intermedio = numero1
     elif numero2 != mayor and numero2 != menor:
        intermedio = numero2
     else:
        intermedio = numero3
    
    
     return mayor, intermedio, menor


primer_numero=float(input("Ingrese el primer numnero: "))
segundo_numero=float(input("Ingrese el segundo numero: "))
tercer_numero=float(input("Ingrese el tercer numero: "))

mayor, intermedio, menor = buscar_mayor(primer_numero, segundo_numero, tercer_numero)
print("\nNúmero mayor:", mayor, "\nNúmero intermedio:", intermedio, "\nNúmero menor:", menor)