#4. Contar mayores a un valor: 
#Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado. 


mi_lista=[0]*8
contador=0


for x in range(len(mi_lista)):
    mi_lista[x]=int(input(f"Ingrese un valor por favor {x+1}: "))
    if mi_lista[x] >= 100:
        contador += 1

print(contador)