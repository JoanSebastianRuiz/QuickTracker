from validaciones import *
from datos import *

#La empresa no puede identificar patrones de uso de servicios, preferencias de los clientes o áreas geográficas con mayor demanda
def numero_ventas_articulo(datos):
    bandera=False
    datos_productos=cargar_datos_json(RUTA_DATOS_PRODUCTOS)
    datos_servicios=cargar_datos_json(RUTA_DATOS_SERVICIOS)
    
    while bandera==False:
        print("Opciones de lectura:")
        print("1. Numero de ventas por servicios ")
        print("2. Numero de ventas por productos")

        opcion=socilitar_opcion()
        if opcion>=1 and opcion<=2 and validar_contiene_contenido(opcion)==True and validar_contiene_numeros(opcion)==True:
            bandera=True
        elif opcion<1 or opcion>2:
            print("Numero de opcion fuera de rango")  

    if opcion==1:
        lista_servicios=lista_valores_llave_json(datos_servicios, "nombre")
        imprimir_ventas_totales_lista(lista_servicios, datos)
    elif opcion==2:
        lista_productos=lista_valores_llave_json(datos_productos, "nombre")
        imprimir_ventas_totales_lista(lista_productos, datos)


def imprimir_ventas_totales(datos):
    datos_servicios=cargar_datos_json(RUTA_DATOS_SERVICIOS)
    lista_servicios=lista_valores_llave_json(datos_servicios, "nombre")
    ventas_servicios=ventas_totales(lista_servicios, datos)
    
    datos_productos=cargar_datos_json(RUTA_DATOS_PRODUCTOS)
    lista_productos=lista_valores_llave_json(datos_productos, "nombre")
    ventas_productos=ventas_totales(lista_productos, datos)
    
    print(f"Ventas totales de servicios: {ventas_servicios}")
    print(f"Ventas totales de productos: {ventas_productos}")
    print(f"Ventas totales: {ventas_servicios+ventas_productos}")
    print("")
    
    
def ventas_ubicacion_geografica(datos):
    print("Analizar las ventas de: ")
    print("1. Servicios")
    print("2. Productos")

    numero_opcion=socilitar_opcion()
    if numero_opcion==1:
        opcion="servicio"
        lista_productos_o_servicios=lista_valores_llave_json(cargar_datos_json(RUTA_DATOS_SERVICIOS),"nombre")
    elif numero_opcion==2:
        opcion="producto"
        lista_productos_o_servicios=lista_valores_llave_json(cargar_datos_json(RUTA_DATOS_PRODUCTOS),"nombre")

    print("Analizar las ventas segun: ")
    print("1. Departamento")
    print("2. Ciudad")

    numero_opcion=socilitar_opcion()
    if numero_opcion==1:
        opcion2="departamento"
    elif numero_opcion==2:
        opcion2="ciudad"

    lista_valores_opcion=lista_valores_llave_json(datos,opcion2)

    for valor_opcion in lista_valores_opcion:
        cont_servicios_o_productos=[]
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                if diccionario[opcion]==nombre_servicio_o_producto and diccionario[opcion2]==valor_opcion:
                    cont+=1
            cont_servicios_o_productos.append(cont)
        print(f"{valor_opcion}:")
        for i in range(len(cont_servicios_o_productos)):
            print(f"{lista_productos_o_servicios[i]}: {cont_servicios_o_productos[i]}")
        print("")
    print("")


def imprimir_ventas_totales_lista(lista, datos):
    cont_opcion=[]
    
    for nombre in lista:
        cont=0
        for diccionario in datos:
            if diccionario["articulo"]==nombre:
                cont+=1
        cont_opcion.append(cont)
    
    for i in range(len(cont_opcion)):
        print(f"{lista[i]}: {cont_opcion[i]}")
    print("")


def ventas_totales(lista, datos):
    cont_opcion=[]
    cont_total=0
    
    for nombre in lista:
        cont=0
        for diccionario in datos:
            if diccionario["articulo"]==nombre:
                cont+=1
        cont_opcion.append(cont)
    
    for i in range(len(cont_opcion)):
        cont_total+=cont_opcion[i]
    return cont_total
    