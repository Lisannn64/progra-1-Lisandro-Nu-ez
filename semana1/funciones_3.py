#3. Definir una función area_triangulo que reciba la base y la altura de un triángulo y 
#devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado.  
#Fórmula: area = (b * h) / 2.

def area_triangulo(base, altura) -> float:
    return (base * altura) / 2


base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))


area = area_triangulo(base, altura)
print("Base del triángulo:", base)
print("Altura del triángulo:", altura)
print("Área del triángulo:", area)