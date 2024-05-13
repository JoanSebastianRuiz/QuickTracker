from datos import *
from validaciones import *

"""
Adolescentes: 13-19 años.
Adultos jóvenes: 20-39 años.
Adultos de mediana edad: 40-59 años.
Adultos mayores: 60-79 años.
"""




def promocion_persona_sin_registrar(datos):
    bandera=False
    datos_productos=cargar_datos_json(RUTA_DATOS_PRODUCTOS)
    datos_servicios=cargar_datos_json(RUTA_DATOS_SERVICIOS)
    datos_clientes=cargar_datos_json(RUTA_DATOS_CLIENTES)
    
    while bandera==False:
        print("Desea ofertar una promocion de:")
        print("1. Servicios ")
        print("2. Productos")

        opcion=socilitar_opcion()
        if opcion>=1 and opcion<=2 and validar_contiene_contenido(opcion)==True and validar_contiene_numeros(opcion)==True:
            bandera=True
        elif opcion<1 or opcion>2:
            print("Numero de opcion fuera de rango")  
    bandera=False
    
    if opcion==1:
        lista_productos_o_servicios=lista_valores_llave_json(datos_servicios, "nombre")
        tipo_venta="servicio"
    elif opcion==2:
        lista_productos_o_servicios=lista_valores_llave_json(datos_productos, "nombre")
        tipo_venta="producto"


    while bandera==False:
        print("Desea ofertar una promocion para: ")
        print("1. Adolescentes (menor de 20 años)")
        print("2. Adultos jóvenes (20-39 años)")
        print("3. Adultos de mediana edad (40-60 años)")
        print("4. Adultos mayores (mayor de 60 años)")

        opcion=socilitar_opcion()
        if opcion>=1 and opcion<=4 and validar_contiene_contenido(opcion)==True and validar_contiene_numeros(opcion)==True:
            bandera=True
        elif opcion<1 or opcion>4:
            print("Numero de opcion fuera de rango")  
    
    diccionario_promocion={}
    cont_servicios_o_productos=[]
    
    if opcion==1:
        
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                documento=diccionario["documento"]
                diccionario_persona=ubicacion_valor(datos_clientes,"documento",documento)
                if diccionario["articulo"]==nombre_servicio_o_producto and int(diccionario_persona["edad"])<20:
                    cont+=1
            cont_servicios_o_productos.append(cont)    
    
    elif opcion==2:
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                documento=diccionario["documento"]
                diccionario_persona=ubicacion_valor(datos_clientes,"documento",documento)
                if diccionario["articulo"]==nombre_servicio_o_producto and int(diccionario_persona["edad"])>=20 and int(diccionario_persona["edad"])<=39:
                    cont+=1
            cont_servicios_o_productos.append(cont)
    
    elif opcion==3:
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                documento=diccionario["documento"]
                diccionario_persona=ubicacion_valor(datos_clientes,"documento",documento)
                if diccionario["articulo"]==nombre_servicio_o_producto and int(diccionario_persona["edad"])>=40 and int(diccionario_persona["edad"])<=60:
                    cont+=1
            cont_servicios_o_productos.append(cont)
    
    elif opcion==4:
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                documento=diccionario["documento"]
                diccionario_persona=ubicacion_valor(datos_clientes,"documento",documento)
                if diccionario["articulo"]==nombre_servicio_o_producto and int(diccionario_persona["edad"])>60:
                    cont+=1
            cont_servicios_o_productos.append(cont)

    for i in range(len(cont_servicios_o_productos)):
            diccionario_promocion[lista_productos_o_servicios[i]]=cont_servicios_o_productos[i]
    
    valor_mayor=0
    llave_mayor=""
    for llave, valor in diccionario_promocion.items():
        if valor>=valor_mayor:
            llave_mayor=llave
    
    print(f"En el rango de edades {LISTA_EDADES[opcion-1]} el {tipo_venta} mas vendido es: {llave_mayor}")