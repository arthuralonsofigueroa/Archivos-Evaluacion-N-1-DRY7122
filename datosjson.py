import json
from datetime import datetime

ruta_archivo = "/home/devasc/labs/devnet-src/parsing/myfile.json"

try:
    with open(ruta_archivo, 'r') as archivo_json:
        ourjson = json.load(archivo_json)
    print("Archivo JSON cargado correctamente.")

    if "token" in ourjson and "expiracion" in ourjson:
        token = ourjson["token"]
        expiracion = ourjson["expiracion"]

        tiempo_restante = expiracion - datetime.now()

        print("Valor del token:", token)
        print("Tiempo restante antes de que caduque el token:", tiempo_restante)
    else:
        print("El archivo JSON no contiene información sobre el token o su tiempo de expiración.")
except FileNotFoundError:
    print("El archivo myfile.json no se encontró en la ruta especificada.")
except json.JSONDecodeError:
    print("Error al decodificar el archivo JSON. Asegúrate de que el archivo tenga un formato JSON válido.")

