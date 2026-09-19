import requests
from api_key import API_KEY_2

FUNCION = "GLOBAL_QUOTE"
URL_BASE = "https://www.alphavantage.co/query"

def obtener_datos (simbolo):
    params =  { 
        "function": FUNCION,
        "symbol": simbolo,
        "apikey": API_KEY_2}

    respuesta = requests.get(URL_BASE, params=params)

    if respuesta.status_code != 200:
        print("\nAlgo salió mal en tu búsqueda:")
        print(respuesta.text)
        return None
    datos_json = respuesta.json()

    cotizacion = datos_json.get("Global Quote", {})

    if not cotizacion or cotizacion.get("05. price") is None:
        return None

    return cotizacion

def opcion_consultar ():
    simbolo = input("Ingresa el símbolo búrsatil (ejemplos: aapl, tsla, ibm): ").lower()
    datos = obtener_datos(simbolo)

    if not datos: 
        print("\n No se encontraron datos para ese símbolo - CONSULTA DE BOLSA DE VALORES")
        return

    print(f"\n--- Cotización de {datos['01. symbol'].upper()} ---")
    print(f"Fecha: {datos["07. latest trading day"]}")
    print(f"Apertura: ${datos["02. open"]}")
    print(f"Máximo: ${datos["03. high"]}")
    print(f"Mínimo: ${datos["04. low"]}")
    print(f"Cierre: ${datos["05. price"]}")
    print(f"Volumen: {datos["06. volume"]}")
    

def opcion_variacion():
    """Opción 2: muestra si la acción subió o bajó hoy (usa una sola consulta)."""
    simbolo = input("Ingresa el símbolo bursátil: ").lower()
    datos = obtener_datos(simbolo)

    if not datos:
        print("\nNo se encontraron datos para ese símbolo.")
        return

    cambio = float(datos["09. change"])
    porcentaje = datos["10. change percent"]

    print(f"\n--- Variación de {datos['01. symbol'].upper()} hoy ---")
    print(f"Cierre anterior: ${datos['08. previous close']}")
    print(f"Precio actual: ${datos['05. price']}")

    if cambio > 0:
        print(f"SUBIÓ ${cambio} ({porcentaje}) respecto al cierre anterior.")
    elif cambio < 0:
        print(f"BAJÓ ${abs(cambio)} ({porcentaje}) respecto al cierre anterior.")
    else:
        print("Se mantuvo sin cambios hoy.")


def opcion_alerta ():
    simbolo = input("Símbolo a verificar: ").upper()
    umbral = float(input("Precio objetivo: "))

    datos = obtener_datos(simbolo)
    if not datos: 
        print("\n No se encontraron datos para dicho símbolo.")
        return
    precio_actual = float(datos["05. price"])
    print(f"\nPrecio actual de {datos['01. symbol']}: ${precio_actual}")

    if precio_actual >= umbral:
        print(f"El precio está POR ENCIMA de tu objetivo de ${umbral}.")
    else:
        print(f"El precio está POR DEBAJO de tu objetivo de ${umbral}.")
    



def menu ():
    while True: 
        print("\n=========== MENÚ - CONSULTA DE BOLSA DE VALORES ===========")
        print("\n1. Consultar cotización de una acción" \
        "      \n2. Ver variación del día" \
        "      \n3. Verificar alterta de precio" \
        "      \n4. Salir del programa")

        user_opcion = (input("\nEscoge una opción: "))

        if user_opcion == "1":
            opcion_consultar()
        elif user_opcion == "2": 
            opcion_variacion()
        elif user_opcion == "3": 
            opcion_alerta()
        elif user_opcion == "4": 
            print("========== ¡Hasta luego! - CONSULTA DE BOLSA DE VALORES ==========")
            break
        else: 
            print("Opción no válida, intenta de nuevo")



if __name__ == "__main__":

    menu()
