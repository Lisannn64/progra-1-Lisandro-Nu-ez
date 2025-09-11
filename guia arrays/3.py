#3. Promedio de valores: 
#Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio 
#de los valores. 


mi_lista=[0]*6
suma=0

for x in range(len(mi_lista)):
    mi_lista[x]=float(input(f"Ingrese el numero flotante por favor {x+1}: "))
    suma+=mi_lista[x]


promedio=suma/len(mi_lista)
print(promedio)