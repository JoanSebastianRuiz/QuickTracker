"""
    - **Falta de Análisis de Datos**: La ausencia de un sistema de registro adecuado dificulta la recopilación y análisis 
    de datos sobre el comportamiento de los usuarios y las tendencias de consumo. La empresa no puede identificar patrones de 
    uso de servicios, preferencias de los clientes o áreas geográficas con mayor demanda, lo que limita su capacidad para tomar
    decisiones estratégicas informadas.

    - **Ventas**: la ausencia de un sistema que permita identificar y hacer seguimiento a los productos que ofrece y las ventas
    de los mismos, Claro enfrenta dificultades para llevar un registro completo de las facturas (ventas) donde se pueda 
    identificar que productos se han han vendido, cuales clientes han sido los que mas han comprado, etc.

"""

from datetime import *
from datos import *
from menus import socilitar_opcion


def registrar_venta(datos):
    venta={}
    bandera=0
    documento_encontrado=False
    documento=input("Ingrese el documento del cliente: ")
    datos_clientes=cargar_datos_json(RUTA_DATOS_CLIENTES)

    for diccionario in datos_clientes:
        if diccionario["documento"]==documento:
            documento_encontrado=True
            venta["documento"]=documento
            datos_cliente=cargar_datos_json(RUTA_DATOS_CLIENTES)
            for diccionario in datos_cliente:
                if diccionario["documento"]==documento:
                    venta["departamento"]=diccionario["departamento"]
                    venta["ciudad"]=diccionario["ciudad"]
                    break

            objeto_hora=datetime.strptime(input("Ingrese la hora: "), "%H:%M")
            venta["hora"]=str(objeto_hora.time())
            objeto_fecha=datetime.strptime(input("Ingrese la fecha: "), "%d-%m-%Y")
            venta["fecha"]=str(objeto_fecha.date())

            while bandera==0:
                print("Opciones de venta: ")
                print("1. Servicio")
                print("2. Producto")
                opcion=int(input("Ingrese la opcion de la venta que desea realizar: "))
                if opcion==1 or opcion==2:
                    bandera=1

            if opcion==1:
                print("Opciones de servicio: ")
                imprimir_lista_valores_llave_json(cargar_datos_json(RUTA_DATOS_SERVICIOS), "nombre")
                posicion_servicio=int(input("Seleccione el servicio que compro el cliente: "))-1
                venta["servicio"]=lista_valores_llave_json(cargar_datos_json(RUTA_DATOS_SERVICIOS), "nombre")[posicion_servicio]

            elif opcion==2:
                print("Opciones de producto: ")
                imprimir_lista_valores_llave_json(cargar_datos_json(RUTA_DATOS_PRODUCTOS), "nombre")
                posicion_producto=int(input("Seleccione el producto que compro el cliente: "))-1
                venta["producto"]=lista_valores_llave_json(cargar_datos_json(RUTA_DATOS_PRODUCTOS), "nombre")[posicion_producto]
            datos.append(venta)
            print("La venta se ha registrado correctamente")
            break

    if documento_encontrado==False:
        print("El documento ingresado no se encuentra registrado en la lista de clientes")

    return datos

#La empresa no puede identificar patrones de uso de servicios, preferencias de los clientes o áreas geográficas con mayor demanda
def ventas_sevicios_totales(datos):
    print("Opciones para analizar la ventas totales: ")
    print("1. Servicios")
    print("2. Productos")

    numero_opcion=socilitar_opcion()
    if numero_opcion==1:
        lista_opcion=lista_valores_llave_json(cargar_datos_json(RUTA_DATOS_SERVICIOS), "nombre")
    elif numero_opcion==2:
        lista_opcion=lista_valores_llave_json(cargar_datos_json(RUTA_DATOS_PRODUCTOS), "nombre")

    cont_opcion=[]

    for nombre_opcion in lista_opcion:
        cont=0
        for diccionario in datos:
            if diccionario["servicio"]==nombre_opcion:
                cont+=1
        cont_opcion.append(cont)
    
    for i in range(len(cont_opcion)):
        print(f"{lista_opcion[i]}: {cont_opcion[i]}")
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


