#9. Intercambiar elementos pares por ceros: 
#Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array 
#resultante.


mi_lista=[0]*10

for x in range(len(mi_lista)):
    mi_lista[x]=int(input(f"Ingrese el numero por favor: #{x+1} "))
    if mi_lista[x]%2==0:
        mi_lista[x] = 0

print(mi_lista)