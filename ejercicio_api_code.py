import requests
import csv
from io import StringIO

def obtener_datos (simbolo):
    URL = f"https://stooq.com/q/l/?s={simbolo}.us&f=sd2t2ohlcv&h&e=csv"
    respuesta = requests.get(URL)
    texto = respuesta.text
    lineas = texto.slip("\n")

    encabezados = lineas [0].split(",")

    valores = lineas[1].split(",")
    resultado = {}

    for i in range (len(encabezados)):
        resultado[encabezados[i]] = valores [i]

        if resultado.get("Close") == "N/D": 
            return None
        return resultado

def opcion_consultar ():
    simbolo = input("Ingresa el símbolo búrsatil (ejemplos: aapl, tsla, ibm): ").lower()
    datos = obtener_datos(simbolo)

    if not datos: 
        print("\n No se encontraron datos para ese símbolo - CONSULTA DE BOLSA DE VALORES")
        return

    print(f"\n--- Cotización de {datos['Symbol'].upper()} ---")
    print(f"Fecha: {datos["Date"]}")
    print(f"Apertura: ${datos["Open"]}")
    print(f"Máximo: ${datos["High"]}")
    print(f"Mínimo: ${datos["Low"]}")
    print(f"Cierre: ${datos["Close"]}")
    print(f"Volumen: {datos["Volume"]}")
    

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
