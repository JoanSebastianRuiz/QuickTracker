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
from datos.manejo_datos import *
from datos.validaciones import *


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
        venta["codigo"]=len(datos)+1
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


def leer_ventas(datos):
    bandera=False
    while bandera==False:
        print("Opciones de lectura:")
        print("1. Ventas de servicios ")
        print("2. Ventas de productos")
        print("3. Ventas totales")
        opcion=socilitar_opcion()
        if opcion>=1 and opcion<=3 and validar_contiene_contenido(opcion)==True and validar_contiene_numeros(opcion)==True:
            bandera=True
        elif opcion<1 or opcion>3:
            print("Numero de opcion fuera de rango")   
    
    if opcion==1:
        for diccionario in datos:
            if diccionario["tipo de venta"]=="servicio":
                for llave, valor in diccionario.items():
                    print(f"{llave}: {valor}")
                print("")
                
    elif opcion==2:
        for diccionario in datos:
            if diccionario["tipo de venta"]=="producto":
                for llave, valor in diccionario.items():
                    print(f"{llave}: {valor}")
                print("")
                
    elif opcion==3:
        for diccionario in datos:
            for llave, valor in diccionario.items():
                print(f"{llave}: {valor}")
            print("")        


def eliminar_venta(datos):
    bandera=False
    
    while bandera==False:
        codigo=input("Ingrese el codigo la venta que quiere eliminar: ")
        if validar_contiene_contenido(codigo)==True and validar_contiene_numeros(codigo)==True:
            bandera=True   
    
    if verificar_existencia_valor(datos,"codigo",codigo)==True:
        diccionario=ubicacion_valor(datos,"codigo",codigo)
        datos.remove(diccionario)
        print("La venta se ha eliminado correctamente")
        return datos
    else:
        print("El codigo ingresado no se encuentra registrado en la lista de ventas")
        return datos

def imprimir_opciones_venta():
    print("Opciones de venta: ")
    print("1. Servicio")
    print("2. Producto")