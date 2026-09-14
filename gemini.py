"""
Ejemplo vanilla: Gemini API con requests
Para probar la capa gratuita antes de decidir si se usa en clase.

A diferencia de PokeAPI, esta API si pide autenticacion. Para conseguir
una API key gratuita (sin tarjeta):

1. Entrar a https://aistudio.google.com
2. Iniciar sesion con una cuenta de Google normal
3. Click en "Get API key" y copiar la key que genera

Documentacion oficial: https://ai.google.dev/gemini-api/docs
"""
from api_key import API_KEY
import requests

#CONSTANTES
VERBOSE = True
MODEL = "gemini-3.6-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

# PRINT DE CONFIGURACION API
if VERBOSE:
    print("-----------------------------------------------------------------------------------------")
    print (f"\nGEMINI MODEL: {MODEL}")
    print (f"\nAPI KEY: {API_KEY}")
    print("-----------------------------------------------------------------------------------------")


# CONSTRUIR HEADER CON API_KEY
headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY,
}

#------------------------------ Arriba: Constante | Abajo: Dinámico ---------------------------------------
# CONSTRUIR BODY DE REQUEST

while True: 

    print(f"-------------------- GEMINI --------------------")

    user_promt = input("\n¿Qué deseas buscar el día de hoy?" \
    "                   \no marca salir para termina la sesión: ")
    if user_promt.lower().strip() == "salir":
        print("HASTA LUEGO AMIGO!")
        break

    body = {
        "contents": [
            {
                "parts": [
                    {"text": user_promt }
                ]
            }
        ]
    }

    # REALIZAR REQUEST POST - API
    respuesta = requests.post(URL, headers=headers, json=body)

    if VERBOSE: 
        print(f"Status code: {respuesta.status_code}")

    print("Status code:", respuesta.status_code)

    if respuesta.status_code != 200:
        print("\nAlgo salio mal en tu busqueda:")
        print(respuesta.text)
    else:
        datos = respuesta.json()

        # La respuesta de Gemini viene anidada varios niveles:
        # datos -> candidates -> [0] -> content -> parts -> [0] -> text
        respuesta_gemini = datos["candidates"][0]["content"]["parts"][0]["text"]
        print("\nRespuesta de Gemini:\n")
        print(respuesta_gemini)

