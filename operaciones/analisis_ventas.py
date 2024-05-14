from datos.validaciones import *
from datos.manejo_datos import *

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
    
    
def numero_ventas_ubicacion(datos):
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
    bandera=False
    
    if opcion==1:
        lista_productos_o_servicios=lista_valores_llave_json(datos_servicios, "nombre")
    elif opcion==2:
        lista_productos_o_servicios=lista_valores_llave_json(datos_productos, "nombre")

    while bandera==False:
        print("Analizar el numerode ventas segun: ")
        print("1. Departamento")
        print("2. Ciudad")

        opcion=socilitar_opcion()
        if opcion>=1 and opcion<=2 and validar_contiene_contenido(opcion)==True and validar_contiene_numeros(opcion)==True:
            bandera=True
        elif opcion<1 or opcion>2:
            print("Numero de opcion fuera de rango")  

    if opcion==1:
        tipo_analisis="departamento"
    elif opcion==2:
        tipo_analisis="ciudad"

    lista_valores_analisis=lista_valores_llave_json(datos,tipo_analisis)

    for nombre_lugar in lista_valores_analisis:
        cont_servicios_o_productos=[]
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                if diccionario["articulo"]==nombre_servicio_o_producto and diccionario[tipo_analisis]==nombre_lugar:
                    cont+=1
            cont_servicios_o_productos.append(cont)
        print(f"{nombre_lugar}:")
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


def numero_ventas_rango_edad(datos):
    bandera=False
    datos_productos=cargar_datos_json(RUTA_DATOS_PRODUCTOS)
    datos_servicios=cargar_datos_json(RUTA_DATOS_SERVICIOS)
    datos_clientes=cargar_datos_json(RUTA_DATOS_CLIENTES)
    
    while bandera==False:
        print("Opciones de lectura:")
        print("1. Numero de ventas por servicios ")
        print("2. Numero de ventas por productos")

        opcion=socilitar_opcion()
        if opcion>=1 and opcion<=2 and validar_contiene_contenido(opcion)==True and validar_contiene_numeros(opcion)==True:
            bandera=True
        elif opcion<1 or opcion>2:
            print("Numero de opcion fuera de rango")  
    bandera=False
    
    if opcion==1:
        lista_productos_o_servicios=lista_valores_llave_json(datos_servicios, "nombre")
    elif opcion==2:
        lista_productos_o_servicios=lista_valores_llave_json(datos_productos, "nombre")

    while bandera==False:
        print("Ver compras hechas por: ")
        print("1. Adolescentes (menor de 20 años)")
        print("2. Adultos jóvenes (20-39 años)")
        print("3. Adultos de mediana edad (40-60 años)")
        print("4. Adultos mayores (mayor de 60 años)")

        opcion=socilitar_opcion()
        if opcion>=1 and opcion<=4 and validar_contiene_contenido(opcion)==True and validar_contiene_numeros(opcion)==True:
            bandera=True
        elif opcion<1 or opcion>4:
            print("Numero de opcion fuera de rango")  
    
    if opcion==1:
        cont_servicios_o_productos=[]
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                documento=diccionario["documento"]
                diccionario_persona=ubicacion_valor(datos_clientes,"documento",documento)
                if diccionario["articulo"]==nombre_servicio_o_producto and int(diccionario_persona["edad"])<20:
                    cont+=1
            cont_servicios_o_productos.append(cont)
        print(f"{LISTA_EDADES[opcion-1]}:")
        for i in range(len(cont_servicios_o_productos)):
            print(f"{lista_productos_o_servicios[i]}: {cont_servicios_o_productos[i]}")
        print("")
    
    elif opcion==2:
        cont_servicios_o_productos=[]
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                documento=diccionario["documento"]
                diccionario_persona=ubicacion_valor(datos_clientes,"documento",documento)
                if diccionario["articulo"]==nombre_servicio_o_producto and int(diccionario_persona["edad"])>=20 and int(diccionario_persona["edad"])<=39:
                    cont+=1
            cont_servicios_o_productos.append(cont)
        print(f"{LISTA_EDADES[opcion-1]}:")
        for i in range(len(cont_servicios_o_productos)):
            print(f"{lista_productos_o_servicios[i]}: {cont_servicios_o_productos[i]}")
        print("")
    
    elif opcion==3:
        cont_servicios_o_productos=[]
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                documento=diccionario["documento"]
                diccionario_persona=ubicacion_valor(datos_clientes,"documento",documento)
                if diccionario["articulo"]==nombre_servicio_o_producto and int(diccionario_persona["edad"])>=40 and int(diccionario_persona["edad"])<=60:
                    cont+=1
            cont_servicios_o_productos.append(cont)
        print(f"{LISTA_EDADES[opcion-1]}:")
        for i in range(len(cont_servicios_o_productos)):
            print(f"{lista_productos_o_servicios[i]}: {cont_servicios_o_productos[i]}")
        print("")
    
    elif opcion==4:
        cont_servicios_o_productos=[]
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                documento=diccionario["documento"]
                diccionario_persona=ubicacion_valor(datos_clientes,"documento",documento)
                if diccionario["articulo"]==nombre_servicio_o_producto and int(diccionario_persona["edad"])>60:
                    cont+=1
            cont_servicios_o_productos.append(cont)
        print(f"{LISTA_EDADES[opcion-1]}:")
        for i in range(len(cont_servicios_o_productos)):
            print(f"{lista_productos_o_servicios[i]}: {cont_servicios_o_productos[i]}")
        print("")
    