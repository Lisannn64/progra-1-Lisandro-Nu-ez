from gestion_parque.funciones import registrar_visita, mostrar_resumen



def main():
    resumen = registrar_visita()
    mostrar_resumen(resumen)

main()