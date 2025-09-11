#Sumar todos los elementos: 
#Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los 
#elementos


suma=0
mi_lista=[1, 4, 7, 2, 11, 0, 9, 3, 12, 19]

for x in range(len(mi_lista)):
    suma+=mi_lista[x]
    print(suma)

