#5. Buscar un valor: 
#Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array. 
#Informar la posición en caso afirmativo, o indicar que no se encuentra. 


mi_lista=[0]*10

for x in range(len(mi_lista)):
    mi_lista[x]=int(input(f"Ingrese el valor #{x+1} "))

valor=int(input("Ingrese el numero que cree estar en la lista: "))


for i in range(len(mi_lista)):
    if mi_lista[i] == valor:
        print("Encontrado en posición", (i+1))
        break
else:
    print("No está en la lista")