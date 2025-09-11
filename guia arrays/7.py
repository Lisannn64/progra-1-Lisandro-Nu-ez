#. Invertir orden: 
#Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero. 


mi_lista=[0]*6

for x in range(len(mi_lista)):
    mi_lista[x]=int(input("Ingrese los numeros por favor: "))
    
print(mi_lista[::-1])