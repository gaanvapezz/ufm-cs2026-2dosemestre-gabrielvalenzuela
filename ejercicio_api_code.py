import requests
import csv
from io import StringIO

def obtener_datos (simbolo):
    return

def opcion_consultar ():
    return

def opcion_comparar ():
    return

def opcion_alerta ():
    return



def menu ():
    while True: 
        print("\n=========== MENÚ - CONSULTA DE BOLSA DE VALORES ===========")
        print("\n1. Consultar cotización de una acción" \
        "      \n2. Comparar dos acciones" \
        "      \n3. Verificar alterta de precio" \
        "      \n4. Salir del programa")

        user_opcion = float(input("\nEscoge una opción: "))

        if user_opcion == 1:
            opcion_consultar()
        elif user_opcion == 2: 
            opcion_comparar()
        elif user_opcion == 3: 
            opcion_alerta()
        elif user_opcion == 4: 
            print("========== ¡Hasta luego! - CONSULTA DE BOLSA DE VALORES ==========")
        else: 
            print("Opción no válida, intenta de nuevo")




menu()
