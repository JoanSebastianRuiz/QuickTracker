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
from validaciones import *


def registrar_venta(datos):
    venta={}
    datos_clientes=cargar_datos_json(RUTA_DATOS_CLIENTES)
    bandera=False
    
    while bandera==False:
        documento=input("Ingrese el documento del cliente con el que que va a registrar la venta: ")
        if validar_longitud_documento(documento)==True and validar_contiene_contenido(documento)==True and validar_contiene_numeros(documento)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos_clientes,"documento",documento)==True:
        venta["documento"]=documento
        
        fecha_actual=datetime.now()
        venta["fecha"]=fecha_actual.strftime("%d-%m-%Y")
        venta["hora"]=fecha_actual.strftime("%H:%M")

        while bandera==False:
            departamento=input("Ingrese el departamento de la venta: ")
            if validar_contiene_contenido(departamento)==True and validar_contiene_letras(departamento)==True:
                bandera=True
        bandera=False
        venta["departamento"]=departamento
        
        while bandera==False:
            ciudad=input("Ingrese la ciudad de la venta: ")
            if validar_contiene_contenido(ciudad)==True and validar_contiene_letras(ciudad)==True:
                bandera=True
        bandera=False    
        venta["ciudad"]=ciudad

        while bandera==False:
            imprimir_opciones_venta()
            opcion_venta=socilitar_opcion()
            if opcion_venta>=1 and opcion_venta<=2 and validar_contiene_contenido(opcion_venta)==True and validar_contiene_numeros(opcion_venta)==True:
                bandera=True
            elif opcion_venta<1 or opcion_venta>2:
                print("Numero de opcion fuera de rango")
        bandera=False

        if opcion_venta==1:
            datos_servicios=cargar_datos_json(RUTA_DATOS_SERVICIOS)
            venta["tipo de venta"]="servicio"
                
            while bandera==False:
                print("Opciones de servicio: ")
                imprimir_lista_valores_llave_json(datos_servicios, "nombre")
                posicion_servicio=socilitar_opcion()
                if posicion_servicio>=1 and posicion_servicio<=len(lista_valores_llave_json(datos_servicios,"nombre")) and validar_contiene_contenido(posicion_servicio)==True and validar_contiene_numeros(posicion_servicio)==True:
                    bandera=True
                elif posicion_servicio<1 or posicion_servicio>len(lista_valores_llave_json(datos_servicios,"nombre")):
                    print("Numero de opcion fuera de rango")
                    
            bandera=False
            
            nombre_servicio=lista_valores_llave_json(datos_servicios, "nombre")[posicion_servicio-1]
            venta["articulo"]=nombre_servicio
            diccionario=ubicacion_valor(datos_servicios,"nombre",nombre_servicio)
            diccionario["clientes"].append(documento)
            venta["valor"]=diccionario["precio"]
            subir_datos_json(RUTA_DATOS_SERVICIOS ,datos_servicios)
            
        elif opcion_venta==2:
            datos_productos=cargar_datos_json(RUTA_DATOS_PRODUCTOS)
            venta["tipo de venta"]="producto"
            
            while bandera==False:
                print("Opciones de producto: ")
                imprimir_lista_valores_llave_json(datos_productos, "nombre")
                posicion_producto=socilitar_opcion()
                if posicion_producto>=1 and posicion_producto<=len(lista_valores_llave_json(datos_productos,"nombre")) and validar_contiene_contenido(posicion_producto)==True and validar_contiene_numeros(posicion_producto)==True:
                    bandera=True
                elif posicion_producto<1 or posicion_producto>len(lista_valores_llave_json(datos_productos,"nombre")):
                    print("Numero de opcion fuera de rango")
                    
            bandera=False
            
            nombre_producto=lista_valores_llave_json(datos_productos, "nombre")[posicion_producto-1]
            venta["articulo"]=nombre_producto
            diccionario=ubicacion_valor(datos_productos,"nombre",nombre_producto)
            diccionario["clientes"].append(documento)
            venta["valor"]=diccionario["precio"]
            subir_datos_json(RUTA_DATOS_PRODUCTOS,datos_productos)      
            
        datos.append(venta)
        print("La venta se ha registrado correctamente")
        print(venta)
        return datos
            
    else:
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


def imprimir_opciones_venta():
    print("Opciones de venta: ")
    print("1. Servicio")
    print("2. Producto")

