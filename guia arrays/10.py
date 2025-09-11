#10. Función para buscar la primera aparición de un valor: 
#Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar 
#la posición de la primera aparición de ese número o -1 si no se encuentra. 


#el numero a buscar va a ser 64


def buscar_valor(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  # retorna la posición de la primera aparición
    return -1  # si no se encontró

# Programa principal
mi_lista = [12, 45, 64, 78, 64, 99]  # ejemplo cargado
posicion = buscar_valor(mi_lista, 64)

if posicion != -1:
    print(f"El número 64 se encontró en la posición {posicion+1}")
else:
    print("El número 64 no se encuentra en la lista.")