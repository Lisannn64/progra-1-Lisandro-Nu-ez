#6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva 
#cuántas horas y minutos sobran. 

def convertir_minutos(minutos):
    horas = minutos // 60          # cuántas horas completas
    minutos_sobrantes = minutos % 60  # lo que sobra
    return horas, minutos_sobrantes

# Programa principal
total_min = int(input("Ingrese la cantidad de minutos: "))

horas, minutos = convertir_minutos(total_min)
print(f"{total_min} minutos equivalen a {horas} hora(s) y {minutos} minuto(s).")