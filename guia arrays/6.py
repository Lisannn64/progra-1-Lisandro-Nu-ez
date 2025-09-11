#Mayor y su posición: 
#Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se 
#encuentra. 

mi_lista=[0]*7
maximo = mi_lista[0]
posicion=""


for x in range(len(mi_lista)):
    mi_lista[x]=int(input(f"Ingrese el numero #{x+1} "))
    if mi_lista[x] > maximo:
        maximo = mi_lista[x]
        posicion:int=x

print(f"El numero maximo está en la posición: #{posicion+1} y es: {maximo}")