import json

RUTA_DATOS_USUARIOS="archivos/usuarios.json"
RUTA_DATOS_CLIENTES="archivos/clientes.json"
RUTA_DATOS_SERVICIOS="archivos/servicios.json"
RUTA_DATOS_PRODUCTOS="archivos/productos.json"
RUTA_DATOS_VENTAS="archivos/ventas.json"
RUTA_DATOS_PQR="archivos/pqr.json"
RUTA_DATOS_EXCEPCIONES="Archivos/excepciones.txt"

RUTA_REPORTE_PRODUCTOS="reportes/productos.txt"
RUTA_REPORTE_SERVICIOS="reportes/servicios.txt"

LISTA_CATEGORIA_CLIENTE=["nuevo","regular", "leal"]
LISTA_PQR=["consulta de servicio al cliente", "reclamacion", "sugerencia"]
LISTA_EDADES=["Adolescentes (menor de 20 años)", "Adultos jóvenes (20-39 años)", "Adultos de mediana edad (40-60 años)", "Adultos mayores (mayor de 60 años)"]


def cargar_datos_json(ruta):
    file=open(ruta)
    datos=json.load(file)
    file.close()
    return datos

def subir_datos_json(ruta, lista):
    informacion=json.dumps(lista, indent=4)
    file=open(ruta,"w")
    file.write(informacion)
    file.close()
    
def cargar_datos_txt(ruta):
    file=open(ruta)
    informacion=file.read()
    return informacion

def subir_datos_txt(ruta,cadena):
    file=open(ruta,"a")
    file.write(cadena)
    file.close()

def vaciar_datos_txt(ruta):
    file=open(ruta,"w")
    file.write("")
    file.close
    
#Lista de nombres de lista de diccionarios(json)
def lista_valores_llave_json(datos,llave):
    lista_valores=[]
    for diccionario in datos:
        for llave_local,valor in diccionario.items():
            if llave_local==llave:
                lista_valores.append(valor)
                
    set_valores=set(lista_valores)
    lista_retornar=list(set_valores)
    lista_retornar.sort()
    return lista_retornar

def imprimir_lista_valores_llave_json(datos, llave):
    nombres=lista_valores_llave_json(datos, llave)
    for i in range(len(nombres)):
        print(f"{i+1}. {nombres[i]}")