import re

def buscar_ruta_por_defecto(archivo_configuracion):
    with open(archivo_configuracion, 'r') as archivo:
        configuracion = archivo.read()


    patron = r'ip route 0\.0\.0\.0 0\.0\.0\.0 (\S+)'
    coincidencias = re.findall(patron, configuracion)

    if coincidencias:
        print("El archivo de configuración cuenta con una entrada de ruta por defecto:")
        for ruta in coincidencias:
            print("- Ruta por defecto encontrada:", ruta)
    else:
        print("El archivo de configuración no cuenta con una entrada de ruta por defecto.")

if __name__ == "__main__":
    archivo_configuracion = "RT01.cfg"  
    buscar_ruta_por_defecto(archivo_configuracion)

