#5. Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si 
#es impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función. 

def es_par(numero):
    if numero%2==0:
        return  True
    else:
         return  False
    
pedir_numero=int(input("Ingrese el numero: "))

if es_par(pedir_numero):
    print("El número es par")
else:
    print("El número es impar")