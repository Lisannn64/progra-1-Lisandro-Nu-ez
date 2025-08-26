#8. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y 
#devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el 
#año de nacimiento del usuario y mostrar la edad calculada. 

def calcular_edad(edad):
    return (2025-edad)

año=int(input("Ingrese el año en que nació: "))


edad = calcular_edad(año)
print("Su edad es:", edad)