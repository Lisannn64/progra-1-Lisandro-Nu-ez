#8. Comparar dos arrays: 
#Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento 
#y mostrar un mensaje indicando si son o no iguales. 


mi_lista=[0]*5
lista_2=[0]*5
posicion=0


for x in range(len(mi_lista)):
    mi_lista[x]=int(input(f"Ingrese los numeros de la primer lista: #{x+1} "))
    
for y in range(len(lista_2)):
    lista_2[y]=int(input(f"Ingrese los numeros de la segunda lista: #{y+1} "))


for i in range(len(mi_lista)):
    if mi_lista[i] != lista_2[i]:
        print("Las listas NO son iguales.")
        break
else:
    print("Las dos listas son iguales elemento por elemento.")