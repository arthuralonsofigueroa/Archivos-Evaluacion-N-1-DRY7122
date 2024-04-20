import json

def validar_json(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            json.load(archivo)
        print("El archivo JSON es válido y está correctamente estructurado.")
    except FileNotFoundError:
        print("El archivo JSON no se encontró en la ruta especificada.")
    except json.JSONDecodeError as e:
        print("Error de sintaxis JSON:", e)

validar_json('running-config.json')

