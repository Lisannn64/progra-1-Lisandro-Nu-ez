def mostrar_atracciones():
    print("Estas son nuestras atracciones: \n 1- Montaña Rusa \n 2- Casa del Terror \n 3- Carrusel ")

def nombre_atraccion(elegido):
    if elegido==1:
        return "Montaña Rusa "
    elif elegido==2:
        return "Casa del Terror "
    elif elegido==3:
        return "Carrusel "
    else:
        return "Desconocido"

def elegir_atracciones():
    cantidad_atracciones = int(input("¿Cuántas atracciones querés visitar? "))
    atraccion_elegida = ""

    for x in range(cantidad_atracciones):
        atraccion = int(input("Elegí la atracción (1-3): "))
        atraccion_elegida += str(atraccion) + " "

    return atraccion_elegida



def puede_subir(edad, atraccion):
    if edad <= 6 and atraccion !=3:
        return False
    elif edad <= 12 and atraccion == 1:
        return False
    else:
        return True




def calcular_precio(atraccion):
    total=0
    if atraccion == 1:
        total=1500
    elif atraccion == 2:
        total=1200
    elif atraccion == 3:
        total = 800
    else:
        total=0
    return total




def registrar_visita():
    nombre=input("Ingrese su nombre: ")
    edad=int(input("Ingrese su edad: "))
    mostrar_atracciones()
    atracciones_elegidas=elegir_atracciones()


    total=0
    compradas=0
    detalle=""
    rechazadas=""


    for y in atracciones_elegidas:
        if y =="1" or y=="2" or y=="3":
            elegido=int(y)
            if puede_subir(edad, elegido):
                precio=calcular_precio(elegido)
                total+=precio
                compradas+=1
                detalle+= f"- {nombre_atraccion(elegido)} (${precio}\n )"
            else:
                rechazadas+= f"- {nombre_atraccion(elegido)} (NO permitido por edad)\n "
        else:
            pass
    

    descuento=0
    if compradas>=3:
        descuento=int(total*0.10)
        total=total-descuento

        
    resumen = f"""===== RESUMEN DE VISITA =====
Visitante: {nombre}
Edad: {edad}
Atracciones compradas: {compradas}
Detalle:
{detalle if detalle else "- Ninguna"}
{"Atracciones rechazadas:\n" + rechazadas if rechazadas else ""}{("Descuento aplicado (10%): $" + str(descuento) + "\n") if descuento > 0 else ""}TOTAL a pagar: ${total}
"""
    return resumen
    
def mostrar_resumen(resumen):
    print(resumen)

